---
title: Agent Operating Rules
maintenance_action: policy_update
updated_at_utc: "2026-06-02T07:42:21Z"
source:
  type: user_request
  uri: "conversation://current-thread"
  title: "Require repository edits to be written in English"
  observed_at_utc: "2026-06-02T07:42:21Z"
  retrieved_at_utc: "2026-06-02T07:42:21Z"
  version: "n/a"
previous_source:
  type: initial_design
  uri: "internal-design-session"
  title: "Agent constrained maintenance rules"
  observed_at_utc: "2026-06-02T00:00:00Z"
  retrieved_at_utc: "2026-06-02T00:00:00Z"
  version: "v1"
status: published
source_of_truth: true
---

# Agent Operating Rules

Agents are not general editors of this repository. Agents are constrained maintainers.

## Repository language

All agent-created or agent-updated repository content must be written in English. If approved source content is not in English, the agent must stop and require a human-approved English source or translation before updating repository files.

## Allowed actions

Agents may perform only these two actions:

1. `add_module`
2. `source_sync`

## Action 1: add_module

Trigger examples:

```text
Add a module named Observability for unified service monitoring, logging, alerting, and SLO operations.
Add a module named Developer Experience for onboarding, tooling, and engineering productivity.
```

Agent steps:

1. Validate module name and purpose.
2. Generate a safe module ID.
3. Create the standard module folder from `templates/module/`.
4. Fill `module.yml`, `README.md`, and `charter.md` with provenance.
5. Update `module_registry.json`.
6. Append `maintenance/source-log.jsonl`.
7. Open a PR.

Agent must not create detailed standards, playbooks, or policies for the new module unless explicit approved source content is provided.

## Action 2: source_sync

Trigger examples:

```text
Confluence page 123456789 has been updated; sync it to modules/05-aws-compliance/source-mirrors/aws-control-evidence.md.
The Confluence page https://... has been updated; sync it to modules/07-service-host-platform/source-mirrors/onboarding.md.
```

Agent steps:

1. Verify the source is approved in `sync_manifest.json`, or create a draft sync entry requiring owner approval.
2. Fetch or use the provided source content.
3. Update only the configured target path.
4. Preserve and update provenance.
5. Append `maintenance/source-log.jsonl`.
6. Open a PR.

Agent must not silently sync content into arbitrary files.

## Required provenance

Every agent-created or agent-updated file must include time and source. Missing provenance is a blocking error.

## Forbidden behavior

Agents must not:

- perform broad repository reorganization;
- invent domain standards;
- update unrelated modules;
- approve their own PRs;
- mark draft content as published;
- remove source metadata;
- process customer data, secrets, credentials, production logs, or regulated customer records;
- make final compliance, security, release, or cost decisions.

## Before editing

Read:

1. `CONTROLLED_MAINTENANCE.md`
2. `MODULE_SYSTEM.md`
3. `SOURCE_SYNC.md`
4. `module_registry.json`
5. `sync_manifest.json`
6. the target module `module.yml`

## Definition of done

A valid agent PR must have:

- exactly one maintenance action;
- source and timestamp in every changed content file;
- source-log entry;
- module owner review requested;
- no unrelated changes;
- passing provenance validation.
