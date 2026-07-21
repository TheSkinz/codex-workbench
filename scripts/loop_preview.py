#!/usr/bin/env python3
"""Read-only preview runner for the workbench loop contracts."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

from loop_contract import make_outcome


LOOPS = ("capture", "review", "research", "drift", "consolidation", "health")


def candidates(path: Path, research_only: bool = False) -> list[Path]:
    if not path.exists():
        return []
    result = []
    for item in sorted(path.rglob("*.md")):
        if item.name.lower() == "readme.md":
            continue
        if research_only and "research-brief" not in item.read_text(encoding="utf-8").lower():
            continue
        result.append(item)
    return result


def combined_candidates(root: Path, directories: tuple[str, ...]) -> list[Path]:
    items: list[Path] = []
    for directory in directories:
        items.extend(candidates(root / directory))
    return sorted(set(items), key=lambda path: path.relative_to(root).as_posix())


def knowledge_gaps(root: Path) -> list[Path]:
    result = []
    for item in candidates(root / "knowledge"):
        text = item.read_text(encoding="utf-8").lower()
        if "knowledge gap" in text or "research gap" in text or item.stem.endswith("-gap"):
            result.append(item)
    return result


def result(
    loop: str,
    status: str,
    selected: str | None,
    evidence: list[str],
    next_action: str,
    touched: list[str] | None = None,
    next_action_type: str | None = None,
) -> dict:
    return make_outcome(
        run_id=datetime.now(timezone.utc).strftime("preview-%Y%m%dT%H%M%SZ"),
        loop=loop,
        result=status,
        selected_input=selected,
        touched_paths=touched,
        evidence=evidence,
        next_action=next_action,
        next_action_type=next_action_type,
    )


def git_state(root: Path) -> tuple[str | None, bool | None]:
    try:
        branch = subprocess.run(
            ["git", "-C", str(root), "branch", "--show-current"],
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip()
        dirty = bool(subprocess.run(
            ["git", "-C", str(root), "status", "--porcelain"],
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip())
        return branch, dirty
    except (OSError, subprocess.CalledProcessError):
        return None, None


def preview(root: Path, loop: str, require_clean: bool) -> dict:
    if loop == "health":
        check = subprocess.run(
            [sys.executable, str(root / "scripts" / "workbench_check.py"), "--json"],
            capture_output=True,
            text=True,
        )
        try:
            payload = json.loads(check.stdout)
            error_count = int(payload.get("error_count", 0))
        except (ValueError, TypeError, json.JSONDecodeError):
            error_count = 1
        if check.returncode != 0 and error_count == 0:
            error_count = 1
        status = "no-op" if check.returncode == 0 and error_count == 0 else "failed"
        next_action = "Continue with the next bounded loop" if status == "no-op" else "Fix reported validation errors before continuing"
        return result(
            loop,
            status,
            None,
            [check.stdout.strip() or "validator returned no output"],
            next_action,
            next_action_type="continue" if status == "no-op" else "resolve",
        )

    if require_clean or loop in {"drift", "consolidation"}:
        branch, dirty = git_state(root)
        if branch is None:
            return result(loop, "blocked", None, ["Git metadata is unavailable"], "Run from a Git repository", next_action_type="run")
        if branch == "main":
            return result(loop, "blocked", None, ["Current branch is main"], "Use a clean isolated worktree on a proposal branch")
        if dirty:
            return result(loop, "blocked", None, ["Working tree is dirty"], "Resolve or isolate existing changes before the loop writes")

    if loop == "capture":
        items = candidates(root / "workbench" / "inbox")
        if not items:
            return result(loop, "no-op", None, ["No eligible inbox items"], "Wait for the next public-safe handoff")
        selected = items[0].relative_to(root).as_posix()
        return result(loop, "proposal", selected, ["One inbox item selected by path order"], "Create one classified proposal after review", ["workbench/proposals/<slug>.md"], next_action_type="run")

    if loop == "review":
        items = combined_candidates(root, ("workbench/proposals", "workbench/reviews", "knowledge"))
        if not items:
            return result(loop, "no-op", None, ["No eligible proposals, reviews, or named knowledge records"], "Wait for a proposal or named record")
        selected = items[0].relative_to(root).as_posix()
        return result(loop, "proposal", selected, ["One proposal, review, or named knowledge record selected by path order"], "Create one evidence-backed review record", ["workbench/reviews/<slug>.md"], next_action_type="run")

    if loop == "research":
        items = candidates(root / "workbench" / "inbox", research_only=True) + knowledge_gaps(root)
        items = sorted(set(items), key=lambda path: path.relative_to(root).as_posix())
        if not items:
            return result(loop, "no-op", None, ["No research briefs or named knowledge gaps"], "Wait for a public research brief or named knowledge gap")
        selected = items[0].relative_to(root).as_posix()
        return result(loop, "proposal", selected, ["One research brief or named knowledge gap selected by path order"], "Create one cited research record", ["workbench/research/<slug>.md"], next_action_type="run")

    if loop == "drift":
        return result(loop, "no-op", None, ["Preview does not invent a drift finding"], "Run the drift skill to compare exact source lines", next_action_type="continue")

    return result(loop, "no-op", None, ["No consolidation candidate selected by the preview"], "Run the consolidation skill with a named candidate", next_action_type="run")


def self_test() -> None:
    with tempfile.TemporaryDirectory(prefix="codex-workbench-loop-") as temporary:
        root = Path(temporary)
        inbox = root / "workbench" / "inbox"
        inbox.mkdir(parents=True)
        item = inbox / "2026-01-01-synthetic-handoff.md"
        item.write_text("# Synthetic handoff\n\nPublic-safe fixture.\n", encoding="utf-8")
        outcome = preview(root, "capture", False)
        if outcome["result"] != "proposal" or outcome["selected_input"] != "workbench/inbox/2026-01-01-synthetic-handoff.md":
            raise AssertionError(f"one-item selection failed: {outcome}")
        (root / "knowledge").mkdir()
        (root / "knowledge" / "synthetic-gap.md").write_text("# Knowledge gap\n", encoding="utf-8")
        research = preview(root, "research", False)
        if research["selected_input"] != "knowledge/synthetic-gap.md":
            raise AssertionError(f"named knowledge gap selection failed: {research}")
        blocked = preview(root, "capture", True)
        if blocked["result"] != "blocked" or blocked["status"] != "blocked":
            raise AssertionError(f"missing Git metadata was not blocked: {blocked}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--loop", choices=LOOPS)
    parser.add_argument("--require-clean", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        print("SELF-TEST 0 error(s), 0 warning(s)")
        return 0
    if not args.loop:
        parser.error("--loop is required unless --self-test is used")
    print(json.dumps(preview(args.root.resolve(), args.loop, args.require_clean), indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
