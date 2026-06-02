---
title: Security Policy
maintenance_action: policy_seed
updated_at_utc: "2026-06-02T00:00:00Z"
source:
  type: initial_design
  uri: "internal-design-session"
  title: "Security policy for repository maintenance"
  observed_at_utc: "2026-06-02T00:00:00Z"
  retrieved_at_utc: "2026-06-02T00:00:00Z"
  version: "v1"
status: published
source_of_truth: true
---

# Security Policy

Do not store customer data, account data, secrets, credentials, production tokens, production logs, or regulated customer records in this repository.

For Confluence sync, only approved source pages may be mirrored. Source pages must be classified as safe for this repository before they are added to `sync_manifest.json`.

If sensitive information is found:

1. Stop the agent task.
2. Do not commit the sensitive content.
3. Notify the repository steward and security owner.
4. Follow the organization incident process.
