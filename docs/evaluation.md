# Harness Evaluation

Measure the harness with real work, not synthetic “agent quality” scores.

## Baseline set

Keep five small representative tasks:

1. Turn a messy request into a correctly routed task packet.
2. Inspect an unfamiliar repository without editing it.
3. Make one reversible documentation or configuration change and show the narrow validation.
4. Research a current technical decision with source-backed trade-offs.
5. Review a proposed change for contract, safety, and regression risk.

6. Preview each workbench loop with an empty queue and receive a clean `no-op`.
7. Preview a loop with one synthetic fixture and select exactly one item.
8. Run drift or consolidation on `main` or a dirty worktree and receive a safe block.

## For each run, record

- input/task packet;
- execution surface;
- usable-output time;
- correction turns;
- evidence returned;
- acceptance-check result;
- failure mode, if any.

For loop runs also record:

- loop name and selected input;
- result (`proposal`, `committed`, `no-op`, `blocked`, or `failed`);
- touched paths;
- evidence and next action.

## Promotion threshold

Make a prompt, tool, connector, or pack part of the harness only when it has been used at least three times, reduces time or correction burden, and has a practical verification method.

Do not add a model-dependent dashboard or transcript archive solely to gather
these measurements. Use the deterministic validator and loop previews, then
capture evidence when real work already happens.
