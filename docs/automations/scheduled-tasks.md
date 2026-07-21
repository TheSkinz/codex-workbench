# Scheduled Task Runbooks

Codex Scheduled tasks are configured outside the repository. This file is the
portable prompt and safety contract to use when creating them in the Codex
desktop or web surface.

## Shared prompt

```text
Run the named workbench loop in this repository. Read AGENTS.md and the loop
runbook first. Use an isolated worktree for any write. Process at most one item.
Run the deterministic validator before reporting success. Treat no-op as
success. Stop on dirty state, main-branch writes, missing authority, private
material, missing evidence, or any request to push without explicit approval.
Return the machine-readable loop result fields, changed paths, evidence, and
next action. Do not claim a change happened without diff or validation evidence.
```

Recommended cadence is capture weekly, research weekly, drift monthly, and
consolidation monthly. Review remains explicit until the queue proves that
scheduled review is safe and useful.

Test each prompt interactively before scheduling it. Do not commit schedule
definitions, access tokens, or local machine paths.
