# Visual sample audit

Status: COMPLETED for local sample. Browser: real in-app browser, local production build at http://127.0.0.1:4323. Screenshots: screenshots/home-mobile.png and screenshots/beginner-mobile.png. Desktop screenshot observed at 1280px; dark navy arena style, red accents, original ring illustration, legible large heading, four actionable guide cards.

The high-level viewport override did not change the measured desktop innerWidth, so it was not accepted as a mobile test. Tab-scoped DevTools emulation produced innerWidth=375 and document.scrollWidth=375 on Home, Beginner and Combat. Mobile screenshots use the actual 375×812 clipping rectangle. Controls page is withheld, not represented as tested.

Home H1 count 1; images loaded. Beginner H1 count 1; editorial diagram loaded. Combat H1 count 1; tables fit a 343px content column and overflow only within the table scroll container. The stamina anchor exists and internal anchor URLs are preserved after the pathname fix.

Pagefind search dialog opens; stamina returns four relevant article results. Browser warning/error log was empty. Final Pages UI checks completed: FAQ answer expands; phone menu opens and Guides link is visible; article TOC expands and the stamina heading lands at y=79.875 under the sticky header with the correct fragment. Menu summary now has accessible name Menu after discovering the inherited icon-only summary was unlabeled. Latest mobile screenshot: screenshots/live-home-mobile.png. Desktop screenshot: screenshots/live-home-desktop.png. No document overflow at 375px. Temporary viewport overrides are cleared after QA. Original brand icon replaces the inherited hammer. No game screenshot or official logo used.

GA4 consent tested on the actual Pages deployment: before consent no gtag script, acceptance sends the correct page_view (HTTP 204) and Realtime receives it. An independent immutable-deployment origin tested Decline plus reload: banner stays dismissed and no gtag script loads. These are self-tests, not organic visitors.

Cleanup note: tab-scoped mobile metrics were explicitly cleared on both test tabs. The later browser-wide viewport reset/handoff batch timed out, and a single inventory recovery also timed out. Completion of that browser-wide cleanup/tab marking is unverified; no further UI retries. This does not affect deployed website settings.
