"""Public search evidence. Never infer rankings from unparsed HTML."""
import urllib.request, urllib.parse, json, datetime, re
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
root=Path('research/raw');root.mkdir(parents=True,exist_ok=True)
def get(item):
    url,name=item
    row={'url':url,'collected_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'file':str(root/name)}
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
        with urllib.request.urlopen(req,timeout=15) as r:
            body=r.read().decode('utf-8',errors='replace');row['status']=r.status
        (root/name).write_text(body,encoding='utf-8');row['body']=body
    except Exception as e:row.update(status=None,error=type(e).__name__)
    return row
suggest=[]
for suffix in ['',*'abcdefghijklmnopqrstuvwxyz']:
    q='first person boxing'+(' '+suffix if suffix else '')
    r=get(('https://suggestqueries.google.com/complete/search?client=firefox&hl=en&gl=us&q='+urllib.parse.quote(q),'suggest-'+(suffix or 'root')+'.json'))
    body=r.pop('body','')
    try:r['suggestions']=json.loads(body)[1]
    except Exception:r['suggestions']=None
    suggest.append({'query':q,**r})
    if r.get('status') in (403,429):break
Path('research/google-suggest.json').write_text(json.dumps(suggest,indent=2),encoding='utf-8')
keywords=['first person boxing','first person boxing wiki','first person boxing roblox','first person boxing guide','first person boxing codes','first person boxing controls','first person boxing mobile','first person boxing game pc','first person boxing game android','first person boxing beginner guide','first person boxing combat','first person boxing training']
serp=[]
for q in keywords:
    r=get(('https://www.google.com/search?hl=en&gl=us&num=10&q='+urllib.parse.quote(q),'google-'+q.replace(' ','-')+'.html'))
    body=r.pop('body','');r.update(query=q,rank_status='UNVERIFIED',heading_count=len(re.findall('<h3\\b',body)),blocked=bool(re.search('unusual traffic|enable JavaScript|captcha',body,re.I)))
    serp.append(r)
    if r.get('status') in (403,429):break
Path('research/google-serp-requests.json').write_text(json.dumps(serp,indent=2),encoding='utf-8')
others=[('https://www.firstpersonboxing.wiki/sitemap.xml','competitor-sitemap.xml'),('https://www.firstpersonboxing.wiki/','competitor-home.html'),('https://roterminal.co/g/10768418427-first-person-boxing','roterminal.html'),('https://trends.google.com/trends/explore?date=now%207-d&geo=US&q=first%20person%20boxing','trends.html')]
summary=[]
for r in ThreadPoolExecutor(max_workers=3).map(get,others):r.pop('body',None);summary.append(r)
Path('research/public-fetch-status.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
print(json.dumps({'suggest_queries':len(suggest),'unique_suggestions':len(set(x for r in suggest for x in (r.get('suggestions') or []))),'serp_queries':len(serp),'serp':serp,'other':summary},indent=2))
