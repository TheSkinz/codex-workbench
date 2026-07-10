# ChatGPT + Codex Harness Workbench

A small, versioned adapter for routing work between ChatGPT, Deep Research, Codex, GitHub, and connected tools.

This repository is **not** a knowledge vault, a customer-data store, or a generic agent platform. It exists to keep the cross-tool layer small, testable, and portable.

## Architecture boundary

| System | Owns |
|---|---|
| Canonical vault / domain repository | Domain knowledge, operational policy, source history |
| `leverage` | Generic gates, schemas, evaluation logic, and experiments |
| This workbench | ChatGPT task packets, routing rules, Codex configuration examples, setup verification |
| ChatGPT | Framing, research, route selection, task-packet drafting, evidence-based QA |

Do not use this repository as a second copy of domain instructions. Release sanitized, minimal runtime packs only through the protocol in `docs/pack-release.md`.

## Safety boundary

Assume this repository may be visible outside your private environment.

Never store customer information, internal rates, operational records, credentials, tokens, private source documents, proprietary reference packs, or personal data here. Keep public-safe examples generic.

## Start here

1. Add `chatgpt/PROJECT-INSTRUCTIONS.md` to the existing AI Workflow & Agent Architecture Project.
2. Use `chatgpt/TASK-PACKET-TEMPLATE.md` for any task that crosses a tool boundary.
3. Configure a target repository with its own `AGENTS.md` and `.codex/config.toml`.
4. Run `scripts/verify-codex-setup.ps1` from the target repository before trusting a configuration.
5. Promote a reusable workflow only after it passes the evaluation rule in `docs/evaluation.md`.

## Repository layout

```text
codex-workbench/
├─ AGENTS.md
├─ .codex/config.toml              # Project defaults only
├─ chatgpt/                        # Project instructions and task packet template
├─ contracts/                      # Portable task-packet contract
├─ docs/                           # Routing, setup, evaluation, and pack-release guidance
├─ examples/codex-home/            # Explicit CODEX_HOME profile examples
└─ scripts/verify-codex-setup.ps1  # Runtime configuration smoke check
```

## Design rules

- One canonical owner per kind of information.
- Prefer a small task packet over a large context dump.
- Treat test output, diffs, and source links as completion evidence.
- Use the least-powerful tool that can complete the task safely.
- Do not add a connector, plugin, prompt, or process until real use proves its value.
