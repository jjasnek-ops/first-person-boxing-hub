# Search Console and analytics

## Search Console

Status: COMPLETED for Domain Property ownership verification, sc-domain:firstpersonboxinghub.wiki. Confirmed absent in the visible property list, created it, and added the exact TXT through documented registrar DNS API plus the target CF Zone. Public Google DNS returns TXT with AD=true. GSC displayed Ownership verified and Processing data. Preserve the TXT. Screenshot retained locally, excluded from the public repository due account chrome.

Sitemap submission: BLOCKED until the formal host serves XML over HTTPS. URL Inspection/discovery/indexing/impressions/clicks: NOT_STARTED or unverified. No other property's metrics reused. Verification is not indexing.

## GA4

Property creation: COMPLETED. Existing account, new property First Person Boxing Hub, property ID 559103339. Timezone China Time (GMT+08:00), USD; Games, small site, understand traffic objective. No existing project property modified. Website stream https://firstpersonboxinghub.wiki, stream ID 16132040655, Measurement ID G-P1MXKVMQVT. Creation was visibly confirmed, without a new terms acceptance.

Instrumentation deployed through wrangler.toml and the inherited consent-gated loader; privacy and banner copy updated. Local build explicitly used PUBLIC_GA_ID because local Astro does not read Wrangler vars. Consent regression suite: 4 assertions passed. CF source build reads Wrangler vars; actual remote HTML and browser confirm the project ID exists, banner appears, and no gtag script is loaded before consent. Clicking Accept removes the banner and loads the exact project's gtag.js. Browser network pageview and GA received-data verification are recorded below after the test.

An earlier DOM snapshot misleadingly showed Loading while the actual UI had loaded; that diagnostic is superseded. The temporary Google tag iframe also resisted pointer actions; Escape recovered it. No UI-loading blocker remains.

Advertising remains disabled. The local GA screenshot is excluded from the public repository. Ordinary reporting, organic sessions and indexing remain unestablished; a self-test must not be represented as organic traffic.

Decline branch also passed on the actual immutable deployment: after Decline and reload, the banner stays dismissed and no gtag script is loaded.

## Browser receipt proof

Status: COMPLETED for Pages instrumentation and received self-test. Before consent: banner visible, no gtag script. Accept loads gtag.js for G-P1MXKVMQVT (HTTP 200). The actual browser sent en=page_view for /guides/combat/ to Google Analytics /g/collect with the same measurement ID and received HTTP 204. Sanitized evidence: ga4-network-proof.json (no client ID, cookies or headers retained). The correct property's Realtime overview displayed page_view=1 and session_start=1. Browser warning/error log was empty. Local screenshot: screenshots/ga4-realtime.png. Formal-host self-test remains BLOCKED until DNS/TLS launch; this Pages self-test is not an organic session or evidence of Google indexing.

## Formal hostname self-test — 2026-10-15

Consent loading on https://firstpersonboxinghub.wiki was verified in the actual browser: no GA script before acceptance; after Accept, the exact script URL is https://www.googletagmanager.com/gtag/js?id=G-P1MXKVMQVT. Navigated through the home page's Start boxing link to /guides/beginner-guide/. The correct property's Realtime pages reported active users=1, views=2, with / and /guides/beginner-guide/ each one view. Receipt and page-path verification: COMPLETED. Screenshot kept locally: screenshots/ga4-formal-realtime-pages.png. Formal raw network capture was unavailable due repeated CDP timeouts; no formal-host HTTP 204 claim is made. This is a real self-test, not organic acquisition data.

GSC sitemap submitted successfully and displayed Success / Last read Oct 15, 2026. Initial discovered count 0. URL Inspection for home and beginner guide: not indexed, URL unknown to Google. Both Request indexing operations returned Indexing requested / priority crawl queue. Screenshots gsc-sitemap-submitted.png, gsc-home-index-requested.png and gsc-core-inspection.png are local-only. Sitemap receipt, indexing request, discovery and actual indexing remain separate facts.
