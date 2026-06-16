# Codex Workbench Instructions

## Purpose

This repository is a safe sandbox for configuring, testing, and documenting Codex workflows.

## Default behavior

- Inspect relevant files before editing.
- Summarize the intended change before making edits.
- Prefer small, reviewable diffs.
- Do not add dependencies unless explicitly approved.
- Do not introduce build systems, package managers, generated files, or automation unless explicitly requested.
- Do not modify unrelated files.
- After edits, summarize changed files, validation performed, and remaining risks.

## Safety

- Never add secrets, tokens, credentials, API keys, cookies, private keys, or private data.
- Do not print secrets if discovered.
- Do not run destructive commands unless explicitly authorized.
- Do not push to GitHub without explicit approval.
- Keep network access disabled unless the task explicitly requires it.

## Review behavior

- Focus on correctness, safety, clarity, maintainability, and regression risk.
- Avoid style nitpicks unless they affect readability or violate existing formatting.
- Prefer actionable findings over broad commentary.

## Definition of done

- Files are created or updated as requested.
- Markdown is clear and practical.
- TOML files are syntactically valid.
- No secrets or private data are introduced.
- Changes are summarized clearly.
