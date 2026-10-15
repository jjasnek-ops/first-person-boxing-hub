"""Read-only registry delegation and validating public-resolver launch checks."""
import argparse
import datetime
import json
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import dns.message
import dns.query
import dns.rdatatype

parser = argparse.ArgumentParser()
parser.add_argument('--output', default='reports/formal-domain-dns.json')
parser.add_argument('--summary', action='store_true')
args = parser.parse_args()
domain = 'firstpersonboxinghub.wiki'
expected = {'armfazh.ns.cloudflare.com', 'laura.ns.cloudflare.com'}
registry = []
for server in ['37.209.192.10', '156.154.174.82']:
    row = {'server': server}
    try:
        response = dns.query.udp(dns.message.make_query(domain, 'NS'), server, timeout=5)
        names = [str(value.target).rstrip('.') for rr in list(response.answer) + list(response.authority)
                 if rr.rdtype == dns.rdatatype.NS and str(rr.name).rstrip('.') == domain for value in rr]
        row.update(rcode=response.rcode(), nameservers=names, matches_target=set(names) == expected)
    except Exception as exc:
        row['error'] = type(exc).__name__
    registry.append(row)

def resolve(job):
    provider, base, name, kind = job
    row = {'provider': provider, 'name': name, 'type': kind}
    try:
        request = urllib.request.Request(f'{base}?name={name}&type={kind}&do=true',
                                         headers={'Accept': 'application/dns-json', 'User-Agent': 'Mozilla/5.0',
                                                  'Cache-Control': 'no-cache'})
        with urllib.request.urlopen(request, timeout=15) as response:
            row['response'] = json.load(response)
            row['http_cache'] = {key: response.headers.get(key) for key in ['Date', 'Age', 'Cache-Control']}
    except Exception as exc:
        row['error'] = type(exc).__name__
    return row

jobs = [(provider, base, name, kind)
        for provider, base in [('Google', 'https://dns.google/resolve'),
                               ('Cloudflare', 'https://cloudflare-dns.com/dns-query')]
        for name, kinds in [(domain, ['DS', 'NS', 'A', 'AAAA', 'TXT']), ('www.' + domain, ['A', 'AAAA'])]
        for kind in kinds]
with ThreadPoolExecutor(max_workers=4) as pool:
    recursive = list(pool.map(resolve, jobs))
for row in recursive:
    data = row.get('response', {})
    answers = data.get('Answer', [])
    valid = data.get('Status') == 0 and not row.get('error')
    if row['type'] == 'DS':
        valid = valid and not any(rr.get('type') == 43 for rr in answers)
    elif row['type'] == 'NS':
        valid = valid and {rr['data'].rstrip('.') for rr in answers if rr.get('type') == 2} == expected
    elif row['type'] in ['A', 'AAAA']:
        valid = valid and any(rr.get('type') == (1 if row['type'] == 'A' else 28) for rr in answers)
    elif row['type'] == 'TXT':
        valid = valid and any('google-site-verification=' in rr.get('data', '') for rr in answers)
    row['passed'] = bool(valid)
result = {'checked_at': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'domain': domain,
          'registry': registry, 'recursive': recursive,
          'registry_delegation_verified': all(row.get('matches_target') for row in registry),
          'all_recursive_checks_passed': all(row['passed'] for row in recursive),
          'scope': 'Observed authoritative servers and public resolvers; no claim of globally expired caches.'}
Path(args.output).write_text(json.dumps(result, indent=2), encoding='utf-8')
if args.summary:
    print(json.dumps({'checked_at': result['checked_at'],
                      'registry_delegation_verified': result['registry_delegation_verified'],
                      'all_recursive_checks_passed': result['all_recursive_checks_passed'],
                      'failed': [{'provider': row['provider'], 'name': row['name'], 'type': row['type'],
                                  'status': row.get('response', {}).get('Status')} for row in recursive if not row['passed']]}, indent=2))
    raise SystemExit(0)
print(json.dumps({'checked_at': result['checked_at'], 'registry': registry,
                  'recursive': [{'provider': row['provider'], 'name': row['name'], 'type': row['type'],
                                 'status': row.get('response', {}).get('Status'),
                                 'answers': [rr['data'] for rr in row.get('response', {}).get('Answer', [])
                                             if rr.get('type') != 46], 'error': row.get('error')}
                                for row in recursive]}, indent=2))
