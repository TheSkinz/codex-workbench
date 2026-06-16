# Codex Workbench

This repository is a private workbench for configuring, testing, and documenting Codex workflows.

Use it for:

- testing Codex workflows
- maintaining reusable prompts
- experimenting with `AGENTS.md` behavior
- storing safe Codex config examples
- documenting setup and rollout steps

## Safety boundary

Do not store secrets, tokens, credentials, API keys, cookies, private keys, production code, customer data, or other private data in this repository.

This repo should stay lightweight: plain Markdown, TOML, and workflow notes only. Avoid adding dependencies, package managers, generated files, CI/CD automation, or build systems unless there is a specific reason and the change is reviewed first.

## Suggested use

1. Clone the repo locally.
2. Open it with Codex CLI or the Codex IDE extension.
3. Start in read-only mode when testing new prompts.
4. Use the prompt templates in `docs/prompt-templates.md`.
5. Record useful workflow improvements in `docs/codex-workflow.md`.

## Repository structure

```text
codex-workbench/
├─ README.md
├─ AGENTS.md
├─ .codex/
│  ├─ config.toml
│  ├─ readonly.config.toml
│  └─ careful.config.toml
└─ docs/
   ├─ codex-workflow.md
   ├─ prompt-templates.md
   └─ setup-checklist.md
```
