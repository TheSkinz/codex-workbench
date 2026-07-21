# Codex Workbench

A public-safe, versioned operating system for routing, executing, reviewing,
and improving work through Codex, ChatGPT, Deep Research, GitHub, and connected
tools.

This repository is not a private knowledge vault or customer-data store. It
contains generic industry concepts, synthetic examples, Codex-native skills,
bounded loops, and deterministic verification patterns.

## Architecture boundary

| System | Owns |
|---|---|
| Canonical private/domain repository | Private knowledge, operational policy, source history |
| `leverage` | Generic gates, schemas, evaluation logic, and experiments |
| This workbench | Public-safe concepts, task packets, routing rules, Codex skills, loop contracts, and setup verification |
| ChatGPT | Framing, research, route selection, task-packet drafting, evidence-based QA |

Do not use this repository as a copy of private domain instructions. Release
sanitized runtime packs only through `docs/pack-release.md`.

## Safety boundary

Assume this repository may be visible outside your private environment.

Never store customer information, internal rates, operational records, credentials, tokens, private source documents, proprietary reference packs, or personal data here. Keep public-safe examples generic.

## Start here

1. Read `AGENTS.md` and `docs/system/operating-model.md`.
2. Use `chatgpt/TASK-PACKET-TEMPLATE.md` for work that crosses a tool boundary.
3. Invoke the relevant repo-local skill from `.agents/skills/`.
4. Preview a loop with `python scripts/loop_preview.py --loop <name>`.
5. Run one bounded loop with `python scripts/workbench_run.py --loop <name>`.
6. Run `python scripts/workbench_check.py --self-test` before reporting completion.
7. Configure scheduled tasks outside Git using `docs/automations/scheduled-tasks.md`.

To exercise the Codex execution adapter safely, use its local fake executor:

```powershell
python scripts/workbench_execute.py --self-test
```

Real execution requires a clean non-`main` source checkout. The adapter creates
an isolated `codex/*` worktree, validates the result, and preserves the worktree
for manual review; it does not commit, push, or create a PR.

## Repository layout

```text
codex-workbench/
├─ AGENTS.md
├─ .agents/skills/                 # Codex-native core and loop skills
├─ .codex/config.toml              # Project defaults only
├─ chatgpt/                        # Project instructions and task packet template
├─ contracts/                      # Task, evidence, proposal, and loop contracts
├─ docs/                           # System, loop, routing, setup, and release guidance
├─ knowledge/                      # Sanitized concepts and synthetic examples
├─ workbench/                      # Inbox, proposals, reviews, research, local state
├─ examples/codex-home/            # Explicit CODEX_HOME profile examples
└─ scripts/                        # Setup, validator, loop preview, and runner
```

## Design rules

- One canonical owner per kind of information.
- Prefer a small task packet over a large context dump.
- Treat test output, diffs, and source links as completion evidence.
- Use the least-powerful tool that can complete the task safely.
- Agentic loop writes use isolated worktrees or reviewable branches.
- Deterministic checks must work without models, network, or paid APIs.
- Do not package a plugin until the repo-local workflow has real-use evidence.
