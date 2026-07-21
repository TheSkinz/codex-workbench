#!/usr/bin/env python3
"""Deterministic, dependency-free checks for the public Codex workbench."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


CONTRACTS = (
    "task-packet.schema.json",
    "loop-run.schema.json",
    "evidence-record.schema.json",
    "proposal.schema.json",
)

FIXTURE_SCHEMAS = {
    "task-packet": "task-packet.schema.json",
    "loop-run": "loop-run.schema.json",
    "evidence-record": "evidence-record.schema.json",
    "proposal": "proposal.schema.json",
}

# This is the complete authored public scope. Git metadata, ignored runtime
# state, caches, reports, and generated evidence are intentionally excluded.
PUBLIC_ROOTS = (
    ".agents",
    ".codex",
    ".gitattributes",
    ".gitignore",
    "AGENTS.md",
    "README.md",
    "chatgpt",
    "contracts",
    "docs",
    "examples",
    "fixtures",
    "knowledge",
    "scripts",
    "workbench",
)
IGNORED_PARTS = {
    ".git",
    ".state",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    ".venv",
    "venv",
    "reports",
    "coverage",
    "dist",
    "build",
    "evidence_packs",
}
IGNORED_SUFFIXES = {".pyc", ".pyo", ".log", ".tmp", ".bak"}
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


def is_ignored_runtime(path: Path, root: Path) -> bool:
    relative = path.relative_to(root)
    return bool(set(relative.parts) & IGNORED_PARTS) or path.suffix.lower() in IGNORED_SUFFIXES


def public_files(root: Path) -> list[Path]:
    paths: list[Path] = []
    for entry in PUBLIC_ROOTS:
        path = root / entry
        if path.is_file():
            if not is_ignored_runtime(path, root):
                paths.append(path)
        elif path.is_dir():
            paths.extend(
                p for p in path.rglob("*")
                if p.is_file() and not is_ignored_runtime(p, root)
            )
    return sorted(set(paths))


def error(errors: list[str], path: str, message: str) -> None:
    errors.append(f"{path}: {message}")


def parse_json(path: Path, errors: list[str]) -> Any | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        error(errors, path.as_posix(), f"invalid JSON ({exc})")
        return None


def _type_matches(value: Any, expected: str) -> bool:
    return {
        "object": isinstance(value, dict),
        "array": isinstance(value, list),
        "string": isinstance(value, str),
        "boolean": isinstance(value, bool),
        "null": value is None,
        "integer": isinstance(value, int) and not isinstance(value, bool),
        "number": isinstance(value, (int, float)) and not isinstance(value, bool),
    }.get(expected, True)


def _json_pointer(root_schema: dict[str, Any], pointer: str) -> dict[str, Any]:
    if not pointer.startswith("#/"):
        raise ValueError(f"unsupported schema reference: {pointer}")
    value: Any = root_schema
    for token in pointer[2:].split("/"):
        value = value[token.replace("~1", "/").replace("~0", "~")]
    if not isinstance(value, dict):
        raise ValueError(f"schema reference is not an object: {pointer}")
    return value


def validate_schema_value(
    value: Any,
    schema: dict[str, Any],
    name: str,
    root_schema: dict[str, Any] | None = None,
) -> list[str]:
    """Validate the JSON Schema subset used by the checked-in contracts."""

    root_schema = root_schema or schema
    if "$ref" in schema:
        return validate_schema_value(value, _json_pointer(root_schema, schema["$ref"]), name, root_schema)

    errors: list[str] = []
    if "type" in schema:
        expected_types = schema["type"] if isinstance(schema["type"], list) else [schema["type"]]
        if not any(_type_matches(value, expected) for expected in expected_types):
            error(errors, name, f"expected type {schema['type']!r}, got {type(value).__name__}")
            return errors
    if "enum" in schema and value not in schema["enum"]:
        error(errors, name, f"value {value!r} is not in enum")
    if "const" in schema and value != schema["const"]:
        error(errors, name, f"value {value!r} does not equal const {schema['const']!r}")

    if isinstance(value, dict):
        for required in schema.get("required", []):
            if required not in value:
                error(errors, name, f"missing required field '{required}'")
        properties = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            for key in sorted(set(value) - set(properties)):
                error(errors, f"{name}.{key}", "unexpected property")
        for key, child_schema in properties.items():
            if key in value:
                errors.extend(validate_schema_value(value[key], child_schema, f"{name}.{key}", root_schema))
        additional = schema.get("additionalProperties")
        if isinstance(additional, dict):
            for key in sorted(set(value) - set(properties)):
                errors.extend(validate_schema_value(value[key], additional, f"{name}.{key}", root_schema))
    if isinstance(value, list):
        minimum = schema.get("minItems")
        if minimum is not None and len(value) < minimum:
            error(errors, name, f"array must contain at least {minimum} item(s)")
        if "maxItems" in schema and len(value) > schema["maxItems"]:
            error(errors, name, f"array must contain at most {schema['maxItems']} item(s)")
        if isinstance(schema.get("items"), dict):
            for index, item in enumerate(value):
                errors.extend(validate_schema_value(item, schema["items"], f"{name}[{index}]", root_schema))
    if isinstance(value, str):
        if "minLength" in schema and len(value) < schema["minLength"]:
            error(errors, name, f"string must contain at least {schema['minLength']} character(s)")
        if "maxLength" in schema and len(value) > schema["maxLength"]:
            error(errors, name, f"string must contain at most {schema['maxLength']} character(s)")
        if "pattern" in schema and re.search(schema["pattern"], value) is None:
            error(errors, name, f"value does not match pattern {schema['pattern']!r}")
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if "minimum" in schema and value < schema["minimum"]:
            error(errors, name, f"value must be at least {schema['minimum']}")
    if "allOf" in schema:
        for child_schema in schema["allOf"]:
            errors.extend(validate_schema_value(value, child_schema, name, root_schema))
    if "anyOf" in schema:
        branches = [validate_schema_value(value, child, name, root_schema) for child in schema["anyOf"]]
        if all(branches):
            error(errors, name, "value did not match anyOf branches")
    if "oneOf" in schema:
        branches = [validate_schema_value(value, child, name, root_schema) for child in schema["oneOf"]]
        if sum(not branch for branch in branches) != 1:
            error(errors, name, "value did not match exactly one oneOf branch")
    return errors


def check_contracts(root: Path, errors: list[str]) -> None:
    contracts = root / "contracts"
    for filename in CONTRACTS:
        path = contracts / filename
        if not path.exists():
            error(errors, rel(path, root), "required contract is missing")
            continue
        schema = parse_json(path, errors)
        if not isinstance(schema, dict):
            error(errors, rel(path, root), "schema must be a JSON object")
            continue
        if schema.get("type") != "object" or not isinstance(schema.get("properties"), dict):
            error(errors, rel(path, root), "schema must define an object with properties")
        if schema.get("additionalProperties") is not False:
            error(errors, rel(path, root), "top-level authored contract must prohibit unexpected properties")


def check_fixtures(root: Path, errors: list[str]) -> None:
    fixtures = root / "fixtures" / "workbench"
    schemas: dict[str, dict[str, Any]] = {}
    for filename in CONTRACTS:
        schema = parse_json(root / "contracts" / filename, errors)
        if isinstance(schema, dict):
            schemas[filename] = schema
    fixture_files = sorted(fixtures.glob("valid-*.json")) + sorted(fixtures.glob("invalid-*.json"))
    if not fixture_files:
        error(errors, rel(fixtures, root), "schema fixture set is empty")
    for path in fixture_files:
        prefix, _, suffix = path.stem.partition("-")
        schema_filename = FIXTURE_SCHEMAS.get(suffix)
        if schema_filename is None:
            error(errors, rel(path, root), "fixture name does not identify a known schema")
            continue
        schema = schemas.get(schema_filename)
        if schema is None:
            continue
        parse_errors: list[str] = []
        value = parse_json(path, parse_errors)
        if parse_errors:
            errors.extend(parse_errors)
            continue
        schema_errors = validate_schema_value(value, schema, rel(path, root))
        if prefix == "valid" and schema_errors:
            errors.extend(schema_errors)
        elif prefix == "invalid" and not schema_errors:
            error(errors, rel(path, root), "negative fixture unexpectedly passed its JSON Schema")


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
    fixture_errors: list[str] = []
    check_fixtures(root, fixture_errors)
    errors.extend(fixture_errors)
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
