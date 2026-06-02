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
| “新增一个模块 X，用于 Y” | `add_module` | New module folder, registry update, PR |
| “Confluence 页面 X 有更新，同步到 Y” | `source_sync` | Target mirror update, source log, PR |
| “帮我整理一下这个主题” | Not allowed directly | Human must reframe into one approved action |
| “帮我重构整个目录” | Not allowed | Human governance review required |
| “帮我写一个新标准” | Not allowed unless source-backed | Requires source sync or human-authored draft |
