# Codex Workflow

## Recommended daily Codex loop

1. Start with a clear task.
2. Ask Codex to inspect relevant files before editing.
3. Have Codex summarize the intended change.
4. Approve only a small, reviewable edit.
5. Run the narrowest relevant validation.
6. Review the diff before committing.
7. Record reusable prompts or workflow improvements.

## Read-only inspection workflow

Use read-only mode when exploring unfamiliar repositories or testing prompts.

```bash
codex --profile readonly
```

Suggested prompt:

```text
Inspect this repository in read-only mode. Explain what it does, identify main entry points, find test/build/lint commands, and list risky areas that should require approval. Do not edit files.
```

## Small edit workflow

Use normal workbench mode for small, reversible changes.

```text
Make this small change: <task>. Inspect relevant files first, summarize the planned edit, keep the diff minimal, run narrow validation, and summarize changed files and remaining risk.
```

## Review workflow

Use Codex review prompts for serious issues only:

- correctness regressions
- security issues
- missing tests
- API or contract breaks
- data loss risk
- error handling gaps

Avoid style nitpicks unless formatting violates configured tooling.

## When to use careful mode

Use careful mode for high-risk debugging, complex refactors, or tasks involving ambiguous behavior.

```bash
codex --profile careful
```

## When not to use Codex

Do not use Codex for:

- secrets handling without strict controls
- production deployment changes without review
- destructive shell operations
- legal, medical, or financial decisions
- broad rewrites without tests
- tasks where requirements are unknown

## What to record after each useful workflow

Record:

- prompt used
- repo/context
- what worked
- what failed
- validation command
- whether the workflow should become a template
