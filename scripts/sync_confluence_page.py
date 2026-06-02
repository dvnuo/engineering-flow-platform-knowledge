#!/usr/bin/env python3
"""Sync approved Confluence pages into governed target files.

This skeleton expects Confluence Cloud REST API credentials in environment variables:
- CONFLUENCE_BASE_URL, for example https://your-company.atlassian.net
- CONFLUENCE_EMAIL
- CONFLUENCE_API_TOKEN

The script reads sync_manifest.json and updates enabled entries only.
"""
from pathlib import Path
import argparse, base64, datetime, html, json, os, re, sys, urllib.request

ROOT = Path(__file__).resolve().parents[1]

def now_utc():
    return datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).strftime('%Y-%m-%dT%H:%M:%SZ')

def strip_html(value: str) -> str:
    # Minimal fallback conversion. Replace with a reviewed converter if approved.
    value = re.sub(r'<br\s*/?>', '\n', value, flags=re.I)
    value = re.sub(r'</p\s*>', '\n\n', value, flags=re.I)
    value = re.sub(r'<[^>]+>', '', value)
    return html.unescape(value).strip()

def fetch_confluence_page(base_url, email, token, page_id):
    if not base_url or not email or not token:
        raise RuntimeError('Missing Confluence credentials')
    url = f"{base_url.rstrip('/')}/wiki/api/v2/pages/{page_id}?body-format=storage"
    auth = base64.b64encode(f'{email}:{token}'.encode()).decode()
    req = urllib.request.Request(url, headers={'Authorization': f'Basic {auth}', 'Accept': 'application/json'})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode('utf-8'))

def render_target(entry, page, retrieved_at):
    version = str(page.get('version', {}).get('number', entry.get('source_version', 'unknown')))
    title = page.get('title') or entry.get('source_title') or 'Untitled Confluence Page'
    updated_at = page.get('version', {}).get('createdAt') or entry.get('source_last_updated_at') or retrieved_at
    body_value = (((page.get('body') or {}).get('storage') or {}).get('value') or '')
    body_text = strip_html(body_value)
    return f"""---
title: "{title}"
maintenance_action: source_sync
updated_at_utc: "{retrieved_at}"
source:
  type: confluence
  uri: "{entry.get('source_uri','')}"
  id: "{entry.get('source_id','')}"
  title: "{title}"
  observed_at_utc: "{updated_at}"
  retrieved_at_utc: "{retrieved_at}"
  version: "{version}"
status: draft
source_of_truth: false
---

# {title}

> This file is a controlled mirror of an approved Confluence source. Do not edit the body manually. Update the source or the sync configuration instead.

## Source metadata

| Field | Value |
|---|---|
| Source type | Confluence |
| Source URI | {entry.get('source_uri','')} |
| Source page ID | {entry.get('source_id','')} |
| Source version | {version} |
| Source observed at UTC | {updated_at} |
| Retrieved at UTC | {retrieved_at} |
| Target path | {entry.get('target_path','')} |

## Mirrored content

{body_text}
"""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--manifest', default='sync_manifest.json')
    args = ap.parse_args()

    manifest = json.loads((ROOT/args.manifest).read_text(encoding='utf-8'))
    base_url = os.environ.get('CONFLUENCE_BASE_URL')
    email = os.environ.get('CONFLUENCE_EMAIL')
    token = os.environ.get('CONFLUENCE_API_TOKEN')
    retrieved_at = now_utc()
    changed = 0

    for entry in manifest.get('entries', []):
        if not entry.get('enabled'):
            continue
        if entry.get('source_type') != 'confluence':
            continue
        page = fetch_confluence_page(base_url, email, token, entry['source_id'])
        target = ROOT / entry['target_path']
        if not str(target.resolve()).startswith(str(ROOT.resolve())):
            raise RuntimeError(f'Unsafe target path: {target}')
        target.parent.mkdir(parents=True, exist_ok=True)
        rendered = render_target(entry, page, retrieved_at)
        old = target.read_text(encoding='utf-8') if target.exists() else ''
        if old != rendered:
            target.write_text(rendered, encoding='utf-8')
            changed += 1
            log = {
                'timestamp_utc': retrieved_at,
                'maintenance_action': 'source_sync',
                'source': {
                    'type': 'confluence',
                    'uri': entry.get('source_uri'),
                    'id': entry.get('source_id'),
                    'title': page.get('title') or entry.get('source_title'),
                    'observed_at_utc': page.get('version', {}).get('createdAt') or retrieved_at,
                    'retrieved_at_utc': retrieved_at,
                    'version': str(page.get('version', {}).get('number', 'unknown'))
                },
                'target': entry.get('target_path'),
                'owner': entry.get('owner'),
                'reviewer': entry.get('reviewer')
            }
            with (ROOT/'maintenance/source-log.jsonl').open('a', encoding='utf-8') as f:
                f.write(json.dumps(log, ensure_ascii=False) + '\n')

    print(f'Confluence sync completed. Changed targets: {changed}')

if __name__ == '__main__':
    main()
