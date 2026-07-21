# Drift Loop

## Trigger

Monthly or explicit `$workbench-drift` invocation in a clean non-`main`
worktree.

## Inputs and selection

Compare `AGENTS.md`, `.agents/skills/`, `contracts/`, `docs/`, `knowledge/`,
and `scripts/`. Select one drift finding at a time and quote the current
evidence.

## Allowed writes

Create one review/proposal record and, when approved for implementation, an
isolated branch or draft PR containing exact proposed edits. Never edit or push
`main` automatically.

## Stop and no-op rules

If the worktree is dirty, the current branch is `main`, or no exact conflict is
found, stop with `blocked` or `no-op` respectively.

## Validation and handoff

Run `python scripts/workbench_check.py` and review the diff. Return the quoted
conflict, proposed replacement, evidence, touched paths, and PR next action.
