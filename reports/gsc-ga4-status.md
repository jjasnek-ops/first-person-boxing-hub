# Search Console and analytics

## Search Console

Status: COMPLETED for domain ownership verification. Property: sc-domain:firstpersonboxinghub.wiki in the user's existing Google account. Confirmed it was absent from the visible property list, then added the website Domain Property. Added the exact returned verification TXT through the documented registrar API and pre-staged it in Cloudflare. Public Google DNS returns the TXT with AD=true. GSC Verify returned Ownership verified; the new property shows firstpersonboxinghub.wiki and Processing data.

The verification screenshot is retained locally at screenshots/gsc-verified.png and excluded from the public repository because it includes account chrome. Do not remove the verification TXT during migration.

Sitemap submission: BLOCKED until the formal hostname serves the real XML over HTTPS. URL Inspection / discovery / indexing / impressions / clicks: NOT_STARTED or unverified. No data from another property is reused. Verification is not indexing.

## GA4

Status: BLOCKED. Opened analytics.google.com; it stayed on Loading. One reload did not recover it. No permission error or account state could be established; this is a UI-loading blocker, not a claimed lack of permission. No measurement ID created or borrowed. PUBLIC_GA_ID remains empty; analytics is not installed. Realtime pageview, landing pages and organic sessions are not verified.

Advertising remains disabled. Privacy copy reflects the absence of tracking.
