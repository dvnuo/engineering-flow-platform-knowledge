# Sync Source Update Prompt

You are performing the controlled maintenance action `source_sync`.

Read:
- `CONTROLLED_MAINTENANCE.md`
- `AGENTS.md`
- `SOURCE_SYNC.md`
- `sync_manifest.json`

Required input:
- source type
- source URI
- source ID
- source title
- source version if available
- source observed/retrieved time UTC
- target path
- owner
- reviewer

Do:
1. Confirm source is in `sync_manifest.json` or add a draft manifest entry.
2. Update only the target path.
3. Preserve provenance.
4. Append `maintenance/source-log.jsonl`.
5. Prepare a PR.

Do not update unrelated files. Do not invent interpretation beyond the source.
