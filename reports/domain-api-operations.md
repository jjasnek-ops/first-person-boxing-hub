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

After login: inspect exact-domain DNSSEC controls and record inventory; prepare a safe old-DS transition and rollback. If DS removal is used, verify authoritative absence and allow old TTL/cache transition before NS change. Do not disable old signing while validators can still require the old DS without evaluating the resulting outage. Do not use an undocumented endpoint. Never use nameservers from a different Zone.

Pages project created independently with GitHub source; source commit must still be pushed and deployed. Domain binding and HTTPS are not yet complete.
