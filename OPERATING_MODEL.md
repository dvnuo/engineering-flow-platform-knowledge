---
title: Operating Model
maintenance_action: policy_seed
updated_at_utc: "2026-06-02T00:00:00Z"
source:
  type: initial_design
  uri: "internal-design-session"
  title: "Operating model for constrained maintenance"
  observed_at_utc: "2026-06-02T00:00:00Z"
  retrieved_at_utc: "2026-06-02T00:00:00Z"
  version: "v1"
status: published
source_of_truth: true
---

# Operating Model

The repository runs on a constrained maintenance model.

## Roles

| Role | Responsibilities |
|---|---|
| Requester | Requests a new module or reports a source update. Must provide source and purpose. |
| Agent | Creates structured draft changes only for approved maintenance actions. |
| Module Owner | Reviews changes for the module and approves module-level accuracy. |
| Compliance / Security Reviewer | Reviews controlled domains such as cyberflows, AWS compliance, and sensitive operational flows. |
| Repository Steward | Maintains module registry, sync manifest, templates, and workflow health. |

## Daily operating rhythm

Daily input is not free-form writing. Daily input is triaged into one of two actions:

1. `add_module`
2. `source_sync`

If an input does not match either action, it goes to `maintenance/unclassified-requests.md` and requires a human to reframe it.

## Weekly operating rhythm

Weekly review checks:

- open module creation PRs;
- failed source syncs;
- source files with stale timestamps;
- PRs missing provenance;
- modules without owners;
- source sync targets without reviewers.

## Monthly operating rhythm

Monthly governance review checks:

- whether modules still reflect actual team concerns;
- whether source sync entries remain valid;
- whether stale mirror documents should be archived;
- whether additional module owners are needed;
- whether any module should move from draft to published.
