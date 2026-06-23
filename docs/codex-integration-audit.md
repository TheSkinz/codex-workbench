# Codex Integration Audit

Generated: 2026-06-23

Scope: audit `TheSkinz/claude-config` for migration into Codex in a way that matches Codex's instruction, skill, plugin, and project-loading model. No migration changes have been applied by this audit.

User priority update: ignore Claude-specific migration mechanics, `settings.json`, `audit/current-state-snapshot.md`, `adversarial-review`, and `usadebusk-vault-ingest` unless they contain genuinely reusable logic that improves Codex. The useful migration target is the USADeBusk operational knowledge and workflows, not parity with the old Claude setup.

## Executive Recommendation

Do not do a blind one-to-one copy of the Claude setup.

Use a layered Codex design:

1. Keep global `AGENTS.md` short and behavior-only.
2. Build one primary `usadebusk` Codex skill as the front door.
3. Put detailed estimating, SOP, equipment, operations, and field PM material behind that skill as references or sub-workflows.
4. Keep the `claude-config` repo as the source of truth for versioned skill content.
5. Package the cleaned USADeBusk workflow as a Codex plugin later only if it needs distribution across machines or teammates.

Codex can import other agent setups from the app settings, but that is not the right primary path here. The goal is not to preserve Claude behavior. The goal is to make Codex fast and accurate on USADeBusk work.

## Codex Surfaces To Use

### Global Codex guidance

Target: `C:\Users\Jwuts\.codex\AGENTS.md`

Use for personal working agreements only:

- push back when the approach is wrong or inefficient
- inspect relevant files before editing
- prefer small diffs
- ask one clarifying question when a significant task is ambiguous
- do not add dependencies without approval
- run narrow validation after edits
- summarize changed files, tests, and residual risk

Do not put USADeBusk rates, SOP details, equipment specs, proposal structure, or vault schema here. Global guidance loads in every Codex session, so domain facts here would become context tax on unrelated work.

Current state: this file already exists and contains solid generic working agreements. It should be augmented carefully, not replaced wholesale by `CLAUDE.md`.

### User-scoped skills

Target: `C:\Users\Jwuts\.agents\skills`

Use for reusable USADeBusk workflows and domain knowledge that should be available across repos and folders.

Current state: existing user skills are `find-skills`, `obsidian-cli`, and `obsidian-markdown`. No name collisions were found with the USADeBusk skills.

Recommended first install:

- one `usadebusk` router skill
- detailed reference files for estimating, SOPs, equipment, operations, and field PM
- optional separate skills only if trigger behavior proves unreliable in use

### Vault project guidance

Target: `C:\Users\Jwuts\OneDrive\obsidian-usadebusk\AGENTS.md`

Defer this unless Codex is launched directly inside the vault often. If used, keep it narrow and local:

- source-of-truth path and vault structure
- OneDrive safety rules
- finalized/client-deliverable document confirmation gates
- Obsidian formatting conventions
- instruction precedence for vault work

Do not use vault guidance as a second copy of USADeBusk operating knowledge. That belongs in the `usadebusk` skill and its references.

### Plugin

Target: future `usadebusk-codex` plugin in this repo.

Use a plugin only after the skill set is clean, because plugins are best as distribution bundles. A plugin can bundle all USADeBusk skills, app/MCP metadata, icons, and optional UI metadata. It is the right long-term format if this setup should be installable on another machine.

## File Mapping

| Claude source | Codex destination | Recommendation |
| --- | --- | --- |
| `CLAUDE.md` | optional notes only | Ignore unless extracting a small number of durable working preferences. Do not spend migration effort preserving Claude behavior. |
| `settings.json` | ignore | No meaningful Codex value unless a plugin entry points to a capability Codex lacks. None found so far. |
| `skills/usadebusk-core` | `~/.agents/skills/usadebusk` or reference | High-value core. Use as the router/front door plus canonical brand, terminology, heater-card schema, and boundaries. |
| `skills/usadebusk-estimating` | `usadebusk/references/estimating.md` | High-value. Keep intake gates, duration model, pricing rules, proposal structure, and rate-confirmation discipline. |
| `skills/usadebusk-sop` | `usadebusk/references/sop.md` | High-value. Keep variant gates, decoking sequence, SOP structure, PFD requirements, and suppression rules. |
| `skills/usadebusk-equipment` | `usadebusk/references/equipment.md` | High-value. Keep hardware specs, pig sizing rules, hose/connection details, and equipment diagrams. |
| `skills/usadebusk-fieldpm` | `usadebusk/references/fieldpm.md` | High-value if field execution threads are common. Keep receipt extraction, shift logs, payroll email, status, and report workflows. |
| `skills/usadebusk-ops` | `usadebusk/references/ops.md` | Medium-value. Keep invoice readiness, ticket breakdown, service receipt, and filing logic. |
| `skills/usadebusk-vault-ingest` | ignore by default | Out of current scope unless document ingest becomes an active workflow. Salvage only routing/collision logic if needed later. |
| `skills/adversarial-review` | ignore | Not worth migration unless explicitly requested later. |
| `audit/current-state-snapshot.md` | ignore | Historical inventory only. Do not load or migrate. |

