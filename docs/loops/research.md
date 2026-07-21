# Research Loop

## Trigger

Explicit `$workbench-research` invocation or a scheduled public-research task.

## Inputs and selection

Read one research brief from `workbench/inbox/` or a named knowledge gap.
Research only public sources and process one brief per run.

## Allowed writes

Create one evidence-backed record in `workbench/research/`. Include source
links, retrieval date, findings, uncertainty, and a recommended action. Never
build the proposed solution or convert a recommendation into a decision.

## Stop and no-op rules

No research brief is a successful `no-op`. A source that cannot be verified or
an instruction to use private material produces `blocked`.

## Validation and handoff

Run `python scripts/workbench_check.py`. Return the source list, confidence,
known gaps, and the next decision or bounded investigation.
