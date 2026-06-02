#!/usr/bin/env python3
"""Create a governed module from the module template.

Example:
python scripts/create_module.py \
  --name "Observability" \
  --purpose "统一服务监控、日志、告警和 SLO 运营" \
  --source-uri "https://github.com/org/repo/issues/123" \
  --source-title "New module request: Observability" \
  --observed-at-utc "2026-06-02T16:00:00Z" \
  --owner "observability-owner" \
  --reviewer "sre-reviewer"
"""
from pathlib import Path
import argparse, datetime, json, re

ROOT = Path(__file__).resolve().parents[1]

def now_utc():
    return datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).strftime('%Y-%m-%dT%H:%M:%SZ')

def slugify(name: str) -> str:
    s = name.strip().lower()
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    return s or 'new-module'

def replace_tokens(text: str, values: dict) -> str:
    for k, v in values.items():
        text = text.replace(k, v)
    return text

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--name', required=True)
    ap.add_argument('--purpose', required=True)
    ap.add_argument('--source-uri', required=True)
    ap.add_argument('--source-title', required=True)
    ap.add_argument('--observed-at-utc', required=True)
    ap.add_argument('--owner', required=True)
    ap.add_argument('--reviewer', required=True)
    ap.add_argument('--id', default=None)
    args = ap.parse_args()

    registry_path = ROOT / 'module_registry.json'
    registry = json.loads(registry_path.read_text(encoding='utf-8'))
    existing = {m['id'] for m in registry.get('modules', [])}
    base_id = args.id or slugify(args.name)
    module_id = base_id
    if module_id in existing:
        raise SystemExit(f'Module already exists: {module_id}')

    updated_at = now_utc()
    values = {
        '<module-id>': module_id,
        '<module-name>': args.name,
        '<module-purpose>': args.purpose,
        '<owner>': args.owner,
        '<reviewer>': args.reviewer,
        '<created-at-utc>': updated_at,
        '<updated-at-utc>': updated_at,
        '<source-uri>': args.source_uri,
        '<source-title>': args.source_title,
        '<observed-at-utc>': args.observed_at_utc,
        '<retrieved-at-utc>': updated_at,
    }

    mod_dir = ROOT / 'modules' / module_id
    mod_dir.mkdir(parents=True)
    for sub in ['standards','playbooks','checklists','runbooks','metrics','decisions','source-mirrors']:
        (mod_dir/sub).mkdir(parents=True)
        (mod_dir/sub/'.gitkeep').write_text('', encoding='utf-8')

    for rel in ['module.yml', 'README.md', 'charter.md', 'faq.md', 'backlog.md']:
        template = (ROOT / 'templates' / 'module' / rel).read_text(encoding='utf-8')
        (mod_dir / rel).write_text(replace_tokens(template, values), encoding='utf-8')

    registry['updated_at_utc'] = updated_at
    registry.setdefault('modules', []).append({
        'id': module_id,
        'name': args.name,
        'purpose': args.purpose,
        'owner': args.owner,
        'status': 'draft'
    })
    registry_path.write_text(json.dumps(registry, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

    log = {
        'timestamp_utc': updated_at,
        'maintenance_action': 'add_module',
        'source': {
            'type': 'user_request',
            'uri': args.source_uri,
            'title': args.source_title,
            'observed_at_utc': args.observed_at_utc,
            'retrieved_at_utc': updated_at,
            'version': 'n/a'
        },
        'target': f'modules/{module_id}',
        'owner': args.owner,
        'reviewer': args.reviewer
    }
    with (ROOT/'maintenance/source-log.jsonl').open('a', encoding='utf-8') as f:
        f.write(json.dumps(log, ensure_ascii=False) + '\n')

    print(f'Created module: modules/{module_id}')

if __name__ == '__main__':
    main()
