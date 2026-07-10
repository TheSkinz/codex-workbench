# Codex Setup Checklist

## Project defaults

- [ ] The target repository has a concise, repository-specific `AGENTS.md`.
- [ ] The target repository has `.codex/config.toml` only for settings that should travel with the repository.
- [ ] Network access is disabled by default unless the task requires it.
- [ ] No secrets, customer data, or runtime-specific private settings are committed.

## Profile verification

- [ ] If named profiles are needed, copy the examples in `examples/codex-home/` to the intended `CODEX_HOME`.
- [ ] Set `CODEX_HOME` explicitly before invoking `codex --profile <name>`.
- [ ] Run `scripts/verify-codex-setup.ps1 -WorkingDirectory <target-repository> -Profile <name>` from the workbench.
- [ ] Confirm the reported active instructions, sandbox mode, approval policy, network access, and writable roots.
- [ ] Treat a profile as untrusted until this check has been performed in the real local environment.

## Task execution

- [ ] Use a task packet for non-trivial work.
- [ ] Inspect authoritative inputs before editing.
- [ ] Keep the diff within the packet's allowed actions.
- [ ] Run the narrowest relevant validation.
- [ ] Review the diff before committing or publishing.

## Reuse

- [ ] Add a reusable prompt, tool, connector, or pack only after three successful real uses.
- [ ] Record a verification method and known limits.
- [ ] Keep generic harness artifacts separate from canonical domain knowledge.
