# Harness Workbench Instructions

## Purpose

Maintain a public-safe Codex workbench: portable routing, task packets, sanitized industry concepts, Codex-native skills, bounded improvement loops, configuration examples, and deterministic verification.

## Boundaries

- Canonical private or customer-specific knowledge belongs in its governing repository or vault.
- Generic gates and executable evaluations belong in `leverage` when they are experiment-specific.
- This repository may contain only sanitized, public-safe industry concepts and synthetic examples.
- Never add customer information, private reference packs, rates, credentials, source documents, or copied vault material.
- Do not scrape private agent transcripts or commit personal Codex state.
- Agentic loops must propose through isolated worktrees or reviewable branches; never mutate `main` unattended.
- Keep deterministic validation separate from model judgment and external scheduling.

## Before changing anything

1. Inspect relevant files and identify the owning layer.
2. State the intended change and the acceptance check.
3. Keep the diff small and limited to the requested workbench behavior.
4. Verify current Codex behavior from official documentation before changing configuration semantics.
5. Use `docs/pack-release.md` for any runtime-pack release or removal.

## Configuration

- `.codex/config.toml` is the repository's project configuration.
- Named profiles are loaded from `CODEX_HOME`, not from arbitrary project files. Keep examples in `examples/codex-home/`; do not claim they are active until the runtime smoke check proves it.
- Do not enable network access by default.
- Do not commit active schedules, MCP credentials, personal profiles, or machine-specific paths.

## Definition of done

- Changed files are public-safe and source-neutral.
- The relevant template, schema, or documentation stays internally consistent.
- A narrow validation or smoke-check instruction is recorded.
- Loop behavior has a dry-run or fixture-backed acceptance check where applicable.
- The final summary names changed files, evidence, remaining risk, and any runtime test the user must run locally.
