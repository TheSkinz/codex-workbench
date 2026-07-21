---
name: workbench-health
description: Run deterministic health checks for workbench contracts, skills, references, public safety, and loop readiness.
---

# Workbench Health

Use `python scripts/workbench_check.py --self-test` before release or after a
loop. Use `python scripts/loop_preview.py --loop health` for a machine-readable
status result. Do not modify files, call models, use the network, or hide
warnings. Report every failure and the exact next action.
