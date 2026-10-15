# Visual and interaction audit

Status: COMPLETED. Actual in-app browser, production HTTPS site https://firstpersonboxinghub.wiki. Earlier local and Pages evidence is retained as baseline, not relabeled as formal-host evidence.

Desktop: 1280px viewport; document width 1265px, no horizontal overflow. Original navy/red boxing arena layout, original SVG ring illustration, legible heading, four guide cards. Home and beginner images loaded; one H1 per inspected page. No borrowed game screenshot or official logo.

Formal-host tab-scoped phone emulation: 375×812 on Home, Beginner and Combat. Each measured innerWidth=375 and document.scrollWidth=375, one H1 and loaded images. Tables scroll within their own container. Unsupported Controls content is withheld, not represented as tested on a game device. Website responsiveness does not prove game control bindings.

Actual interactions passed: Start boxing opens the native beginner URL; FAQ answer expands; mobile Menu opens and exposes Guides; TOC expands; stamina anchor lands around y=79.9 below the sticky header. Pagefind query stamina returns four relevant articles; selecting the combat result opens the proper fragment. Production UI/runtime/worker cache version f88386cfe8 matches (pagefind-formal-proof.json). Fixed the content-independent inherited cache key and added one focused regression test.

Formal screenshots: screenshots/formal-home-desktop.png, formal-home-mobile.png, formal-beginner-mobile.png, formal-beginner-desktop.png, formal-search-results.png. Earlier phone/menu/TOC samples: live-home-mobile.png and live-home-desktop.png.

Formal-host GA4 consent, actual page_view HTTP 204 and correct-property Realtime receipt passed; details in gsc-ga4-status.md. These visits are self-tests.

Cleanup completed: phone metrics explicitly cleared and default 1280px width confirmed. Formal website, GA4 and GSC output tabs retained for the user. Earlier browser cleanup/network timeouts were recovered and do not remain an open launch blocker. No Lighthouse or field Core Web Vitals score is claimed.
