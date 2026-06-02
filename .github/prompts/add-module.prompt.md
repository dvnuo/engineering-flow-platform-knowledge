# Add Module Prompt

You are performing the controlled maintenance action `add_module`.

Read:
- `CONTROLLED_MAINTENANCE.md`
- `AGENTS.md`
- `MODULE_SYSTEM.md`
- `module_registry.json`
- `templates/module/`

Required input:
- module name
- module purpose
- source URI or request identifier
- source observed time UTC
- owner
- reviewer

Do:
1. Generate a safe module ID.
2. Create the standard module folder.
3. Fill required provenance.
4. Update `module_registry.json`.
5. Append `maintenance/source-log.jsonl`.
6. Prepare a PR.

Do not create detailed standards or playbooks unless source-backed content is supplied.
