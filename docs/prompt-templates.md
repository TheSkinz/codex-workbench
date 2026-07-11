# Prompt Templates

These prompts are intentionally short. Put task-specific facts in a task packet instead of accumulating permanent prompt prose.

## Inspect and route

```text
Inspect the supplied sources without editing. Identify the authoritative inputs, the correct execution surface, the required authority lane, the smallest useful deliverable, and the evidence required for completion. Return a task packet.
```

## Implement from a packet

```text
Implement the supplied task packet in this repository. Inspect the named authoritative inputs first. Stay within the allowed actions, avoid the blocked actions, and run each available acceptance check. Return changed files, validation evidence, and remaining risk.
```

## Evidence-based review

```text
Review this proposed change against the supplied task packet. Report only contract breaks, correctness regressions, privacy/security exposure, destructive behavior, and missing validation. Cite the specific evidence behind every finding. Do not edit files.
```

## Fresh-session handoff

```text
Create a compact handoff for the next session: objective, decisions already made, authoritative inputs, artifacts and paths, evidence, open risks, and the next exact action. Do not restate the full transcript.
```
