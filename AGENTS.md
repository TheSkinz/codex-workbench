# Harness Workbench Instructions

## Purpose

Maintain a small, public-safe adapter for ChatGPT and Codex. The repository contains portable routing, task-packet, configuration, and verification patterns—not domain knowledge or a second operating system.

## Boundaries

- Canonical domain knowledge belongs in its governing repository or vault.
- Generic gates and executable evaluations belong in `leverage`.
- This repository may contain only sanitized, runtime-neutral examples.
- Never add customer information, private reference packs, rates, credentials, source documents, or copied vault material.
- Do not create standing dashboards, transcript archives, broad automation, or dependency-heavy frameworks here.

## Before changing anything

1. Inspect relevant files and identify the owning layer.
2. State the intended change and the acceptance check.
3. Keep the diff small and limited to the requested adapter behavior.
4. Verify current Codex behavior from official documentation before changing configuration semantics.
5. Use `docs/pack-release.md` for any runtime-pack release or removal.

## Configuration

- `.codex/config.toml` is the repository's project configuration.
- Named profiles are loaded from `CODEX_HOME`, not from arbitrary project files. Keep examples in `examples/codex-home/`; do not claim they are active until the runtime smoke check proves it.
- Do not enable network access by default.

## Definition of done

- Changed files are public-safe and source-neutral.
- The relevant template, schema, or documentation stays internally consistent.
- A narrow validation or smoke-check instruction is recorded.
- The final summary names changed files, evidence, remaining risk, and any runtime test the user must run locally.
