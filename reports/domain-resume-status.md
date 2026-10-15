# Domain resume closure — 2026-10-15

Domain onboarding: COMPLETED. Public resolver acceptance: COMPLETED.

Spaceship login was restored. The exact domain firstpersonboxinghub.wiki showed DNSSEC Enabled, with authoritative DS 63051 / algorithm 13. Therefore the user's unsigned-new-domain shortcut did not apply. The user explicitly answered “授权此次处理并继续上线” to the scoped request to disable this domain's old DNSSEC/DS, verify withdrawal and migrate NS; no further confirmation was needed for this same scope.

- Disabled existing Spaceship DNSSEC through its actual domain UI and confirmed Disabled. No automatic re-enable.
- At 04:26:46Z, both checked .wiki authoritative servers returned no DS. Initial recursive caches still retained the old DS. Assessed the approved cache-risk branch for this unlaunched site with no existing web/mail service; retained the final acceptance gate until observed public resolver errors clear.
- At 04:28:17Z, documented registrar NS API saved the exact Cloudflare pair, armfazh.ns.cloudflare.com and laura.ns.cloudflare.com. Read-back and actual browser confirmed saved values.
- At 04:31:04Z both checked registry servers delegated to Cloudflare. Zone activated 04:32:15Z. Apex and www Pages bindings and Universal certificate are Active.
- Formal HTTPS, 21-page audit, permanent redirects, browser mobile/search, GSC sitemap and GA4 formal-host receipt passed. See launch-verification.md.

Historical pending/login/authorization snapshots remain dated evidence, not current blockers. No unrelated account resources changed and no credential published.

Final resolver gate passed 05:24:53Z: 14/14 Google/Cloudflare checks; no old DS or SERVFAIL. Both registry delegations match the assigned NS. Evidence: formal-domain-dns.json.
