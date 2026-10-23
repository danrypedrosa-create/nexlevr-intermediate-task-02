#!/usr/bin/env python3
"""Teaching matcher only: not official Sigma validation or a full rule engine."""
from pathlib import Path
import json
import sys
import yaml

ROOT = Path(__file__).resolve().parent

def match_value(actual, operator, expected):
    if isinstance(expected, list):
        return any(match_value(actual, operator, value) for value in expected)
    if not operator:
        if isinstance(actual, str) and isinstance(expected, str):
            return actual.casefold() == expected.casefold()
        return actual == expected
    if not isinstance(actual, str) or not isinstance(expected, str):
        return False
    a, e = actual.casefold(), expected.casefold()
    if operator == 'contains':
        return e in a
    if operator == 'endswith':
        return a.endswith(e)
    raise ValueError('Unsupported modifier: ' + operator)

def match_rule(rule, sample):
    if any(sample['logsource'].get(k) != v for k, v in rule['logsource'].items() if k != 'definition'):
        return False
    detection = rule['detection']
    if detection['condition'] != 'selection':
        raise ValueError('Matcher supports only condition: selection')
    for field, value in detection['selection'].items():
        parts = field.split('|')
        if len(parts) > 2:
            raise ValueError('Unsupported compound modifier: ' + field)
        name = parts[0]
        operator = parts[1] if len(parts) == 2 else ''
        if name not in sample['event'] or not match_value(sample['event'][name], operator, value):
            return False
    return True

def main():
    paths = sorted((ROOT / 'rules').glob('*.yml'))
    assert len(paths) == 5, f'Expected 5 Sigma rules, found {len(paths)}'
    rules = {path.name: yaml.safe_load(path.read_text(encoding='utf-8')) for path in paths}
    required = {'title', 'id', 'status', 'description', 'logsource', 'detection', 'level', 'falsepositives', 'tags'}
    for name, rule in rules.items():
        assert required <= set(rule), f'Missing Sigma fields in {name}'
        assert rule['status'] == 'experimental'
    assert len({rule['id'] for rule in rules.values()}) == len(rules), 'Duplicate IDs'
    rows = [json.loads(x) for x in (ROOT / 'samples' / 'synthetic_events.jsonl').read_text().splitlines() if x.strip()]
    assert len(rows) == 15, f'Expected 15 sample events, found {len(rows)}'
    outcomes = []
    print('NEXLEVR Task 02 - synthetic sample matcher (NOT official Sigma CLI validation)')
    print()
    for row in rows:
        result = match_rule(rules[row['rule']], row)
        ok = result == row['expected_match']
        outcomes.append(ok)
        print(f"{'PASS' if ok else 'FAIL'} {row['rule']} :: {row['test_case']} | expected={row['expected_match']} got={result}")
    print()
    print(f'Rules loaded: {len(rules)}')
    print(f'Expected outcomes met: {sum(outcomes)}/{len(outcomes)}')
    print(f'Suspicious-pattern matches: {sum(1 for x in rows if x["expected_match"] and not x["test_case"].startswith("benign_"))}')
    print(f'Benign-context matching examples: {sum(1 for x in rows if x["expected_match"] and x["test_case"].startswith("benign_"))}')
    print(f'Nonmatching examples: {sum(1 for x in rows if not x["expected_match"])}')
    return 0 if all(outcomes) else 1

if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception as err:
        print(f'ERROR: {err}', file=sys.stderr)
        sys.exit(2)
