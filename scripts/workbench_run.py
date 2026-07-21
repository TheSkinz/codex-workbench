#!/usr/bin/env python3
"""Run a bounded workbench loop and optionally persist its local receipt."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
import uuid
from datetime import datetime, timezone
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from loop_contract import validate_outcome  # noqa: E402
from loop_preview import LOOPS, preview  # noqa: E402


def new_run_id(loop: str) -> str:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return f"run-{loop}-{timestamp}-{uuid.uuid4().hex[:10]}"


def receipt_path(root: Path, run_id: str) -> Path:
    return root / "workbench" / ".state" / "receipts" / f"{run_id}.json"


def write_receipt(root: Path, outcome: dict) -> Path:
    validate_outcome(outcome)
    destination = receipt_path(root, outcome["run_id"])
    destination.parent.mkdir(parents=True, exist_ok=True)
    receipt = dict(outcome)
    receipt["telemetry"] = True
    temporary = destination.with_suffix(".tmp")
    temporary.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    temporary.replace(destination)
    return destination


def execute(root: Path, loop: str, require_clean: bool, persist: bool = True) -> tuple[dict, Path | None]:
    if not root.is_dir():
        raise ValueError(f"root does not exist or is not a directory: {root}")
    outcome = preview(root, loop, require_clean)
    outcome["run_id"] = new_run_id(loop)
    if not persist:
        validate_outcome(outcome)
        return outcome, None
    destination = receipt_path(root, outcome["run_id"])
    outcome.setdefault("notes", []).append(
        f"local_receipt={destination.relative_to(root).as_posix()}"
    )
    write_receipt(root, outcome)
    return outcome, destination


def git(root: Path, *arguments: str) -> None:
    subprocess.run(
        ["git", "-C", str(root), *arguments],
        check=True,
        capture_output=True,
        text=True,
    )


def self_test() -> None:
    with tempfile.TemporaryDirectory(prefix="codex-workbench-run-") as temporary:
        root = Path(temporary)
        inbox = root / "workbench" / "inbox"
        inbox.mkdir(parents=True)
        (inbox / "2026-01-01-synthetic-handoff.md").write_text(
            "# Synthetic handoff\n\nPublic-safe fixture.\n", encoding="utf-8"
        )

        selected, selected_receipt = execute(root, "capture", False)
        assert selected["result"] == "proposal", selected
        assert selected["status"] == "ok" and selected["error_count"] == 0, selected
        assert selected["selected_input"] == "workbench/inbox/2026-01-01-synthetic-handoff.md", selected
        assert selected_receipt and selected_receipt.exists()
        receipt = json.loads(selected_receipt.read_text(encoding="utf-8"))
        assert receipt["telemetry"] is True and receipt["status"] == selected["status"], receipt

        no_op, no_op_receipt = execute(root, "review", False)
        assert no_op["result"] == "no-op" and no_op["next_action_type"] == "wait", no_op
        assert no_op_receipt and no_op_receipt.exists()

        invalid = dict(no_op)
        invalid["status"] = "failed"
        try:
            validate_outcome(invalid)
        except ValueError:
            pass
        else:
            raise AssertionError("contradictory receipt result was accepted")

        (root / ".gitignore").write_text("workbench/.state/\n", encoding="utf-8")
        (root / "README.md").write_text("# Synthetic pilot\n", encoding="utf-8")
        git(root, "init")
        git(root, "config", "user.email", "pilot@example.invalid")
        git(root, "config", "user.name", "Synthetic Pilot")
        git(root, "add", ".gitignore", "README.md")
        git(root, "commit", "-m", "Initialize synthetic pilot")
        git(root, "branch", "-M", "main")

        protected, _ = execute(root, "drift", False)
        assert protected["result"] == "blocked", protected
        assert "main" in " ".join(protected["evidence"])

        git(root, "checkout", "-b", "pilot")
        (root / "uncommitted.md").write_text("dirty fixture\n", encoding="utf-8")
        dirty, _ = execute(root, "consolidation", False)
        assert dirty["result"] == "blocked", dirty
        assert "dirty" in " ".join(dirty["evidence"]).lower()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--loop", choices=LOOPS)
    parser.add_argument("--require-clean", action="store_true")
    parser.add_argument("--no-receipt", action="store_true", help="Do not persist ignored local state")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        print("SELF-TEST 0 error(s), 0 warning(s)")
        return 0
    if not args.loop:
        parser.error("--loop is required unless --self-test is used")
    try:
        outcome, _ = execute(args.root.resolve(), args.loop, args.require_clean, not args.no_receipt)
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        print(f"workbench run failed: {error}", file=sys.stderr)
        return 2
    print(json.dumps(outcome, indent=2))
    return 0 if outcome["result"] != "failed" else 1


if __name__ == "__main__":
    sys.exit(main())
