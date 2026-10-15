"""Read-only DS gate: authoritative withdrawal and recursive cache evidence."""
import argparse
import datetime
import json
import urllib.request
from pathlib import Path

import dns.flags
import dns.message
import dns.query
import dns.rdatatype

parser = argparse.ArgumentParser()
parser.add_argument('--output', default='reports/ds-after-authorized-disable.json')
args = parser.parse_args()
name = 'firstpersonboxinghub.wiki'
result = {'checked_at': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'domain': name,
          'authority': [], 'recursive': []}
for server in ['37.209.192.10', '156.154.174.82']:
    row = {'server': server}
    try:
        query = dns.message.make_query(name, 'DS', want_dnssec=True)
        query.flags &= ~dns.flags.RD
        response = dns.query.udp(query, server, timeout=5)
        row.update(aa=bool(response.flags & dns.flags.AA), rcode=response.rcode(),
                   ds_present=any(rr.rdtype == dns.rdatatype.DS for rr in response.answer),
                   answer=[rr.to_text() for rr in response.answer],
                   authority=[rr.to_text() for rr in response.authority])
    except Exception as exc:
        row['error'] = type(exc).__name__
    result['authority'].append(row)
for provider, base in [('Google', 'https://dns.google/resolve'),
                       ('Cloudflare', 'https://cloudflare-dns.com/dns-query')]:
    row = {'provider': provider}
    try:
        request = urllib.request.Request(f'{base}?name={name}&type=DS&do=true',
                                         headers={'Accept': 'application/dns-json', 'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(request, timeout=12) as response:
            data = json.load(response)
        ds = [rr for rr in data.get('Answer', []) if rr.get('type') == 43]
        row.update(response=data, ds_present=bool(ds), remaining_ds_ttl=max([rr['TTL'] for rr in ds], default=0))
    except Exception as exc:
        row['error'] = type(exc).__name__
    result['recursive'].append(row)
result['authoritative_withdrawal_verified'] = all(
    row.get('aa') and row.get('rcode') == 0 and row.get('ds_present') is False for row in result['authority'])
result['observed_recursive_caches_clear'] = all(
    row.get('response', {}).get('Status') == 0 and row.get('ds_present') is False for row in result['recursive'])
Path(args.output).write_text(json.dumps(result, indent=2), encoding='utf-8')
print(json.dumps({key: value for key, value in result.items() if key not in ['authority', 'recursive']} |
                 {'authority': [{key: row.get(key) for key in ['server', 'aa', 'rcode', 'ds_present', 'error']}
                                for row in result['authority']],
                  'recursive': [{key: row.get(key) for key in ['provider', 'ds_present', 'remaining_ds_ttl', 'error']}
                                for row in result['recursive']]}, indent=2))
