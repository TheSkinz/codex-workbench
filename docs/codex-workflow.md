# Codex Workflow

## Operating loop

1. Use ChatGPT to clarify the outcome and produce a task packet when the work is non-trivial.
2. Start Codex in the target repository, not in the harness workbench unless you are testing the harness itself.
3. Ask Codex to inspect the active instructions and relevant files before editing.
4. Keep the change bounded, run the narrowest relevant validation, and review the diff.
5. Return changed files and evidence to ChatGPT only for final synthesis or QA.

## Read-only inspection

Use a real read-only profile only after the local smoke check confirms the active configuration.

```powershell
$env:CODEX_HOME = "$HOME\.codex-harness"
codex --profile readonly "Inspect this repository. Identify entry points, validation commands, risks, and active instructions. Do not edit files."
```

The example profile files in `examples/codex-home/` are installation templates, not active configuration by themselves.

## Reversible implementation

```text
Implement this task packet. Inspect the authoritative inputs first. Keep the diff limited to the stated scope. Run each acceptance check that is available. Do not claim completion without changed-file and validation evidence.
```

## Review

Review serious issues only: contract breaks, correctness regressions, security/privacy exposure, destructive behavior, and missing validation. Ignore ordinary style preferences.

## Record a reusable improvement

A workflow becomes reusable only when it has succeeded on at least three real tasks, reduces correction burden, and has an observable verification method. Record the durable pattern in the appropriate contract or documentation file—not as a transcript.
