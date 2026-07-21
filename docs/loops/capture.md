# Capture Loop

## Trigger

Explicit `$workbench-capture` invocation or a scheduled Codex task using an
isolated worktree.

## Inputs and selection

Read public-safe Markdown files in `workbench/inbox/`. Select the oldest
eligible file by path order and process exactly one item. Ignore README files.

## Allowed writes

Create one proposal in `workbench/proposals/`. Do not edit `knowledge/` or
remove the inbox source. A proposal may recommend a later knowledge update.

## Stop and no-op rules

No eligible inbox file produces a successful `no-op`. Missing source authority,
private material, or ambiguous ownership produces `blocked` with evidence.

## Validation and handoff

Run `python scripts/workbench_check.py`. Return the proposal path, source
authority, evidence, and the next review action.
