# Codex Workbench Operating Model

The workbench is a public-safe operating system for Codex work. It combines
durable repository guidance, reusable skills, bounded improvement loops,
sanitized knowledge patterns, and deterministic checks.

## Ownership

| Layer | Owner | Purpose |
|---|---|---|
| `AGENTS.md` | Repository | Short, durable safety and completion rules. |
| `.agents/skills/` | Codex | Reusable task workflows and loop instructions. |
| `knowledge/` | Workbench | Sanitized concepts and synthetic examples only. |
| `workbench/` | Workbench | Inbox, proposals, reviews, research records, and local state boundary. |
| `contracts/` | Validator | Machine-readable task, evidence, proposal, and run-result contracts. |
| `scripts/` | Deterministic tooling | Read-only previews and fixture-backed validation. |
| GitHub | Collaboration surface | Optional issues, branches, and pull requests; never hidden canonical state. |

## Operating principles

1. Inspect authoritative inputs before acting.
2. Separate evidence, interpretation, proposal, and approved change.
3. One loop run selects at most one item unless its contract explicitly says otherwise.
4. A clean no-op is success when no eligible item exists.
5. Agentic writes happen in a worktree or reviewable branch; `main` is protected.
6. Deterministic checks enforce shape and safety; the model supplies judgment.
7. Public artifacts contain no private paths, credentials, customer records, or proprietary source material.

## Artifact lifecycle

`inbox -> proposal/research -> review -> approved change -> validation evidence`

The transition from proposal to approved change is explicit. A loop may create
an artifact or branch proposal, but it must not silently promote untrusted
content or decide a human-gated change.
