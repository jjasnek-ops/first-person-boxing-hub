"""Read-only authoritative DNS evidence; no credentials or mutations."""
import json, datetime
from pathlib import Path
import dns.message, dns.query, dns.flags, dns.rcode, dns.rdatatype
import urllib.request

domain = 'firstpersonboxinghub.wiki.'
records = []
def query(name, kind, server):
    q = dns.message.make_query(name, kind, want_dnssec=True)
    q.flags &= ~dns.flags.RD
    for tcp in (False, True):
        try:
            r = (dns.query.tcp if tcp else dns.query.udp)(q, server, timeout=4)
            row = {'name':name,'type':kind,'server':server,'transport':'TCP' if tcp else 'UDP','rcode':dns.rcode.to_text(r.rcode()),'authoritative':bool(r.flags & dns.flags.AA),'answer':[x.to_text() for x in r.answer],'authority':[x.to_text() for x in r.authority]}
            records.append(row)
            return r
        except Exception as e:
            records.append({'name':name,'type':kind,'server':server,'transport':'TCP' if tcp else 'UDP','error':type(e).__name__})
    return None

def doh(name, kind):
    url = f'https://dns.google/resolve?name={name}&type={kind}&do=true'
    with urllib.request.urlopen(url, timeout=15) as r:
        data=json.load(r)
    records.append({'source':url,'response':data})
    return data

tld = doh('wiki','NS')
for rr in tld.get('Answer',[])[:2]:
    host=rr['data']
    ips=doh(host,'A')
    for addr in ips.get('Answer',[]):
        if addr['type']==1:
            query(domain,'DS',addr['data'])
            query(domain,'NS',addr['data'])
            break
for server in ['1.1.1.1','8.8.8.8']:
    # Recursive cache check is explicitly separate from authoritative proof.
    q=dns.message.make_query(domain,'DS',want_dnssec=True)
    try:
        r=dns.query.udp(q,server,timeout=4)
        records.append({'source':'recursive-cache','server':server,'rcode':dns.rcode.to_text(r.rcode()),'answer':[x.to_text() for x in r.answer],'authority':[x.to_text() for x in r.authority]})
    except Exception as e:
        records.append({'source':'recursive-cache','server':server,'error':type(e).__name__})
for kind in ['DS','NS','MX','TXT','A','AAAA','DNSKEY']:
    try:doh(domain,kind)
    except Exception as e:records.append({'source':'doh','type':kind,'error':type(e).__name__})
result={'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'domain':domain,'records':records}
Path('reports/dns-preflight.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
