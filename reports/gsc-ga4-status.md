# Search Console and analytics

Updated 2026-10-15. Setup and formal-host self-tests: COMPLETED.

## Search Console

Correct Domain Property: sc-domain:firstpersonboxinghub.wiki. Ownership verified; exact Google TXT preserved in Cloudflare. No other property's metrics reused.

Submitted https://firstpersonboxinghub.wiki/sitemap-index.xml. Actual Sitemaps UI shows Success, Submitted / Last read Oct 15, 2026, Discovered pages 0 at latest inspection. Home and /guides/beginner-guide/ URL Inspection showed not indexed / URL unknown to Google. Both Request indexing actions returned Indexing requested / priority crawl queue. Receipt and request acceptance do not prove indexing, impressions or clicks.

Local-only proof screenshots: screenshots/gsc-sitemap-submitted.png, gsc-home-index-requested.png and gsc-core-inspection.png. Account chrome is excluded from the public repository.

## GA4

New site-specific property 559103339, stream 16132040655, Measurement ID G-P1MXKVMQVT. Timezone China (GMT+08:00), USD. Correct website stream: https://firstpersonboxinghub.wiki. No existing project property changed.

Deployed consent-gated loader: before consent no gtag script; Accept loads the exact Measurement ID. Decline plus reload on the immutable deployment retains the rejection and does not load gtag. Four consent regression assertions pass. Advertising, Cloudflare Web Analytics and comments remain off.

Actual formal-host home and beginner guide sent page_view to GA /g/collect and received HTTP 204. gtag.js returned HTTP 200. Sanitized evidence: ga4-formal-network-proof.json; no client ID, cookies or request headers stored. Initial CDP timeouts were recovered after reloading the owned site tab; the final formal-host capture succeeded.

Correct-property Realtime pages snapshot showed one active user, two views: / and /guides/beginner-guide/ each one. Local-only screenshot: screenshots/ga4-formal-realtime-pages.png. Earlier Pages proof is separately retained in ga4-network-proof.json.

All visits above are self-tests. Organic acquisition, ordinary reporting, indexing, impressions, clicks and revenue remain unestablished.
