#!/usr/bin/env python3
"""Validate module registry and sync manifest shape without external dependencies."""
from pathlib import Path
import json, sys

errors = []

try:
    registry = json.loads(Path('module_registry.json').read_text(encoding='utf-8'))
except Exception as exc:
    print(f'Cannot read module_registry.json: {exc}')
    sys.exit(1)

seen = set()
for module in registry.get('modules', []):
    mid = module.get('id')
    if not mid:
        errors.append('module missing id')
        continue
    if mid in seen:
        errors.append(f'duplicate module id: {mid}')
    seen.add(mid)
    if not Path('modules', mid, 'module.yml').exists():
        errors.append(f'module {mid} missing module.yml')
    for field in ['name', 'purpose', 'owner', 'status']:
        if not module.get(field):
            errors.append(f'module {mid} missing {field}')

try:
    manifest = json.loads(Path('sync_manifest.json').read_text(encoding='utf-8'))
except Exception as exc:
    print(f'Cannot read sync_manifest.json: {exc}')
    sys.exit(1)

sync_ids = set()
for entry in manifest.get('entries', []):
    sid = entry.get('id')
    if not sid:
        errors.append('sync entry missing id')
        continue
    if sid in sync_ids:
        errors.append(f'duplicate sync entry id: {sid}')
    sync_ids.add(sid)
    for field in ['source_type', 'source_uri', 'source_id', 'source_title', 'target_path', 'owner', 'reviewer', 'content_policy']:
        if field not in entry:
            errors.append(f'sync entry {sid} missing {field}')
    target = entry.get('target_path', '')
    if target and not target.startswith('modules/'):
        errors.append(f'sync entry {sid} target must be under modules/: {target}')

if errors:
    print('Registry validation failed:')
    for e in errors:
        print(f'- {e}')
    sys.exit(1)

print('Registry validation passed.')
