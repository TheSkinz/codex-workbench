---
name: usadebusk
description: USADeBusk furnace decoking, fired heater pigging, estimating, proposal, SOP, equipment, operations, service receipt, field execution, job report, and customer-facing technical documentation workflows. Use for any USADeBusk task involving DSP or USA job numbers, heater cards, fired heater coils, pig sizing, TriMax equipment, decoking proposals, RFQs, execution plans, process flow diagrams, service receipts, payroll email bodies, ticket breakdowns, invoice readiness, or field job summaries.
---

# USADeBusk

Use this skill as the single Codex entry point for USADeBusk operational work. It routes to focused reference files so Codex loads only the facts needed for the task.

Do not assume an Obsidian or vault connection. Treat heater cards, proposals, receipts, drawings, reports, and other source documents as user-provided files or thread context unless the user explicitly points to a path.

## First Steps

1. Read `references/core.md` for every USADeBusk task.
2. Identify the task type from the request.
3. Read only the relevant task references from the routing table.
4. If source data is incomplete, list the missing fields before drafting or estimating.
5. For customer-facing output, hide internal cost basis, markup mechanics, and rate assumptions unless the reference explicitly says the item belongs in the customer document.

## Routing Table

| Task | Read these references |
| --- | --- |
| RFQ intake, proposal, duration, pricing, DSP assignment, commercial scope | `references/estimating.md` |
| SOP, procedure, PFD, pre-execution package, pigging sequence, water/metallurgy rules | `references/sop.md`; optionally `references/sop-pigging-diagrams.md` |
| Equipment specs, TriMax, filter press, pumps, pig sizing, launchers, hoses | `references/equipment.md`; optionally `references/equipment-circuit-diagrams.md` |
| Field job setup, shift extraction, shift logs, payroll email body, job status, final job report | `references/fieldpm.md`; for exact formats also read `references/fieldpm-extraction-format.md` or `references/fieldpm-report-structure.md` |
| Service receipts, ticket breakdown, invoice readiness, PDT, operations admin | `references/ops.md` |
| Coil topology, tube path, section transition, ID change reasoning | `references/core-coil-template.md` |

Do not read all references by default. Load extra references only when the task touches that domain.

## Authority Rules

- `references/core.md` governs company identity, brand standards, document numbering, terminology, heater-card schema, role boundaries, and customer-facing language.
- `references/estimating.md` governs proposal content, RFQ intake, duration logic, commercial structure, rate confirmation, and DSP workflow.
- `references/sop.md` governs procedural/SOP content, operating sequence, variant gates, PFD requirements, and stuck-pig suppression rules.
- `references/equipment.md` governs equipment specifications, pig sizing, hose/connection details, and TriMax/double-pumper terminology.
- `references/fieldpm.md` governs live field execution thread workflows.
- `references/ops.md` governs operations admin, receipt extraction, ticket breakdowns, invoice readiness, and filing.

If two references conflict, stop and identify the conflict instead of blending the rules. Ask Jesse to choose the governing source when the conflict changes customer-facing content, pricing, safety, or field execution.

## Input Gates

Before drafting a proposal, read `references/estimating.md` and confirm the RFQ intake fields that are missing.

Before drafting an SOP or PFD, read `references/sop.md` and confirm metallurgy, water source, pass/circuit count, tube IDs, footage, flange details, return bend type, launcher access, and applicable customer standards.

Before sizing pigs or selecting equipment, read `references/equipment.md` and verify tube ID, max pig OD, launcher/receiver size, hose/connection requirements, and whether a standard TriMax setup or rare double pumper is being discussed.

Before extracting service receipts or creating payroll email bodies, read `references/fieldpm.md` and `references/fieldpm-extraction-format.md`. Never guess illegible names, ticket numbers, times, or hours.

Before compiling a final job report, read `references/fieldpm.md` and `references/fieldpm-report-structure.md`. Use the user's own field observations where available.

## Codex Adaptation Notes

Some reference files originated as Claude skills. Translate legacy wording mechanically:

- "Claude" means Codex.
- "Claude Project" means the current Codex thread or project context.
- Slash commands such as `/setup`, `/extract`, `/log`, `/email`, `/status`, and `/report` are legacy trigger names. Treat equivalent natural-language requests the same way.
- Do not use or configure Obsidian unless the user explicitly asks for an Obsidian workflow.
- Do not install dependencies or create external integrations from old Claude settings.

## Output Rules

Be concise by default. Use tables or checklists when they make operational review easier. For customer-facing drafts, use USADeBusk terminology and brand guidance from `references/core.md`, avoid generic placeholder language, and preserve technical specificity.

For estimates and proposals, show the working assumptions and missing inputs before finalizing. Never reuse prior rates or third-party markup without explicit confirmation.

For procedures and SOPs, never assume metallurgy or water source. Omit stainless/passivation content unless the inputs support it.

For field and operations workflows, preserve shift labels, ticket numbers, dates, crew names, and hour categories. Flag gaps, duplicates, and overruns proactively.
