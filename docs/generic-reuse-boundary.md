# Generic and Domain Reuse Boundary

This repository is the public-safe home for reusable Codex workbench contracts,
validation, evidence handling, review gates, and bounded workflow patterns. It
does not contain private or customer-specific operating knowledge.

## What belongs in the generic workbench

Keep patterns here when they are domain-neutral and useful across repositories,
including:

- bounded execution with declared input and permitted write scopes;
- expected-artifact enforcement, no-op detection, and out-of-scope change detection;
- deterministic, schema-backed validation and synthetic fixtures;
- evidence provenance, source and revision hierarchy, contradiction reporting,
  confidence, and unresolved-gap handling;
- proof and review packets, task packets, and handoffs;
- telemetry receipts that are not treated as authoritative state; and
- human-gated promotion into trusted knowledge.

The executor and loop write path remain experimental. Their contracts and
acceptance checks are reusable, but they do not claim unattended or live Codex
execution maturity.

## What belongs in domain repositories

Domain repositories own domain terminology, fields and schemas, extraction
rules, procedures and SOPs, source documents, customer or proprietary data,
company-specific estimating guidance, and domain-specific safety safeguards.
USADeBusk and fired-heater content therefore remain outside this repository.

## Criteria for promoting a pattern

A candidate pattern should be promoted only when it is:

1. domain-neutral and public-safe;
2. expressible as a stable contract, deterministic check, or bounded workflow;
3. free of hidden assumptions about a particular source, industry, or repository;
4. supported by tests and documentation that describe its limits; and
5. normally proven in at least two materially different use cases.

The two-use-case rule is evidence of reuse, not permission to weaken a domain
control. If generalization would make a domain safeguard less precise, keep the
specialized rule in the domain repository.

## How domain repositories consume the generic layer

Domain repositories should consume the generic contracts and documented
semantics through explicit adapters, fixtures, or pinned revisions. They should
not copy the workbench implementation, generic skills, or validator scripts
into each domain repository. A domain adapter may add stricter validation,
additional evidence requirements, or domain-specific review gates.

Generic abstractions must never weaken domain-specific safeguards. The stricter
applicable domain rule remains authoritative, and promotion into trusted
knowledge remains human-gated.

All contributions to this repository must remain sanitized and public-safe:
never add credentials, private source material, customer information, or local
Codex state.
