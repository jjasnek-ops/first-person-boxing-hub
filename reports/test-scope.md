# Site test scope

The initial complete upstream suite was executed: 350 passed, 23 failed, 1 skipped, plus 3 module-load failures. Failures were caused by fixtures that assume AnvilWiki's own marketing pages, demo codes, Japanese locale, original authors and demo Wrangler identity remain present. Those resources are intentionally removed by the template's official apply-template flow.

For this production fork, eight template/demo-only suites are excluded explicitly in vitest.config.ts; their source is preserved. The remaining 17 suites are the site gate. Three assertions were adjusted for the English-only configuration and current game name. Typecheck covers application and scripts; Vitest executes runtime tests separately. No runtime locale was re-enabled to satisfy a demo fixture.

A regression case covers pathname normalization preserving query strings and fragment targets, after browser inspection found the template appended a slash after an anchor.

This scope does not claim the excluded template-maintainer suites passed. The inherited E2E template and ops-package jobs are outside this single-site launch gate.

Current inventory: 25 suites, 17 applicable / 8 explicitly excluded; 201 tests passed in the applicable gate. New pagefind-cache regression verifies that either UI changes or generated content-manifest changes invalidate the cache version. The initial inventory CI failure was corrected in AGENTS.md; final implementation CI 38685252885 succeeded.
