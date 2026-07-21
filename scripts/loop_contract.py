#!/usr/bin/env python3
"""Shared result construction and consistency checks for workbench loops."""

from __future__ import annotations

from typing import Any


RESULTS = {"proposal", "committed", "no-op", "blocked", "failed"}
STATUS_BY_RESULT = {
    "proposal": "ok",
    "committed": "ok",
    "no-op": "ok",
    "blocked": "blocked",
    "failed": "failed",
}
ACTION_TYPES_BY_RESULT = {
    "proposal": {"review", "decide"},
    "committed": {"continue", "review"},
    "no-op": {"wait", "run", "continue"},
    "blocked": {"resolve", "run", "wait"},
    "failed": {"inspect", "retry", "resolve"},
}
DEFAULT_ACTION_TYPE = {
    "proposal": "review",
    "committed": "continue",
    "no-op": "wait",
    "blocked": "resolve",
    "failed": "inspect",
}


def make_outcome(
    *,
    run_id: str,
    loop: str,
    result: str,
    selected_input: str | None,
    evidence: list[str],
    next_action: str,
    touched_paths: list[str] | None = None,
    notes: list[str] | None = None,
    next_action_type: str | None = None,
    error_count: int | None = None,
) -> dict[str, Any]:
    action_type = next_action_type or DEFAULT_ACTION_TYPE.get(result, "resolve")
    outcome: dict[str, Any] = {
        "run_id": run_id,
        "loop": loop,
        "result": result,
        "status": STATUS_BY_RESULT.get(result, "failed"),
        "error_count": (1 if result == "failed" else 0) if error_count is None else error_count,
        "selected_input": selected_input,
        "touched_paths": touched_paths or [],
        "evidence": evidence,
        "next_action": next_action,
        "next_action_type": action_type,
    }
    if notes:
        outcome["notes"] = notes
    validate_outcome(outcome)
    return outcome


def validate_outcome(outcome: dict[str, Any]) -> None:
    """Reject contradictory machine-readable loop results before persistence."""

    result = outcome.get("result")
    if result not in RESULTS:
        raise ValueError(f"invalid loop result: {result!r}")

    expected_status = STATUS_BY_RESULT[result]
    if outcome.get("status") != expected_status:
        raise ValueError(
            f"status {outcome.get('status')!r} contradicts result {result!r}"
        )

    error_count = outcome.get("error_count")
    if not isinstance(error_count, int) or isinstance(error_count, bool) or error_count < 0:
        raise ValueError("error_count must be a non-negative integer")
    if result == "failed" and error_count < 1:
        raise ValueError("failed results must report at least one error")
    if result != "failed" and error_count != 0:
        raise ValueError("non-failed results must report error_count=0")

    next_action = outcome.get("next_action")
    if not isinstance(next_action, str) or not next_action.strip():
        raise ValueError("next_action must be a non-empty string")
    action_type = outcome.get("next_action_type")
    if action_type not in ACTION_TYPES_BY_RESULT[result]:
        raise ValueError(
            f"next_action_type {action_type!r} contradicts result {result!r}"
        )

    evidence = outcome.get("evidence")
    if not isinstance(evidence, list) or not evidence or not all(isinstance(item, str) for item in evidence):
        raise ValueError("evidence must be a non-empty list of strings")

    touched_paths = outcome.get("touched_paths")
    if not isinstance(touched_paths, list) or not all(isinstance(item, str) for item in touched_paths):
        raise ValueError("touched_paths must be a list of strings")
