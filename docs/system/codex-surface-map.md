# Codex Surface Map

Use the smallest Codex surface that owns the behavior.

| Need | Surface | Workbench rule |
|---|---|---|
| Durable repository behavior | `AGENTS.md` | Keep it short; reference deeper docs. |
| Repeatable workflow | Repo-local skill | Put the playbook in `.agents/skills/<name>/SKILL.md`. |
| Project defaults | `.codex/config.toml` | Safe defaults only; no credentials or personal profiles. |
| Mechanical command guard | Hook or execution rule | Enforce protected paths and unsafe commands only. |
| Scheduled cadence | Codex Scheduled task | Store the prompt/runbook here; configure schedule outside Git. |
| Parallel read-heavy work | Subagents | Require compact evidence summaries and one writer. |
| Live repository/PR state | GitHub connector or local Git | Treat returned state as evidence, not memory. |
| Deterministic enforcement | Script and fixture | Must run without a model, network, or paid API. |

Scheduled tasks are runtime state, not repository content. Local scheduled tasks
should use an isolated worktree when they can write files. The CLI can prepare
and test a task prompt, but schedule management belongs to the Codex desktop or
web surface.
