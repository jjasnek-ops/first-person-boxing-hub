# Formal launch verification

Date: 2026-10-15 Asia/Shanghai. Final acceptance: COMPLETED.

| Gate | Actual evidence |
| --- | --- |
| Registrar | Exact Cloudflare NS saved and read back; screenshot spaceship-ns-saved.png. |
| Registry | Two .wiki authoritative servers confirm delegation and withdrawal of old DS. |
| Cloudflare | Zone Active since 04:32:15Z; apex and www Pages domains Active. |
| HTTPS | Universal certificate Active, LetsEncrypt, expires 2027-01-13; actual browser without warnings. |
| Public DNS | COMPLETED at 05:24:53Z. Google + Cloudflare 14/14 checks; no old DS/SERVFAIL. formal-domain-dns.json; no global cache-expiry guarantee. |
| HTTP | formal-http-audit.json: 21 sitemap pages all 200, one H1, canonical and description correct. Robots, sitemap/guide aliases, real 404 and exact deployed SHA verified. |
| Canonical host | www 301 to HTTPS apex, HTTP upgrades, path/query preserved; formal-redirect-audit.json. |
| UI | Formal desktop and actual 375×812 phone emulation; no document overflow on Home/Beginner/Combat. Search four stamina results, functional guide link and anchor. |
| GSC | Correct Domain Property verified; sitemap-index.xml Success / Oct 15 last read / initial discovered 0; home and beginner indexing requests accepted. |
| GA4 | Consent gate; formal home and beginner page_view HTTP 204; correct property Realtime page paths received. Self-tests only. |
| Code gate | 17 suites / 201 tests, build, lint, types and site checks passed. Latest implementation b70c6ce1728ff8699623f83e2de49cb3e4dbc739, Pages f9dfab8f-cb21-410c-ab4e-31e7e99f0c0f. |
| IndexNow | SITE_LAUNCHED=true enabled after the DNS gate. Final release notification result is being verified. |

Specific DNSSEC migration was explicitly authorized. Existing Spaceship signing disabled and registry DS removed; no automatic re-enable. Initial stale validating resolver responses are recorded honestly. No browser warning bypass or DNSSEC validation bypass used.

Indexing, search visibility, organic traffic, revenue, Lighthouse scores and field Core Web Vitals are not claimed. HTTP timing is one client sample. Day 3/7/14/28 review plan is saved, not an unattended scheduled task.
