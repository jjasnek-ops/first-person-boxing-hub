# Domain operations and safety gate

## 2026-10-15 — Exact target only

1. Query firstpersonboxinghub.wiki Zone: absent.
2. Create full Zone in existing account, Free plan: success; read-back retained in zone-state.json.
3. Read Cloudflare NS: armfazh.ns.cloudflare.com / laura.ns.cloudflare.com.
4. Read Spaceship exact-domain state: registered, basic NS launch1.spaceship.net / launch2.spaceship.net.
5. Query .wiki authoritative DS on y.nic.wiki (156.154.173.82) and a.nic.wiki (37.209.192.10): AA=true, NOERROR; both return DS key tag 63051 / algorithm 13 / digest type 2 / digest B59B0A89BBAA94417C436484408DF8C27CA0145A37F03A7EF2819097BAD69E25, TTL 3600. Exact responses and timestamps: dns-preflight.json.
6. Google recursive DNS confirms existing DS and DNSKEY; AD=true. Cloudflare 1.1.1.1 direct UDP check failed with connection reset, separately recorded, not treated as registry proof.
7. Target Cloudflare DNSSEC is disabled with no DS. Thus the old DS is incompatible with a blind NS change. NS write: BLOCKED. No NS, DS or DNSSEC mutation performed.
8. Reviewed official registrar docs; public API does not document DS management. Browser expired-session prompt requires user login. Request sent while independent site work continues.

Existing public DNS showed registrar parking A addresses, no MX or TXT records in the checked apex responses. The complete provider record inventory must still be read before a migration. No existing record deleted.

User steering received after this audit: skip DNSSEC work for genuinely unsigned newly purchased domains; do not proactively enable, disable or restore DNSSEC. This specific domain already has authoritative DS and a validated chain, so it is not in the unsigned branch. No DNSSEC write is authorized by the new steering. Confirm whether the registrar supports an automatic safe transition; otherwise retain NS and request only the necessary user action. Do not use an undocumented endpoint or blind incompatible switch. Never use nameservers from a different Zone.

Pages project created independently with GitHub source. Commit 22d42a36ee31fd2e89294a1c3bcc206096f35da8 was pushed; first production deployment eba4586a-8989-49e5-87b2-00029118e497 succeeded. Domain binding and HTTPS on the formal host are not yet complete.

## GSC TXT preparation (normal DNS write, no DNSSEC mutation)

Requested a new Domain Property for firstpersonboxinghub.wiki in the user's existing GSC session. The exact returned Google TXT value was added to current Spaceship DNS with the documented TXT schema, force=false. Read before write found no custom records; read after write confirmed exactly the intended TXT. The same value was pre-staged in the target Cloudflare Zone. This proves DNS TXT write permission at both providers. No unrelated record was changed. NS write remains unverified and blocked by the known DS mismatch.

## Resumed after user login

Spaceship login restored and actual DNSSEC UI shows Enabled with automatically configured DS. Fresh authoritative DS still exists; CF signing remains disabled. Verified target NS in a draft form and cancelled it. No NS/DS/DNSSEC mutation. Exact migration confirmation requested because the user retained the no-proactive-DNSSEC boundary. See domain-resume-status.md and associated read-only JSON evidence.

## Authorized migration started — 2026-10-15

The user explicitly approved disabling only this domain's existing Spaceship DNSSEC/old DS and continuing launch. Submitted Disable DNSSEC in the exact domain UI; read-back shows Disabled. No automatic re-enable. Screenshots retained locally. At 04:23:43Z and 04:24:34Z both checked .wiki authoritative servers still returned DS 63051. Google and Cloudflare recursive DS responses also retained it (TTL 3600). NS retained while actual registry withdrawal is pending. The previous no-authorization blocker is superseded by this explicit user approval; no further confirmation needed for that same scoped action.

## Registry withdrawal and NS update

2026-10-15T04:26:46Z: DS withdrawal verified against two authoritative .wiki servers. CF recursive DS also clear; Google still had cached DS (TTL 3417). Under the approved migration and original cache-risk SOP, assessed this as an unlaunched new site with no existing website or mail service; proceeded with NS onboarding while keeping formal acceptance blocked until public validation succeeds. No DNSSEC validation bypass used.

2026-10-15T04:28:17Z: documented Spaceship PUT /v1/domains/firstpersonboxinghub.wiki/nameservers set the exact assigned CF hosts. Fresh CF Zone lookup matched the domain before write. Registrar read-back and browser reload confirm custom NS saved. 04:31:04Z: both parent servers now delegate to the exact CF pair. Google DS query is clear, but address queries still showed EDE 10 DNSSEC validation failures; CF A/AAAA/TXT/NS resolve normally. 04:31:13Z: requested the documented CF activation check once (Free Zone rate limit respected). Zone and Pages bindings still pending at the next short read. No repeated NS/DS writes or automatic DNSSEC re-enable.

## Formal hostname verification

Both Pages domain bindings and the Universal certificate now report Active. HTTPS browser navigation works without a certificate warning. Four canonicalization checks pass, including www-to-apex and HTTP-to-HTTPS with paths and query strings preserved. The unsupported domain-source line in Pages _redirects was removed; the existing token could not read Rulesets, so used the documented Page Rules API under existing Zone Write permission. Exactly one rule was added to this Zone; no new credential scope, Function or paid service. Initial malformed wildcard pattern was rejected without mutation; the accepted rule matches www.firstpersonboxinghub.wiki/* and redirects 301 to https://firstpersonboxinghub.wiki/$1.

The final formal HTTP pass covers all 21 sitemap URLs, metadata, robots, guide aliases and true 404. That pass has zero transient retries on page requests. Earlier certificate-deployment connection errors are retained in the operational notes, not treated as passing evidence.

GSC sitemap index submitted in the correct Domain Property; Success and today's Last read confirmed. Homepage and beginner-guide URL Inspection show not indexed/unknown to Google; their indexing requests were accepted into the priority crawl queue. No indexing, impressions, clicks or organic traffic claimed.

Formal hostname analytics: before consent no gtag script; Accept loads only G-P1MXKVMQVT. Actual formal home and beginner-guide visits appear in property 559103339 Realtime pages as / and /guides/beginner-guide/, one view each in the observed snapshot. Formal CDP network capture timed out twice, so receipt was verified via the actual GA4 UI instead. Earlier Pages-specific HTTP 204 network proof is not relabeled as formal-host proof. All visits are self-tests.

## Browser capture and cache correction recovered

Reloaded the owned formal tab and recovered CDP. Actual formal home and beginner page_view requests returned HTTP 204, exact Measurement ID; sanitized ga4-formal-network-proof.json supersedes the temporary capture limitation. Formal 375×812 emulation on home/beginner/combat confirms no document overflow; cleared metrics and confirmed default 1280px. Pagefind content cache key now includes generated entry manifest, one focused regression added; 17 suites / 201 tests, build/lint/types and CI passed; deployed b70c6ce1728ff8699623f83e2de49cb3e4dbc739. Actual formal search returns four stamina results and correct fragment.

## Final public DNS gate completed

At 2026-10-15T05:24:53Z, Google and Cloudflare validating public resolver checks all passed (14/14), including no old DS, exact NS, apex/www A/AAAA and GSC TXT. Both checked registry delegations match the assigned Cloudflare pair. Evidence formal-domain-dns.json; earlier snapshots retain actual cache behavior. Optional Google official cache-flush UI attempt did not yield a verified completion and is not used as success evidence. No repeated NS/DS mutation or validation bypass. Enabled SITE_LAUNCHED=true only after the passing gate.
