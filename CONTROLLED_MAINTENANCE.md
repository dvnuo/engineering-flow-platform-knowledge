---
title: Controlled Maintenance Policy
maintenance_action: policy_seed
updated_at_utc: "2026-06-02T00:00:00Z"
source:
  type: initial_design
  uri: "internal-design-session"
  title: "Controlled repository maintenance policy"
  observed_at_utc: "2026-06-02T00:00:00Z"
  retrieved_at_utc: "2026-06-02T00:00:00Z"
  version: "v1"
status: published
source_of_truth: true
---

# Controlled Maintenance Policy

This repository is not an open-ended wiki. It is a governed maintenance system. Humans and agents may update it only through approved maintenance actions.

## Allowed maintenance actions

### 1. `add_module`

Use when a human requests a new module, for example:

> 我期望新增一个模块 `Observability`，用于统一服务监控、日志、告警和 SLO 运营。

The agent may:

- create `modules/<module-id>/` from the module template;
- create `module.yml`, `README.md`, `charter.md`, and empty standard subfolders;
- update `module_registry.json`;
- append a line to `maintenance/source-log.jsonl`;
- open a PR.

The agent must not:

- invent standards for the new module;
- fill detailed content without source material;
- change unrelated modules;
- mark the module as mature or approved.

### 2. `source_sync`

Use when an approved source changes, for example:

> Confluence 页面 `ABC123` 有更新，请同步到 `modules/05-aws-compliance/source-mirrors/aws-control-evidence.md`。

The agent or scheduled workflow may:

- fetch the approved source;
- update the configured target file;
- include source metadata and timestamps;
- update `maintenance/source-log.jsonl`;
- open a PR.

The agent must not:

- sync unapproved sources;
- infer missing policy beyond the source;
- silently overwrite human-owned interpretation sections;
- change unrelated files;
- remove provenance.

## Required provenance fields

Every maintained Markdown file under `modules/` must include YAML front matter with these fields:

```yaml
maintenance_action: add_module|source_sync|manual_seed
updated_at_utc: "YYYY-MM-DDTHH:MM:SSZ"
source:
  type: user_request|confluence|github_issue|manual_seed|other
  uri: "..."
  title: "..."
  observed_at_utc: "YYYY-MM-DDTHH:MM:SSZ"
  retrieved_at_utc: "YYYY-MM-DDTHH:MM:SSZ"
  version: "..."
status: draft|published|deprecated
source_of_truth: true|false
```

## PR requirement

Every PR must state:

- maintenance action;
- source URI or source identifier;
- source version;
- source observed/retrieved time;
- repository update time;
- target files;
- human reviewer.

## Human approval boundary

Agents can prepare changes. Humans approve changes.

The following decisions are human-only:

- release approval;
- security exception approval;
- compliance sign-off;
- cost ownership decision;
- platform onboarding approval;
- risk acceptance;
- declaring a module standard as mandatory.
