---
name: workbench-capture
description: Process one public-safe workbench inbox item into a classified proposal without promoting it to trusted knowledge.
---

# Workbench Capture

Read `docs/loops/capture.md` and invoke `python scripts/loop_preview.py --loop capture`
first. Select one eligible item from `workbench/inbox/`, classify its authority
and intended destination, then create at most one proposal under
`workbench/proposals/`. Preserve the source and stop on private material,
missing authority, or ambiguity.
