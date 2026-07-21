# Consolidation Loop

## Trigger

Monthly or explicit `$workbench-consolidate` invocation in an isolated
worktree.

## Inputs and selection

Read only the public knowledge and documentation layer. Select one clear
duplicate, stale section, or broken reference by path order. Do not sweep the
repository broadly.

## Allowed writes

Make at most one bounded documentation/knowledge change per run and preserve
history. Produce a branch or draft PR. Do not touch configuration secrets,
private material, or unrelated code.

## Stop and no-op rules

No clear candidate is a successful `no-op`. Conflicting claims, uncertain
ownership, or a dirty worktree produces `blocked`.

## Validation and handoff

Run `python scripts/workbench_check.py`, inspect the diff, and return the
changed paths, preserved evidence, and review link/next action.
