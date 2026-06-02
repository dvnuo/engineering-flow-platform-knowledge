#!/usr/bin/env python3
"""Validate required provenance front matter for governed markdown files."""
from pathlib import Path
import re, sys, json

REQUIRED = [
    'maintenance_action:',
    'updated_at_utc:',
    'source:',
    'type:',
    'uri:',
    'title:',
    'observed_at_utc:',
    'retrieved_at_utc:',
    'version:',
    'status:',
    'source_of_truth:',
]

SCOPES = [Path('modules'), Path('docs'), Path('maintenance')]
IGNORE = {'.gitkeep'}

def has_front_matter(text: str) -> bool:
    return text.startswith('---\n') and '\n---\n' in text[4:]

def validate_file(path: Path):
    text = path.read_text(encoding='utf-8')
    errors = []
    if not has_front_matter(text):
        errors.append('missing YAML front matter')
        return errors
    fm = text.split('\n---\n', 1)[0]
    for key in REQUIRED:
        if key not in fm:
            errors.append(f'missing {key}')
    # Basic UTC timestamp shape check.
    matches = re.findall(r'(updated_at_utc|observed_at_utc|retrieved_at_utc):\s*"?([^"\n]+)"?', fm)
    for field, value in matches:
        if not re.match(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$', value.strip()):
            errors.append(f'{field} is not ISO-8601 UTC: {value}')
    return errors

def main():
    failures = []
    for scope in SCOPES:
        if not scope.exists():
            continue
        for path in scope.rglob('*.md'):
            if path.name in IGNORE:
                continue
            errs = validate_file(path)
            if errs:
                failures.append((str(path), errs))
    if failures:
        print('Provenance validation failed:')
        for path, errs in failures:
            print(f'- {path}')
            for e in errs:
                print(f'  - {e}')
        sys.exit(1)
    print('Provenance validation passed.')

if __name__ == '__main__':
    main()
