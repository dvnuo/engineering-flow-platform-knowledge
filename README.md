# Engineering Flow & Platform Knowledge

A governed knowledge repository for engineering flows, platform practices, and controlled source-based updates.

This repository is the controlled knowledge and operations hub for the team. It is designed for a small enablement team that supports larger engineering, platform, AI, release, cyber, AWS compliance, AWS cost, and service-hosting workstreams.

The repository intentionally limits AI/agent maintenance to **two approved actions**:

1. **Add Module** — create a new governed module when a human says: “I expect to add a module `xxxx`, used for `xxxx`.”
2. **Sync Source Update** — update a target document from an approved external source, for example: “Confluence page `xxx` has updated; sync it into `xxxx`.”

No agent should freely reorganize, invent, rewrite, or expand repository content outside these two actions.

## Current top-level modules

| Module | Purpose |
|---|---|
| `01-ai-adoption` | AI adoption, Copilot usage, agent usage, AI champion enablement |
| `02-standard-cicd` | Standard CI/CD workflows, pipeline readiness, workflow evidence |
| `03-release-quality` | Release readiness, rollback, post-release quality, change evidence |
| `04-cyberflows` | Security operational flows: vulnerability, exception, escalation, evidence |
| `05-aws-compliance` | AWS control evidence, workload compliance, audit readiness |
| `06-aws-cost-finops` | Cost ownership, tagging, allocation, anomaly review, optimization |
| `07-service-host-platform` | Service onboarding, hosting patterns, platform readiness, runtime support |

## Required provenance

Every maintained content item must include:

- repository update time;
- source type;
- source URI or source identifier;
- source title or human request summary;
- source observed/retrieved time;
- source version when available;
- maintenance action.

Repository timestamps should use UTC ISO-8601 format unless your organization requires another standard.

## Start here

- Human usage: `docs/00-start-here/01-human-guide.md`
- Agent usage: `AGENTS.md`
- Maintenance policy: `CONTROLLED_MAINTENANCE.md`
- Module system: `MODULE_SYSTEM.md`
- Source sync: `SOURCE_SYNC.md`
- Current modules: `module_registry.json`
- Scheduled source map: `sync_manifest.json`
