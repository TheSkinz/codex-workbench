# Loop Contract

Every loop must document these fields before implementation:

- Trigger and execution surface.
- Input scope and one-item selection rule.
- Authority lane and allowed writes.
- Explicit blocked paths and actions.
- No-op behavior.
- Stop conditions and failure result.
- Validation command.
- Handoff artifact and next action.

## Run result

The machine-readable result uses `contracts/loop-run.schema.json` and contains
the run identifier, loop name, result, normalized status, error count, selected
input, touched paths, evidence, next action, and next-action type. The result
and status must agree; failed results require a positive error count, while
other results require zero errors. The next-action type must be valid for the
result. Results are valid when they report `no-op`, `proposal`, `committed`,
`blocked`, or `failed` honestly.

## Write boundary

Preview and health commands are read-only. Agentic loops may write only inside
their declared workbench or documentation scope, and implementation work must
land in an isolated branch or worktree. No loop may push, force-push, delete,
or mutate `main` unattended.

## Local runner

Use `scripts/workbench_run.py --loop <name>` to execute the bounded preview
adapter consistently. It writes only an ignored telemetry receipt under `workbench/.state/receipts/`;
the receipt is marked `telemetry: true` and is not canonical evidence. Use
`--no-receipt` for stdout-only behavior. The runner does not call a model,
access the network, promote artifacts, or create a branch/PR.

## Execution adapter

Use `scripts/workbench_execute.py` only after the preview identifies one
eligible capture, review, or research item. The adapter requires a clean
non-`main` source checkout, creates a uniquely named `codex/*` worktree, writes
an ignored handoff packet, invokes `codex exec --json` with workspace-write and
network disabled, validates the isolated result, and preserves the worktree for
manual review. `--fake-codex` exercises the full control path without model or
network access.
