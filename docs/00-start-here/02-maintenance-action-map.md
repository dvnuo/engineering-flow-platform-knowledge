---
title: Maintenance Action Map
maintenance_action: policy_seed
updated_at_utc: "2026-06-02T00:00:00Z"
source:
  type: initial_design
  uri: "internal-design-session"
  title: "Map of allowed maintenance actions"
  observed_at_utc: "2026-06-02T00:00:00Z"
  retrieved_at_utc: "2026-06-02T00:00:00Z"
  version: "v1"
status: published
source_of_truth: true
---

# Maintenance Action Map

| Input pattern | Action | Output |
|---|---|---|
| “Add a module named X for Y” | `add_module` | New module folder, registry update, PR |
| “Confluence page X has been updated; sync it to Y” | `source_sync` | Target mirror update, source log, PR |
| “Help me organize this topic” | Not allowed directly | Human must reframe into one approved action |
| “Help me refactor the whole directory” | Not allowed | Human governance review required |
| “Help me write a new standard” | Not allowed unless source-backed | Requires source sync or human-authored draft |