## Skill Audit

| Skill | Lines | Reference files | Codex fit |
| --- | ---: | ---: | --- |
| `adversarial-review` | 276 | 0 | Needs rewrite. It is packaged as an archive and contains Claude-specific tools/model names. |
| `usadebusk-core` | 125 | 1 | Good fit. |
| `usadebusk-equipment` | 105 | 1 | Good fit. |
| `usadebusk-estimating` | 223 | 0 | Good fit, but may benefit from reference split. |
| `usadebusk-fieldpm` | 95 | 2 embedded | Needs unpacking and Codex wording. |
| `usadebusk-ops` | 100 | 0 | Good fit. |
| `usadebusk-sop` | 189 | 2 | Good fit. |
| `usadebusk-vault-ingest` | 376 | 2 | Good fit conceptually, but should be refactored for progressive disclosure and safer write gates. |

## Migration Hotspots

The following hotspots matter only if the related workflow stays in scope. Given the revised priority, focus on the USADeBusk domain material first and defer Claude-specific compatibility cleanup.

### 1. Claude slash commands

Affected skills:

- `usadebusk-fieldpm`
- `usadebusk-vault-ingest` if revived later
- `adversarial-review` if revived later

Codex can use slash commands in some surfaces, but skills should not depend on Claude command syntax. Rewrite triggers as natural language plus explicit skill invocation examples.

Example:

- Claude: `/dry-run [path]`
- Codex: "Dry-run ingest this file into the USADeBusk vault" or `$usadebusk-vault-ingest dry-run ...`

### 2. Claude tool names and model names

Affected skill:

- `adversarial-review`

Low priority. Ignore unless the skill is revived.

Remove Claude-specific frontmatter and body assumptions:

- `allowed-tools`
- `user-invocable`
- `argument-hint`
- `Agent`
- `AskUserQuestion`
- `Opus`
- `Bash`, `Read`, `Glob`, `Grep`, `Write`, `Edit`

Codex frontmatter should use only `name` and `description`. UI metadata and invocation policy belong in `agents/openai.yaml`.

### 3. Packaged archive skills

Affected skills:

- `adversarial-review`
- `usadebusk-fieldpm`

Both are currently archives stored at `SKILL.md`. Only `usadebusk-fieldpm` is worth unpacking now.

### 4. Ingestion dependencies

Affected skill:

- `usadebusk-vault-ingest`

Low priority under the revised scope.

The skill assumes MarkItDown. Do not add that dependency automatically. Codex currently has document and PDF skills available, so the initial Codex version should prefer existing document/PDF tooling and make MarkItDown optional.

### 5. OneDrive writes

Affected skill:

- `usadebusk-vault-ingest`

Low priority under the revised scope.

Any workflow that writes into `C:\Users\Jwuts\OneDrive\obsidian-usadebusk` needs explicit confirmation in this environment when it is outside the current workspace. Keep dry-run mandatory, and require a user confirmation before actual ingest writes.

### 6. Context duplication

The existing audit already identified repeated rules across global instructions, vault instructions, context notes, and skills. Codex's progressive disclosure model makes duplication more expensive. Pick single authorities:

- Working style: global `AGENTS.md`
- Brand and terminology: `usadebusk-core`
- Proposal content and bid intake: `usadebusk-estimating`
- SOP/procedural content: `usadebusk-sop`
- Equipment specs: `usadebusk-equipment`
- Vault routing and ingestion: `usadebusk-vault-ingest`
- Vault formatting and local vault behavior: vault root `AGENTS.md`

Everything else should point to these authorities instead of restating them.

## Proposed Codex Skill Shape

The preferred first-pass Codex shape is one primary skill:

```text
usadebusk/
  SKILL.md
  agents/openai.yaml
  references/
    core.md
    estimating.md
    sop.md
    equipment.md
    fieldpm.md
    ops.md
    coil-topology.md
    equipment-circuit-diagrams.md
    sop-pigging-diagrams.md
```

