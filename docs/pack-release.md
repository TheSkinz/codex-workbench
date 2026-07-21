# Knowledge-Pack Release Protocol

## Purpose

A skill or reference pack is a curated, versioned export of canonical knowledge for a specific runtime. It is not a live mirror of a vault and it must not invent a second source of truth.

This protocol prevents drift between a canonical knowledge system and Codex/ChatGPT/Claude adapters.

## Release packet

Every release records:

- canonical source paths or documents;
- release date and semantic version;
- topics added, changed, or deliberately excluded;
- runtime target;
- source sensitivity classification;
- representative tasks used to test it;
- known gaps and expiry/review trigger.

## Rules

1. Export only the minimum material the runtime needs.
2. Never include customer data, secrets, credentials, proprietary rates, or raw private source documents in a public adapter repository.
3. Preserve source authority: a pack may summarize or route, but it cannot silently override canonical policy.
4. When a canonical rule changes, release a new pack; do not patch an old pack without updating its manifest.
5. If a pack cannot be tied to source and test evidence, mark it untrusted and do not use it for customer-facing or irreversible work.

## Manifest template

```yaml
pack: <name>
version: 0.1.0
released: YYYY-MM-DD
runtime: codex | chatgpt | claude
source_classification: sanitized | internal | restricted
canonical_sources:
  - path: <canonical source path>
    revision: <commit or content hash>
included_topics:
  - <topic>
excluded_topics:
  - customer-specific data
validation:
  - task: <representative task>
    expected: <observable success condition>
known_gaps:
  - <gap>
review_trigger: <date, source change, or failed task>
```

## Promotion rule

Promote a workflow into a pack only after it succeeds on at least three real uses and has a defined verification method. One-off prompts remain task packets.
