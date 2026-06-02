---
title: Source Sync System
maintenance_action: policy_seed
updated_at_utc: "2026-06-02T00:00:00Z"
source:
  type: initial_design
  uri: "internal-design-session"
  title: "Source synchronization design"
  observed_at_utc: "2026-06-02T00:00:00Z"
  retrieved_at_utc: "2026-06-02T00:00:00Z"
  version: "v1"
status: published
source_of_truth: true
---

# Source Sync System

Source sync is the controlled mechanism for copying approved external knowledge into this repository.

## Supported initial source type

The initial supported source type is Confluence.

A sync entry is configured in `sync_manifest.json`.

## Sync manifest entry

```json
{
  "id": "aws-control-evidence",
  "enabled": true,
  "source_type": "confluence",
  "source_uri": "https://your-company.atlassian.net/wiki/spaces/ABC/pages/123456789/Page+Title",
  "source_id": "123456789",
  "source_title": "AWS Control Evidence Standard",
  "target_path": "modules/05-aws-compliance/source-mirrors/aws-control-evidence.md",
  "owner": "aws-compliance-owner",
  "reviewer": "security-compliance-reviewer",
  "schedule": "daily",
  "content_policy": "mirror_only"
}
```

## Mirror-only rule

The first implementation should use `mirror_only`.

That means the synced file should represent the source page only. It should not add AI-generated interpretation unless the interpretation is placed in a clearly separated `Team interpretation` section and reviewed by a human.

## Required sync metadata

Each synced target must record:

- source type;
- source URI;
- source title;
- source page ID;
- source version;
- source last updated time when available;
- source retrieved time;
- repository updated time.

## Scheduled sync

The workflow `.github/workflows/sync-confluence.yml` is a skeleton for scheduled sync. The schedule should be adjusted by the repository owner.

## Failure handling

If a source cannot be fetched, the workflow should not modify target documents. It should create or update a sync failure issue with:

- source ID;
- source URI;
- attempted time;
- failure category;
- owner;
- next action.