Use separate skills only if one primary skill becomes too broad in practice.

If separate skills are kept, each migrated skill should have:

```text
skill-name/
  SKILL.md
  agents/openai.yaml
  references/
  scripts/       # only when deterministic execution is needed
  assets/        # only when output templates or media are needed
```

Only `SKILL.md` is required. `agents/openai.yaml` is recommended for app display metadata and invocation policy.

### `usadebusk-core`

Keep in `SKILL.md`:

- company identity
- brand standards
- document numbering
- core terminology
- heater card schema
- customer-facing language boundaries

Keep as reference:

- coil topology template

### `usadebusk-estimating`

Keep in `SKILL.md`:

- required intake fields
- duration model
- proposal-generation guardrails
- rate confirmation rules
- proposal section order

Move to references if trimming:

- baseline rate table
- detailed section templates
- customer type notes

### `usadebusk-sop`

Keep in `SKILL.md`:

- required inputs
- variant selection gates
- decoking sequence
- SOP structure
- suppression gate for lodged-pig procedure

Keep in references:

- pigging diagrams
- lodged/stuck pig procedure

Consider moving to references:

- long plug-header/mule-ear procedure

### `usadebusk-fieldpm`

Rewrite around Codex thread state:

- "Use one Codex thread per field job."
- "Treat setup output as the anchor record."
- "Read prior messages in this thread for extractions/logs/status."
- "Do not pull operational data from another thread without explicit request."

Replace command-only triggers with natural language triggers:

- setup job
- extract service receipts
- log shift note
- draft payroll email
- summarize status
- compile final report

Use the existing document skill for final DOCX generation.

### `usadebusk-ops`

Clarify that this is for back-office operations and invoice readiness. Let `usadebusk-fieldpm` own live job thread workflows. This reduces double-triggering on service receipt tasks.

### `usadebusk-vault-ingest`

This should be the most carefully refactored skill.

Recommended structure:

```text
usadebusk-vault-ingest/
  SKILL.md
  references/
    document-routing.md
    vault-onedrive-safety.md
    heater-card-template.md
    dry-run-output.md
  scripts/
    classify_document.py        # optional later
    build_heater_card.py        # optional later
    validate_frontmatter.py     # optional later
```

Keep the first Codex migration instruction-only unless deterministic scripts are clearly needed. Add scripts after the workflow has been exercised a few times.

### `adversarial-review`

Make explicit-only by adding:

```yaml
policy:
  allow_implicit_invocation: false
```

in `agents/openai.yaml`.

Rewrite it as a Codex review orchestration skill:

- use Codex subagents when available
- otherwise run a single-agent review with explicit adversarial passes
- do not assume Claude Opus or Claude Agent tools
- present findings before fixes
- require user approval before applying changes

## Suggested Migration Plan

### Phase 1: Curated local install

1. Create a Codex-ready skill source tree in this repo, for example `codex/skills/`.
2. Unpack `adversarial-review` and `usadebusk-fieldpm`.
3. Normalize all skill frontmatter to `name` and `description` only.
4. Add `agents/openai.yaml` for each skill.
5. Rewrite Claude-specific wording.
6. Validate each skill.
7. Copy or symlink the final skills into `C:\Users\Jwuts\.agents\skills`.

### Phase 2: Vault guidance

1. Create a vault-level `AGENTS.md`.
2. Put OneDrive safety, finalized-document confirmation gates, and vault source-of-truth rules there.
3. Keep domain facts in skills rather than repeating them in the vault guidance.

### Phase 3: Optional plugin packaging

1. Package the skills as a `usadebusk-codex` plugin.
2. Include only skills and UI metadata at first.
3. Add MCP/app integration only if a real external system needs live access.
4. Use the plugin as the distribution mechanism for future machines.

## What Not To Do

- Do not paste all of `CLAUDE.md` into global `AGENTS.md`.
- Do not put business rates or SOP details in global instructions.
- Do not rely on Claude slash commands as the primary interface.
- Do not install MarkItDown or any new dependency without explicit approval.
- Do not let `adversarial-review` trigger implicitly on ordinary reviews.
- Do not treat the old audit snapshot as active instructions.

## Open Questions Before Implementation

1. Should the first install be user-scoped in `~/.agents/skills`, or should the repo become a plugin immediately?
2. Should the Obsidian vault get a new `AGENTS.md`, or should we keep vault rules only in skills for now?
3. Should default estimating rates remain inside `usadebusk-estimating/SKILL.md`, or move to a reference file to reduce loaded context?
4. Should `adversarial-review` be migrated now, or deferred until the USADeBusk domain skills are working?
