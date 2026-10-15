import argparse,json,time,re,urllib.request,urllib.error,urllib.parse,xml.etree.ElementTree as ET,datetime
from html.parser import HTMLParser
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
parser=argparse.ArgumentParser()
parser.add_argument('--host',default='https://first-person-boxing-hub.pages.dev')
parser.add_argument('--output',default='reports/live-http-audit.json')
args=parser.parse_args()
host=args.host.rstrip('/')
canonical='https://firstpersonboxinghub.wiki'
class Meta(HTMLParser):
 def __init__(self):super().__init__();self.h1=0;self.canonical=None;self.description=None;self.title='';self.intitle=False;self.jsonld=0;self.robots=None
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='h1':self.h1+=1
  if tag=='title':self.intitle=True
  if tag=='link' and a.get('rel')=='canonical':self.canonical=a.get('href')
  if tag=='meta' and a.get('name')=='description':self.description=a.get('content')
  if tag=='meta' and a.get('name')=='robots':self.robots=a.get('content')
  if tag=='script' and a.get('type')=='application/ld+json':self.jsonld+=1
 def handle_endtag(self,tag):
  if tag=='title':self.intitle=False
 def handle_data(self,data):
  if self.intitle:self.title+=data
def get_once(url):
 start=time.perf_counter();row={'url':url}
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
  with urllib.request.urlopen(req,timeout=25) as r:body=r.read().decode('utf-8',errors='replace');row.update(status=r.status,final_url=r.url,content_type=r.headers.get('Content-Type'))
 except urllib.error.HTTPError as e:body=e.read().decode('utf-8',errors='replace');row.update(status=e.code,final_url=e.url)
 except Exception as e:return {**row,'error':type(e).__name__,'reason_type':type(getattr(e,'reason',e)).__name__}
 row['request_seconds']=round(time.perf_counter()-start,3);row['body']=body
 return row
def get(url):
 errors=[]
 for attempt in range(1,4):
  row=get_once(url)
  if not row.get('error'):
   return {**row,'attempts':attempt,'transient_errors':errors}
  errors.append({key:row[key] for key in ['error','reason_type'] if key in row})
  if attempt<3:time.sleep(1)
 return {**row,'attempts':3,'transient_errors':errors}
index=get(host+'/sitemap-index.xml');tree=ET.fromstring(index.pop('body'))
children=[e.text for e in tree.iter() if e.tag.endswith('loc')]
urls=[]
for child in children:
 path=urllib.parse.urlsplit(child).path;r=get(host+path)
 urls += [e.text for e in ET.fromstring(r['body']).iter() if e.tag.endswith('loc')]
results=[]
for r in ThreadPoolExecutor(max_workers=4).map(get,[host+urllib.parse.urlsplit(u).path for u in urls]):
 body=r.pop('body','');m=Meta();m.feed(body);r['meta']=m.__dict__|{};r['meta']={k:v for k,v in r['meta'].items() if k in ['h1','canonical','title','description','jsonld','robots']};r['canonical_matches']=m.canonical==canonical+urllib.parse.urlsplit(r['url']).path;r['demo_residue']=bool(re.search('Anvil Quest|Forge Studios|FORGE-2026|discord.gg/example',body));results.append(r)
extra=[]
for path in ['/robots.txt','/sitemap.xml','/codes','/mobile','/combat','/beginner-guide','/does-not-exist-launch-check/','/.well-known/anvilwiki-deploy.txt']:
 r=get(host+path);body=r.pop('body','');r['sample']=body[:180] if 'text/plain' in r.get('content_type','') else None;extra.append(r)
formal=[]
for path in ['/','/robots.txt','/sitemap.xml']:
 r=get(canonical+path);body=r.pop('body','');m=Meta();m.feed(body);r['title']=m.title;r['is_this_site']='First Person Boxing Hub' in body or 'First Person Boxing Wiki' in body;formal.append(r)
data={'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'host':host,'index':index,'sitemap_url_count':len(urls),'pages':results,'extra':extra,'formal_domain':formal,'timing_scope':'single-host HTTP requests, not Lighthouse or field Web Vitals'}
Path(args.output).write_text(json.dumps(data,indent=2),encoding='utf-8')
print(json.dumps({'pages':len(results),'non200':[r['url'] for r in results if r.get('status')!=200],'badCanonical':[r['url'] for r in results if not r['canonical_matches']],'badH1':[r['url'] for r in results if r['meta']['h1']!=1],'missingDescription':[r['url'] for r in results if not r['meta']['description']],'demo':[r['url'] for r in results if r['demo_residue']],'extra':extra,'formal_domain':formal},indent=2))
