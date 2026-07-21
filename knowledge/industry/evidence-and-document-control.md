---
type: knowledge
status: active
authority: public-concept
confidence: high
review_after: 2027-01-01
---

# Evidence and Document Control

Reliable agent work separates four things:

1. **Evidence** — an observed file, test result, source link, or connector response.
2. **Interpretation** — what the evidence appears to mean, including uncertainty.
3. **Proposal** — a bounded change that another person or agent can review.
4. **Decision** — an approved action with an owner and acceptance check.

When sources disagree, preserve both claims, identify their authority, and open
a contradiction or review record. Do not average conflicting evidence into a
new fact.

Useful document-control fields are `source`, `authority`, `confidence`,
`review_after`, `status`, and `related`. These are workflow metadata, not proof
by themselves; the underlying source still matters.
