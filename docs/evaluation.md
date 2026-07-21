# Harness Evaluation

Measure the harness with real work, not synthetic “agent quality” scores. The
deterministic pilot below uses only repository-local synthetic fixtures.

## Five baseline tasks

1. Turn a messy request into a correctly routed task packet.
2. Inspect an unfamiliar repository without editing it.
3. Make one reversible documentation or configuration change and show the narrow validation.
4. Research a current technical decision with source-backed trade-offs.
5. Review a proposed change for contract, safety, and regression risk.

For each baseline run, record the input/task packet, execution surface,
usable-output time, correction turns, evidence returned, acceptance-check result,
failure mode, and remaining risk.

## Deterministic pilot checks

| Check | Expected result | Evidence |
|---|---|---|
| Positive fixtures for all four schemas | Pass actual schemas | `workbench_check.py --self-test` |
| Negative fixtures for malformed nested values, URLs, enums, and extra properties | Rejected | `workbench_check.py --self-test` |
| Empty capture/review/research queues | Clean `no-op` | `loop_preview.py --loop <name>` |
| Named knowledge gap selection | Exactly one research candidate | `loop_preview.py --self-test` |
| Missing Git metadata / protected branch / dirty worktree | Safe `blocked` | `loop_preview.py --self-test`, `workbench_run.py --self-test` |
| Executor missing, empty, no-op, and out-of-scope artifacts | Failed acceptance | `workbench_execute.py --self-test` |
| Executor bounded artifact in declared scope | Proposal with actual changed path | `workbench_execute.py --self-test` |
| Receipt status, error count, and next action | Consistent telemetry | `workbench_run.py --self-test` |

## Pilot record

- Evidence quality: deterministic, synthetic, and source-local; no confidential or external data used.
- Correction burden: one correction was required during stabilization when the first fake executor test revealed that its relative artifact was written from the parent process directory. The executor was corrected to run in the isolated worktree, and the negative/positive matrix then passed.
- Unexpected behavior: the prior validator accepted malformed nested values and unexpected properties; the schema-driven validator now rejects them. Ignored runtime receipts are excluded from authored-scope validation.
- Limitations: the schema interpreter intentionally implements the JSON Schema keywords used by the checked-in contracts and is not a general replacement for every Draft 2020-12 feature. Live Codex execution was not used; the executor remains experimental. No scheduled automation, plugins, MCP servers, connectors, or dependencies were added.

## Promotion threshold

Make a prompt, tool, connector, or pack part of the harness only when it has been
used at least three times, reduces time or correction burden, and has a
practical verification method. Do not add a model-dependent dashboard or
transcript archive solely to gather these measurements.
