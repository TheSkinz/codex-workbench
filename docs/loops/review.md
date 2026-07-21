# Review Loop

## Trigger

Explicit `$workbench-review` invocation. Scheduling is optional and should be
used only while the review queue remains small.

## Inputs and selection

Read one eligible file from `workbench/proposals/`, `workbench/reviews/`, or a
named knowledge record. Select by path order. Do not deeply scan unrelated
content.

## Allowed writes

Create one review record in `workbench/reviews/`. Do not apply human-gated
decisions, resolve contradictory evidence, or edit source records.

## Stop and no-op rules

An empty queue is a successful `no-op`. Missing authority or conflicting claims
without enough evidence produce `blocked` and preserve both claims.

## Validation and handoff

Run `python scripts/workbench_check.py`. Return findings, decision options,
evidence, and the exact decision required from a human.
