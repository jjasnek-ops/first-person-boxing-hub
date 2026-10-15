# Launch verification

Pages deployment status: COMPLETED. Formal-domain launch: BLOCKED.

The final live HTTP audit tested https://first-person-boxing-hub.pages.dev over HTTPS: all 21 sitemap URLs return 200; every page has one H1, a description and the correct formal-host canonical. No demo-game strings found. Robots returns 200 and permits crawl. /sitemap.xml resolves to the sitemap index. Flat guide aliases resolve to actual MDX routes. A random unknown path returns 404. The deploy marker matches source commit 27ffe9ad2bc80c569fae93cd1b72de855bbf6bba, successfully deployed as 40f8e61e-8f7a-4f56-930a-8d0301b5f381 after CI 38674616701.

Published core pages: /, /guides/beginner-guide/, /guides/combat/, /guides/mobile/, /guides/codes/. Controls, Training, Updates and Gloves are not published and are not counted as failed published-page checks.

Formal host https://firstpersonboxinghub.wiki/, /robots.txt and /sitemap.xml were actually requested; requests failed and the expected site was not observed. Registrar NS remains active; Cloudflare Zone is pending. No formal-domain success or Google indexing is claimed. www binding / redirect remains blocked with the root-domain migration.

HTTP timings in live-http-audit.json are single requests from this host, not Lighthouse scores, field Web Vitals or a global performance guarantee. Browser screenshots and final deployed UI checks are recorded separately.
