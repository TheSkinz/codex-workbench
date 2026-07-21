#!/usr/bin/env python3
"""Deterministic, dependency-free checks for the public Codex workbench."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


CONTRACTS = {
    "task-packet.schema.json": {
        "objective",
        "execution_surface",
        "authority_lane",
        "acceptance_checks",
        "deliverables",
    },
    "loop-run.schema.json": {
        "run_id",
        "loop",
        "result",
        "selected_input",
        "touched_paths",
        "evidence",
        "next_action",
    },
    "evidence-record.schema.json": {
        "title",
        "sources",
        "findings",
        "confidence",
        "uncertainty",
        "recommended_action",
    },
    "proposal.schema.json": {
        "title",
        "objective",
        "authority",
        "evidence",
        "allowed_scope",
        "blocked_scope",
        "decision",
    },
}

ENUMS = {
    "execution_surface": {"chatgpt", "deep-research", "codex", "github", "connected-app", "agent-mode"},
    "authority_lane": {"read-only", "reversible-implementation", "propose-with-default", "human-gated"},
    "loop": {"capture", "review", "research", "drift", "consolidation", "health"},
    "result": {"proposal", "committed", "no-op", "blocked", "failed"},
    "run_mode": {"preview", "interactive", "scheduled"},
    "handoff_status": {"ready", "needs-decision", "blocked", "complete"},
    "confidence": {"high", "medium", "low", "unknown"},
    "authority": {"primary", "supporting", "context-only", "unverified"},
    "decision": {"pending", "approved", "rejected", "blocked"},
}

PUBLIC_ROOTS = (
    "AGENTS.md",
    "README.md",
    ".codex",
    ".agents",
    "contracts",
    "docs",
    "knowledge",
    "workbench",
    "scripts",
    "chatgpt",
    "examples",
)
LOOP_DOCS = ("capture", "review", "research", "drift", "consolidation", "health")
PRIVATE_PATTERNS = (
    re.compile(r"[A-Za-z]:\\Users\\[A-Za-z0-9._-]+", re.IGNORECASE),
    re.compile(r"/(?:Users|home)/[A-Za-z0-9._-]+", re.IGNORECASE),
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    re.compile(r"\b(?:sk|rk)-[A-Za-z0-9]{16,}\b"),
    re.compile(r"\b(?:api[_-]?key|access[_-]?token|client[_-]?secret)\s*[:=]\s*[\"']?[A-Za-z0-9_./+=-]{16,}", re.IGNORECASE),
)


def rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def public_files(root: Path) -> list[Path]:
    paths: list[Path] = []
    for entry in PUBLIC_ROOTS:
        path = root / entry
        if path.is_file():
            paths.append(path)
        elif path.is_dir():
            paths.extend(p for p in path.rglob("*") if p.is_file() and ".git" not in p.parts)
    return sorted(set(paths))


def error(errors: list[str], path: str, message: str) -> None:
    errors.append(f"{path}: {message}")


def parse_json(path: Path, errors: list[str]) -> dict[str, Any] | None:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        error(errors, path.as_posix(), f"invalid JSON ({exc})")
        return None
    if not isinstance(value, dict):
        error(errors, path.as_posix(), "top-level JSON value must be an object")
        return None
    return value


def validate_object(value: dict[str, Any], required: set[str], name: str, errors: list[str]) -> None:
    missing = sorted(required - value.keys())
    for field in missing:
        error(errors, name, f"missing required field '{field}'")
    for field, allowed in ENUMS.items():
        if field in value and value[field] not in allowed:
            error(errors, name, f"invalid {field} value {value[field]!r}")
    for field in ("acceptance_checks", "deliverables", "evidence", "sources", "findings"):
        if field in value and (not isinstance(value[field], list) or (field in {"acceptance_checks", "deliverables", "evidence", "sources", "findings"} and not value[field])):
            error(errors, name, f"{field} must be a non-empty array")


def check_contracts(root: Path, errors: list[str]) -> None:
    contracts = root / "contracts"
    for filename, required in CONTRACTS.items():
        path = contracts / filename
        if not path.exists():
            error(errors, rel(path, root), "required contract is missing")
            continue
        schema = parse_json(path, errors)
        if schema is None:
            continue
        schema_required = set(schema.get("required", []))
        if not required <= schema_required:
            error(errors, rel(path, root), "schema required fields do not cover the workbench contract")


def check_fixtures(root: Path, errors: list[str]) -> None:
    fixtures = root / "fixtures" / "workbench"
    expected = {
        "valid-task-packet.json": CONTRACTS["task-packet.schema.json"],
        "valid-loop-run.json": CONTRACTS["loop-run.schema.json"],
    }
    for filename, required in expected.items():
        path = fixtures / filename
        value = parse_json(path, errors)
        if value is not None:
            validate_object(value, required, rel(path, root), errors)
    for filename in ("invalid-task-packet.json", "invalid-evidence-record.json"):
        if not (fixtures / filename).exists():
            error(errors, rel(fixtures / filename, root), "negative fixture is missing")


def check_skills(root: Path, errors: list[str]) -> None:
    skills_root = root / ".agents" / "skills"
    for skill_file in sorted(skills_root.glob("*/SKILL.md")):
        text = skill_file.read_text(encoding="utf-8")
        if not text.startswith("---\n") or "\n---\n" not in text[4:]:
            error(errors, rel(skill_file, root), "missing front matter")
            continue
        front = text[4:].split("\n---\n", 1)[0]
        for key in ("name:", "description:"):
            if not any(line.startswith(key) and line[len(key):].strip() for line in front.splitlines()):
                error(errors, rel(skill_file, root), f"front matter missing {key[:-1]}")


def check_loop_docs(root: Path, errors: list[str]) -> None:
    required = ("Trigger", "Inputs", "Allowed writes", "Stop", "Validation")
    for name in LOOP_DOCS:
        path = root / "docs" / "loops" / f"{name}.md"
        if not path.exists():
            error(errors, rel(path, root), "loop runbook is missing")
            continue
        text = path.read_text(encoding="utf-8")
        for token in required:
            if token.lower() not in text.lower():
                error(errors, rel(path, root), f"loop runbook does not define {token}")


def check_public_safety(root: Path, errors: list[str]) -> None:
    for path in public_files(root):
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        for pattern in PRIVATE_PATTERNS:
            if pattern.search(text):
                error(errors, rel(path, root), f"public-safety pattern matched: {pattern.pattern}")


def check_links(root: Path, errors: list[str]) -> None:
    link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for path in public_files(root):
        if path.suffix.lower() != ".md":
            continue
        text = path.read_text(encoding="utf-8")
        for target in link_pattern.findall(text):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            target = target.split("#", 1)[0]
            if not target:
                continue
            candidate = (path.parent / target).resolve()
            if not candidate.exists():
                error(errors, rel(path, root), f"broken local link: {target}")


def run_checks(root: Path) -> list[str]:
    errors: list[str] = []
    check_contracts(root, errors)
    check_fixtures(root, errors)
    check_skills(root, errors)
    check_loop_docs(root, errors)
    check_public_safety(root, errors)
    check_links(root, errors)
    return errors


def self_test(root: Path) -> list[str]:
    errors: list[str] = []
    parse_errors: list[str] = []
    invalid_task = parse_json(root / "fixtures" / "workbench" / "invalid-task-packet.json", parse_errors)
    errors.extend(parse_errors)
    if invalid_task is not None:
        findings: list[str] = []
        validate_object(invalid_task, CONTRACTS["task-packet.schema.json"], "invalid-task-packet", findings)
        if not findings:
            error(errors, "self-test", "invalid task packet did not fail validation")
    parse_errors = []
    invalid_evidence = parse_json(root / "fixtures" / "workbench" / "invalid-evidence-record.json", parse_errors)
    errors.extend(parse_errors)
    if invalid_evidence is not None:
        findings = []
        validate_object(invalid_evidence, CONTRACTS["evidence-record.schema.json"], "invalid-evidence-record", findings)
        if not findings:
            error(errors, "self-test", "invalid evidence record did not fail validation")
    if not any(pattern.search("C:\\Users\\example\\private-key") for pattern in PRIVATE_PATTERNS):
        error(errors, "self-test", "private-path detector did not fire")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()
    root = args.root.resolve()
    errors = run_checks(root)
    self_errors = self_test(root) if args.self_test else []
    all_errors = errors + self_errors
    if args.as_json:
        print(json.dumps({"root": str(root), "errors": all_errors, "error_count": len(all_errors)}, indent=2))
    else:
        for item in all_errors:
            print(f"ERROR {item}")
        suffix = "SELF-TEST " if args.self_test else ""
        print(f"{suffix}{len(all_errors)} error(s), 0 warning(s)")
    return 1 if all_errors else 0


if __name__ == "__main__":
    sys.exit(main())
