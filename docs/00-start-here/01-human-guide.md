---
title: Human Guide
maintenance_action: policy_seed
updated_at_utc: "2026-06-02T00:00:00Z"
source:
  type: initial_design
  uri: "internal-design-session"
  title: "Human usage guide"
  observed_at_utc: "2026-06-02T00:00:00Z"
  retrieved_at_utc: "2026-06-02T00:00:00Z"
  version: "v1"
status: published
source_of_truth: true
---

# Human Guide

Use this repository for controlled maintenance only.

## To add a module

Open a `New Module Request` issue or tell the agent:

```text
我期望新增一个模块 Observability，用于统一服务监控、日志、告警和 SLO 运营。
来源：GitHub Issue #123
时间：2026-06-02T16:00:00Z
```

Required values:

- module name;
- purpose;
- source;
- timestamp;
- owner or temporary owner;
- reviewer or temporary reviewer.

## To sync Confluence content

Open a `Source Sync Request` issue or tell the agent:

```text
Confluence 页面 123456789 有更新，请同步到 modules/05-aws-compliance/source-mirrors/aws-control-evidence.md。
来源：https://your-company.atlassian.net/wiki/spaces/ABC/pages/123456789
时间：2026-06-02T16:00:00Z
```

The source must be approved in `sync_manifest.json`, or the PR must add a draft manifest entry for human approval.

## If your request is not one of these

Do not ask the agent to process it directly. Put it in `maintenance/unclassified-requests.md` for human triage.
