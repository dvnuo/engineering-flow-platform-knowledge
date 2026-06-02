---
title: Module System
maintenance_action: policy_seed
updated_at_utc: "2026-06-02T00:00:00Z"
source:
  type: initial_design
  uri: "internal-design-session"
  title: "Modular repository system"
  observed_at_utc: "2026-06-02T00:00:00Z"
  retrieved_at_utc: "2026-06-02T00:00:00Z"
  version: "v1"
status: published
source_of_truth: true
---

# Module System

Modules are stable containers for team capability areas. Each module has the same structure so new topics can be added without reorganizing the repository.

## Module creation rule

New modules can only be created through `add_module`.

A valid request must contain:

```text
module name
module purpose
request source
request timestamp
owner or temporary owner
reviewer or temporary reviewer
```

If any required value is missing, the agent should create a draft PR with explicit `TODO` fields or ask for the missing details, depending on the operating mode.

## Standard module structure

```text
modules/<module-id>/
  module.yml
  README.md
  charter.md
  standards/
  playbooks/
  checklists/
  runbooks/
  metrics/
  decisions/
  source-mirrors/
  faq.md
  backlog.md
```

## Content maturity

| Status | Meaning |
|---|---|
| `draft` | Not yet approved. Can be discussed but should not be treated as source of truth. |
| `published` | Approved by module owner and reviewer. Can be used as source of truth. |
| `deprecated` | Retained for history only. Should not be used for new work. |

## Source of truth

A document can be `source_of_truth: true` only after human review.

For synced sources, the mirror document may be source of truth only for representing the source page. Any team interpretation must be in a separate approved document.
