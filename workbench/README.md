# Workbench Artifacts

This directory is the portable artifact boundary for the loop prototype.

- `inbox/` — explicit handoffs and captured ideas;
- `proposals/` — classified or proposed changes;
- `reviews/` — evidence-backed decisions and questions;
- `research/` — public-source research records;
- `.state/` — local ignored telemetry only; never canonical evidence;
- `reports/` — local generated reports, not canonical source.

Loops may create proposals and review records, but they do not silently promote
them into trusted knowledge. Empty queues are clean no-ops.

The unified `scripts/workbench_run.py` command emits the common loop-run result
and stores a JSON receipt marked `telemetry: true` under the ignored
`.state/receipts/` path. Receipts are diagnostic evidence only and must be
verified against the live result. Use `--no-receipt` when a stdout-only preview
is required.
