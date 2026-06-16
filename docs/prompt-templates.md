# Prompt Templates

## Read-only repo inspection

```text
Inspect this repository in read-only mode.

Goals:
- Explain what this repo does.
- Identify the main entry points.
- Identify build, test, lint, and typecheck commands.
- Identify risky areas where edits should require approval.
- Recommend a minimal AGENTS.md improvement if needed.

Do not edit files.
Do not install packages.
Do not run network commands.
```

## Create a repo-level AGENTS.md

```text
Create a minimal repo-level AGENTS.md for this repository.

Process:
1. Inspect the repository structure.
2. Identify the language, framework, and package manager.
3. Identify likely install, test, lint, typecheck, build, and run commands.
4. Do not guess silently. If a command is uncertain, mark it as verify.
5. Create an AGENTS.md that is short, practical, and specific to this repo.
6. Include project overview, setup commands, validation commands, visible conventions, restricted areas, and definition of done.
7. Do not add broad philosophical instructions.
8. Show the diff before finalizing.
```

## Small controlled edit

```text
Make a small, low-risk change.

Task:
<describe the exact change>

Rules:
- First inspect the relevant files.
- Then summarize the planned edit before making changes.
- Keep the diff minimal.
- Do not add dependencies.
- Do not modify unrelated files.
- Run the narrowest relevant test or validation.
- Summarize files changed, why the change was made, validation run, and any remaining risk.
```

## Debug a failure

```text
Debug this failure systematically.

Inputs:
- Error/output: <paste>
- Recent change: <describe>
- Expected behavior: <describe>

Process:
1. Identify the smallest failing unit.
2. Form 2-3 hypotheses.
3. Check the most likely hypothesis first.
4. Make the smallest fix.
5. Re-run the relevant test.
6. Summarize root cause and prevention.
```

## Review a diff

```text
Review this diff for serious issues only.

Focus:
- Correctness regressions
- Security issues
- Missing tests
- API or contract breaks
- Error handling
- Data loss or destructive behavior

Ignore:
- Style nits handled by formatter
- Subjective refactors
- Minor naming preferences

Output:
- Blockers
- Non-blocking concerns
- Suggested tests
- Confidence level
```

## Document a workflow improvement

```text
Turn this successful Codex interaction into a reusable workflow note.

Include:
- Situation
- Prompt used
- What Codex did well
- What needed correction
- Final reusable prompt
- Validation step
- When to use this workflow again
```
