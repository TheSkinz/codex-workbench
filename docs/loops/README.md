# Workbench Loops

The prototype contains five bounded agentic loops plus a deterministic health
check. Each loop has a skill, a runbook, a one-item selection rule, a safe
no-op result, and a handoff contract. Capture, review, and research can be
passed to the experimental isolated-worktree executor; drift and consolidation
remain preview/skill-driven until their write contracts are implemented.

| Loop | Default trigger | Output |
|---|---|---|
| Capture | Scheduled or explicit | Classified proposal |
| Review | Explicit or scheduled with a small queue | Evidence-backed decision record |
| Research | Scheduled or explicit | Public-source research record |
| Drift | Monthly or explicit | Exact-diff proposal branch/PR |
| Consolidation | Monthly or explicit | Bounded documentation PR |
| Health | Every run and before release | Deterministic status report |

Run a preview before any loop writes:

```powershell
python scripts/loop_preview.py --loop capture
python scripts/workbench_check.py --self-test
```

Use a dedicated worktree for unattended or scheduled changes. A dirty working
tree, a `main` branch, missing authority, or missing evidence is a safe stop.
