# Technical audit

Status: COMPLETED for local build. AnvilWiki/Astro static output and MDX retained. English-only runtime configuration. Code/config/content remain separate; necessary generic fixes are the query/fragment-preserving URL normalizer, configurable FAQ heading level, original hero image slot, brand favicon and site-specific legal content configuration.

- pnpm build: passed, 22 HTML pages including the 404.
- pnpm lint: passed.
- pnpm typecheck: 0 errors / warnings / hints over 137 application/script files.
- pnpm test: 16 applicable suites, 200 assertions passed. Excluded upstream demo suite scope is explicit in test-scope.md.
- pnpm check-content / check-config / check-i18n --strict-ui: passed.
- pnpm check-links: 411 links / 22 HTML pages, all resolve.
- pnpm check-sitemap http://127.0.0.1:4323: 21 URLs returned 200.
- pnpm template-audit: 14/14 clean rebranding checks.

Canonical/SITE_URL configured to https://firstpersonboxinghub.wiki; OG assets generated locally. Robots permits crawl and names the real sitemap-index.xml. /sitemap.xml is a permanent redirect alias. No Japanese pages or fake language variants; sitemap derives from published pages. Four articles have distinct titles, H1 and descriptions. Structured data comes from real visible content; no code-reward schema or fabricated Person author is emitted.

No separate check:test script is required. No Lighthouse score or Core Web Vitals claim is made until actually measured. Live-domain status is separate in launch-verification.md. Exact Controls/Training/Updates/Gloves candidates are withheld, not failed published pages.
