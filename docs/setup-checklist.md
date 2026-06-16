# Codex Setup Checklist

## Phase 1: Baseline repo setup

- [ ] README explains the repo purpose.
- [ ] `AGENTS.md` exists at the repo root.
- [ ] `.codex/config.toml` exists.
- [ ] `.codex/readonly.config.toml` exists.
- [ ] `.codex/careful.config.toml` exists.
- [ ] Prompt templates are documented.
- [ ] Workflow notes are documented.
- [ ] No secrets or private data are present.

## Phase 2: Verify Codex config

- [ ] Clone the repo locally.
- [ ] Start Codex from the repo root.
- [ ] Ask Codex which instruction files are active.
- [ ] Verify sandbox mode.
- [ ] Verify approval policy.
- [ ] Verify network access is disabled unless explicitly needed.

Suggested prompt:

```text
Summarize the active Codex instructions and configuration you loaded. Report active AGENTS.md files, sandbox mode, approval policy, network access, risky config values, and any instruction conflicts. Do not edit files.
```

## Phase 3: Test read-only inspection

- [ ] Run read-only mode.
- [ ] Ask Codex to inspect the repo.
- [ ] Confirm no files are modified.

```bash
codex --profile readonly
```

## Phase 4: Test small edit

- [ ] Ask Codex to make one small documentation edit.
- [ ] Review the diff.
- [ ] Run validation if applicable.
- [ ] Commit only after review.

## Phase 5: Add repo-specific AGENTS.md to real projects

- [ ] Choose one real repository.
- [ ] Ask Codex to inspect it read-only.
- [ ] Generate a minimal repo-specific `AGENTS.md`.
- [ ] Review and edit manually.
- [ ] Keep the file short.

## Phase 6: Evaluate GitHub/Codex review integration later

- [ ] Use manual Codex review first.
- [ ] Enable automated review only after manual review is useful.
- [ ] Scope integration to selected repositories.
- [ ] Avoid broad automation until rules are stable.
