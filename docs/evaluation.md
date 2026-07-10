# Harness Evaluation

Measure the harness with real work, not synthetic “agent quality” scores.

## Baseline set

Keep five small representative tasks:

1. Turn a messy request into a correctly routed task packet.
2. Inspect an unfamiliar repository without editing it.
3. Make one reversible documentation or configuration change and show the narrow validation.
4. Research a current technical decision with source-backed trade-offs.
5. Review a proposed change for contract, safety, and regression risk.

## For each run, record

- input/task packet;
- execution surface;
- usable-output time;
- correction turns;
- evidence returned;
- acceptance-check result;
- failure mode, if any.

## Promotion threshold

Make a prompt, tool, connector, or pack part of the harness only when it has been used at least three times, reduces time or correction burden, and has a practical verification method.

Do not add standing dashboards, recurring review queues, or tool inventory maintenance solely to gather these measurements. Capture evidence when real work already happens.
