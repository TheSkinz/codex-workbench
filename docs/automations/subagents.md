# Subagent Patterns

Use subagents only for independent read-heavy work. Each worker must return a
compact evidence summary, not raw transcripts or an unreviewed write.

Recommended roles:

- source classifier;
- public-source researcher;
- contract/schema checker;
- drift reviewer;
- security and public-safety reviewer.

The main Codex thread is the sole writer. Wait for all requested workers,
reconcile conflicting findings, then write one bounded artifact or stop.
