# GitHub and Cloudflare Pages

Status: COMPLETED for repository and Pages deployment; BLOCKED for formal-domain launch.

- Repository: https://github.com/jjasnek-ops/first-person-boxing-hub
- Branch: main
- First published source: 22d42a36ee31fd2e89294a1c3bcc206096f35da8
- AnvilWiki base: cab46ec2beda72cd6d4e8482ad0060bfa8d8815e (v2.37.0, MIT).
- GitHub CI https://github.com/jjasnek-ops/first-person-boxing-hub/actions/runs/38670356503 succeeded. IndexNow is deliberately gated until SITE_LAUNCHED=true, so it does not notify an unlaunched formal host.
- Pages project: first-person-boxing-hub; actual GitHub source association confirmed by API.
- Build: pnpm build; output dist; Node 22.
- First deployment: eba4586a-8989-49e5-87b2-00029118e497; production, main, exact first source commit; all stages successful at 2026-10-15T02:20:39Z (10:20 Asia/Shanghai).
- URL: https://first-person-boxing-hub.pages.dev
- Immutable deployment URL: https://eba4586a.first-person-boxing-hub.pages.dev

Native push events did not start builds for the first two commits. Added the project-only github-ci-main hook following Cloudflare's documented Pages workflow. GitHub stores only its URL in CLOUDFLARE_PAGES_DEPLOY_HOOK; no account token or registrar credential was uploaded. CI calls it after all main push gates pass. Commit f7bf7164448e3c9836ba8ec152078095d0a5f9ea passed CI run 38672795922, including the trigger. Pages deployment 3a8780ee-9e96-45d6-8e12-6d4025466198 reports source deploy_hook, that exact commit and successful stages. CI-to-Pages deployment is verified.

Remote HTTP audit verifies 21 sitemap URLs, metadata, robots, aliases, 404 and deployed commit marker. See live-http-audit.json. Pages TLS works; formal-domain DNS/HTTPS remains separate and blocked.

GA4 commit cf15c0ba88695dde4e1d9937f43d02ab59494197 deployed successfully as 6d04b1c7. Final implementation commit 27ffe9ad2bc80c569fae93cd1b72de855bbf6bba (accessible menu label) passed CI 38674616701 and deployed successfully as 40f8e61e-8f7a-4f56-930a-8d0301b5f381. Final audit matches that marker. Subsequent report-only commits use the same verified pipeline.
