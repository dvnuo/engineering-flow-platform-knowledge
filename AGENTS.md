---
title: Agent Operating Rules
maintenance_action: policy_update
updated_at_utc: "2026-06-03T01:59:25Z"
source:
  type: user_request
  uri: "conversation://current-thread"
  title: "Constrain GitHub Copilot and opencode agents with shared repository rules"
  observed_at_utc: "2026-06-03T01:59:25Z"
  retrieved_at_utc: "2026-06-03T01:59:25Z"
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

This file is the canonical source of truth for repository-level agent behavior.

This repository is a governed knowledge repository, not a general-purpose wiki, not a documentation sandbox, and not an application codebase.

Agents are constrained maintainers. They must preserve governance, provenance, ownership, and review boundaries.

## Tool compatibility

This policy is intended to guide multiple agent systems:

- GitHub Copilot in VS Code and GitHub uses `.github/copilot-instructions.md`, `.github/instructions/*.instructions.md`, and `AGENTS.md`.
- opencode reads this root `AGENTS.md` natively.
- opencode also loads additional shared instruction files through `opencode.json`.
- If tool-specific instruction files conflict with this file, this file wins.

Do not create tool-specific instructions that weaken or bypass this file.

## Normal allowed content maintenance actions

For normal repository content maintenance, agents may perform only these two actions:

1. `add_module`
2. `source_sync`

Any other action is out of scope unless a repository steward explicitly requests a repository policy/configuration update.

A repository policy/configuration update may only touch the explicitly named policy, agent-instruction, validation, ownership, or tool-configuration files in the human request. It must not touch module content unless the human request explicitly names that module content path.

## Repository language

All agent-created or agent-updated repository content must be written in English.

If approved source content is not in English, the agent must stop and require a human-approved English source or translation before updating repository files.

## Required reading before editing

Before editing, read:

1. `AGENTS.md`
2. `CONTROLLED_MAINTENANCE.md`
3. `MODULE_SYSTEM.md`
4. `SOURCE_SYNC.md`
5. `module_registry.json`
6. `sync_manifest.json`
7. The target module `module.yml`, when a module is involved.

For repository policy/configuration updates, also read:

1. `.github/copilot-instructions.md`
2. `.github/instructions/*.instructions.md`, if present
3. `opencode.json`, if present
4. `.vscode/settings.json`, if present
5. `.github/workflows/validate-maintenance.yml`
6. `CODEOWNERS`

## Action 1: add_module

Trigger examples:

```text
Add a module named Observability for unified service monitoring, logging, alerting, and SLO operations.
Add a module named Developer Experience for onboarding, tooling, and engineering productivity.
```

Required agent steps:

1. Validate the module name and purpose.
2. Generate a safe module ID.
3. Create the standard module folder from `templates/module/`.
4. Fill `module.yml`, `README.md`, and `charter.md` with provenance.
5. Update `module_registry.json`.
6. Append `maintenance/source-log.jsonl`.
7. Open or prepare a PR.

Agents must not create detailed standards, playbooks, procedures, or policies for the new module unless explicit approved source content is provided.

## Action 2: source_sync

Trigger examples:

```text
Confluence page 123456789 has been updated; sync it to modules/05-aws-compliance/source-mirrors/aws-control-evidence.md.
The Confluence page https://... has been updated; sync it to modules/07-service-host-platform/source-mirrors/onboarding.md.
```

Required agent steps:

1. Verify the source is approved in `sync_manifest.json`, or create a draft sync entry requiring owner approval.
2. Fetch or use only the provided or approved source content.
3. Update only the configured target path.
4. Preserve and update provenance.
5. Append `maintenance/source-log.jsonl`.
6. Open or prepare a PR.

Agents must not silently sync content into arbitrary files.

## Required provenance

Every agent-created or agent-updated governed content file must include time and source.

Required provenance fields are:

* Repository update time
* Source type
* Source URI or source identifier
* Source title or human request summary
* Source observed or retrieved time
* Source version when available
* Maintenance action
* Status
* Source-of-truth marker when applicable

Missing provenance is a blocking error.

## Forbidden behavior

Agents must not:

* Perform broad repository cleanup, reorganization, restructuring, or style-only rewrites.
* Invent domain standards, compliance requirements, security requirements, release requirements, cost policies, or risk rules.
* Update unrelated modules.
* Change module status from draft to published unless explicitly approved by a human owner.
* Remove or weaken source metadata.
* Process customer data, secrets, credentials, account numbers, regulated customer records, raw production logs, or production incident data.
* Make final compliance, security, release, cost, or risk decisions.
* Approve their own PRs.
* Push directly to protected branches.
* Hide validation failures.
* Continue changing files in a loop after the same validation error appears twice.

## Definition of done

A valid agent PR must have:

* Exactly one approved maintenance action or one explicitly requested repository policy/configuration update.
* Source and timestamp in every changed governed content file.
* A `maintenance/source-log.jsonl` entry when repository maintenance is performed.
* Module owner review requested when module content is touched.
* No unrelated changes.
* Passing provenance validation.
* Passing registry validation.
* Valid JSON for every changed JSON file.
* No secrets, credentials, customer data, or raw production logs.
