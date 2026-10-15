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
