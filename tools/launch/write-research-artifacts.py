import json,csv,datetime
from pathlib import Path
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
keywords=['first person boxing','first person boxing wiki','first person boxing codes','first person boxing controls','first person boxing game pc','first person boxing game android','first person boxing beginner guide','first person boxing combat','first person boxing training','first person boxing update']
rows=[dict(keyword=k,search_volume=None,volume_period='last 28 days',geography='US',search_engine='Google',KD=None,intent='informational / game access' if k==keywords[0] else 'informational',trend=None,source='Similarweb Keyword Generator',collected_at=stamp,evidence_reference='browser-audit.md; screenshots/us-plan-limit.png',status='BLOCKED',reason='US geography requires custom plan; target phrase metric not verified') for k in keywords]
rows += [dict(keyword=k,search_volume=v,volume_period='28 days, as of Oct 12 2026',geography='Worldwide',search_engine='Google',KD=None,intent='generic game discovery; target Roblox intent unverified',trend=None,source='Similarweb Keyword Generator',collected_at=stamp,evidence_reference='browser-audit.md',status='VERIFIED',reason='Not counted as target-game opportunity') for k,v in [('first person boxing game',140),('are there any first person boxing games','<50')]]
Path('research/similarweb/raw-keywords.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
with open('research/similarweb/keyword-metrics.csv','w',newline='',encoding='utf-8') as f:
 w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
defs=[
('First Person Boxing Wiki & Beginner Guides','first person boxing wiki',['first person boxing roblox'],'/','hub','What is the game, and where should I start?','Official game identity, supported platform list and four verified-scope guides.','A','P0','COMPLETED','low'),
('First Person Boxing Beginner Guide','first person boxing beginner guide',['first person boxing how to play'],'/guides/beginner-guide/','steps','How should a new player practice?','Use AI practice and learn one mechanic at a time; drills are editorial.','A + editorial','P0','COMPLETED','medium'),
('First Person Boxing Combat','first person boxing combat',['first person boxing stamina'],'/guides/combat/','mechanic reference','Which combat systems are confirmed?','Guards, slips, counters, stamina, knockdowns and replays are officially described.','A + editorial','P0','COMPLETED','medium'),
('First Person Boxing Mobile','first person boxing mobile',['first person boxing game android','first person boxing game pc'],'/guides/mobile/','setup checks','Is mobile support advertised and how do I access the right game?','Mobile is listed officially; exact touch layout remains unverified.','A, device untested','P0','COMPLETED','medium'),
('First Person Boxing Codes','first person boxing codes',['first person boxing codes roblox','first person boxing roblox codes'],'/guides/codes/','evidence status table','Which working codes have been verified?','None verified in the limited official-source review; interface unverified.','A for source observation','P1','COMPLETED','high'),
('Controls','first person boxing controls',['first person boxing game pc'],'/controls/','key table','What are the current inputs?','Await verified game-specific keybind evidence.','D withheld','P1','BLOCKED','high'),
('Training','first person boxing training',[],'/training/','practice','Is there a separate progression-based training system?','AI practice confirmed; standalone rewards or stat training unverified.','D withheld','P2','NOT_STARTED','high'),
('Updates','first person boxing update',[],'/updates/','changelog','What changed in the latest patch?','API update timestamp is not patch notes.','D withheld','P2','NOT_STARTED','high'),
('Gloves','first person boxing gloves',[],'/gloves/','equipment','Are gloves an equipment system?','Suggest phrase exists but game-specific system is not verified.','D withheld','P2','BLOCKED','high')]
matrix=[]
published=[x[3] for x in defs if x[10]=='COMPLETED']
for title,primary,secondary,slug,fmt,question,answer,grade,priority,status,cost in defs:
 matrix.append(dict(page_title=title,primary_keyword=primary,secondary_keywords=secondary,intent='informational',volume=None,period=None,geography=None,KD=None,serp_score=None,slug=slug,format=fmt,user_question=question,quick_answer=answer,source_count=2 if status=='COMPLETED' else 0,evidence_grade=grade,internal_links=[u for u in published if u!=slug],priority=priority,publish_status=status,upkeep_cost=cost))
Path('research/page-matrix.json').write_text(json.dumps(matrix,indent=2),encoding='utf-8')
lines=['# Page matrix','','Status means local publish readiness until deployment is verified. Full requested fields and null metrics: page-matrix.json. Two source URLs share the same developer description and are not independent corroboration.','','| Page | Native URL | Keyword | Evidence | Priority | Status |','| --- | --- | --- | --- | --- | --- |']
for r in matrix:lines.append(f"| {r['page_title']} | {r['slug']} | {r['primary_keyword']} | {r['evidence_grade']} | {r['priority']} | {r['publish_status']} |")
Path('research/page-matrix.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
suggest=json.loads(Path('research/google-suggest.json').read_text(encoding='utf-8'))
allterms=sorted(set(x for r in suggest for x in (r.get('suggestions') or [])))
relevant=[x for x in allterms if x.startswith('first person boxing') or x=='1st person boxing']
Path('research/keyword-intents.md').write_text('# Keyword intent evidence\n\nGoogle Suggest: 27 root/a-z queries, 34 unique suggestions. '+str(len(relevant))+' topic-related suggestions remain after removing other fighting games, real boxing and unrelated queries. They establish wording, not traffic or target-game identity.\n\n'+'\n'.join('- '+x for x in relevant)+'\n\nCodes / codes roblox / roblox codes are one intent and share one page. PC and Android are access intents, not proof of current keybinds. Gloves remains a research lead only. The browser Google related-search block additionally supports Roblox mobile wording. Controls, beginner and combat are editorial task intents; no verified volume is assigned.\n',encoding='utf-8')
print('Wrote metrics, page matrix and intent notes; related suggestion count:',len(relevant))
