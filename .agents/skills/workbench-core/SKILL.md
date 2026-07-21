---
name: workbench-core
description: Apply the Codex Workbench evidence, safety, routing, and handoff rules to public-safe repository work.
---

# Workbench Core

Use for any task in this repository.

1. Read `AGENTS.md` and the relevant `docs/` runbook before acting.
2. Identify authoritative inputs, authority lane, allowed paths, blocked paths,
   acceptance checks, and evidence required.
3. Keep evidence, interpretation, proposal, and approved change separate.
4. Use `scripts/workbench_check.py` before reporting completion.
5. Do not expose or add private data, credentials, personal paths, or private
   agent state.
6. Use a worktree or non-`main` branch for writes from loops. Never push without
   explicit approval.

Return changed paths, validation output, remaining uncertainty, and the next
action. A clean no-op or explicit blocker is a valid result.
