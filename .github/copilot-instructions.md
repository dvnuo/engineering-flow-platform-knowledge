# Repository Copilot Instructions

This repository is a controlled maintenance repository.

Before proposing edits or making edits, read and follow `AGENTS.md`. `AGENTS.md` is the canonical source of truth for all repository agent behavior.

This file exists so GitHub Copilot, Copilot Chat, Copilot Agent mode, Copilot CLI, and Copilot coding agent receive the same guardrails at the repository entrypoint.

## Mandatory operating mode

Agents are constrained maintainers.

For normal content maintenance, agents may perform only one of these actions per PR:

1. `add_module`
2. `source_sync`

Do not perform broad repository cleanup, reorganization, rewriting, summarization, refactoring, or expansion outside one approved action.

Repository policy/configuration updates are exceptional. They are allowed only when a repository steward explicitly asks for them. They may only touch the named policy, instruction, validation, ownership, or tool-configuration files.

## Repository language

All agent-created or agent-updated repository content must be written in English.

If the approved source content is not in English, stop and require a human-approved English source or translation before updating repository files.

## Required reading before editing

Before editing, read:

- `AGENTS.md`
- `CONTROLLED_MAINTENANCE.md`
- `MODULE_SYSTEM.md`
- `SOURCE_SYNC.md`
- `module_registry.json`
- `sync_manifest.json`
- The target module `module.yml`, when a module is involved

For policy/configuration updates, also read:

- `.github/copilot-instructions.md`
- `.github/instructions/*.instructions.md`, if present
- `opencode.json`, if present
- `.vscode/settings.json`, if present
- `.github/workflows/validate-maintenance.yml`
- `CODEOWNERS`

## Allowed action: add_module

Only perform this action when the human explicitly asks to add a module and provides both a module name and purpose.

Required behavior:

- Validate the module name and purpose.
- Generate a safe module ID.
- Create the standard module folder from `templates/module/`.
- Fill `module.yml`, `README.md`, and `charter.md` with provenance.
- Update `module_registry.json`.
- Append `maintenance/source-log.jsonl`.
- Open or prepare a PR.

Do not create detailed standards, playbooks, operating procedures, or policies for the new module unless explicit approved source content is provided.

## Allowed action: source_sync

Only perform this action when the human explicitly asks to sync an approved source into a governed target.

Required behavior:

- Verify the source is approved in `sync_manifest.json`, or create a draft sync entry requiring owner approval.
- Fetch or use only the provided or approved source content.
- Update only the configured target path.
- Preserve and update provenance.
- Append `maintenance/source-log.jsonl`.
- Open or prepare a PR.

Do not silently sync content into arbitrary files.

## Provenance is mandatory

Every agent-created or agent-updated governed content file must include provenance with:

- Repository update time
- Source type
- Source URI or source identifier
- Source title or human request summary
- Source observed or retrieved time
- Source version when available
- Maintenance action
- Status
- Source-of-truth marker when applicable

Missing provenance is a blocking error.

## Forbidden behavior

Agents must not:

- Invent domain standards, compliance requirements, security rules, cost policies, release rules, or risk rules.
- Update unrelated modules.
- Mark draft content as published.
- Remove or weaken source metadata.
- Process customer data, secrets, credentials, account numbers, regulated customer records, raw production logs, or production incident data.
- Make final compliance, security, release, cost, or risk decisions.
- Approve their own PRs.
- Push directly to protected branches.
- Continue making unrelated edits after validation passes.

## Definition of done

A valid agent PR must have:

- Exactly one approved maintenance action or one explicitly requested repository policy/configuration update.
- Source and timestamp in every changed governed content file.
- A `maintenance/source-log.jsonl` entry when repository maintenance is performed.
- Module owner review requested when module content is touched.
- No unrelated changes.
- Passing provenance and registry validation.
- Valid JSON for every changed JSON file.
