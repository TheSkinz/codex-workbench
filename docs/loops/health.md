# Health Check

Health is deterministic and read-only. It runs before release and after every
loop preview.

## Trigger

Run before release and after every loop preview.

## Inputs

Read contracts, skills, runbooks, public-safe files, local ignored state, and
optional Git branch/worktree metadata.

## Allowed writes

None. Health is read-only and never changes repository files.

## Stop conditions

Return a failure result when validation errors exist; otherwise return a clean
status result.

It checks:

- the checked-in JSON Schemas and every positive/negative fixture against them;
- skill metadata and required loop sections;
- public-safety patterns and private paths;
- broken local Markdown references;
- ignored local state boundary;
- current branch/worktree safety when requested;
- queue counts and clean no-op eligibility;
- ignored runtime state is excluded from authored-scope validation;
- receipt fields remain contract-consistent when telemetry is present.

Use:

## Validation

```powershell
python scripts/workbench_check.py
python scripts/workbench_check.py --self-test
python scripts/loop_preview.py --loop health
```
