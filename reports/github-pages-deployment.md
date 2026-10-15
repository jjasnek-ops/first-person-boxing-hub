# GitHub and Cloudflare Pages

Repository and formal HTTPS deployment: COMPLETED. Final DNS acceptance: COMPLETED.

- Repository: https://github.com/jjasnek-ops/first-person-boxing-hub, branch main.
- AnvilWiki v2.37.0 / MIT, base cab46ec2beda72cd6d4e8482ad0060bfa8d8815e.
- Pages project first-person-boxing-hub, GitHub source association verified; pnpm build, dist, Node 22.
- First source 22d42a36ee31fd2e89294a1c3bcc206096f35da8 deployed as eba4586a-8989-49e5-87b2-00029118e497.
- Latest implementation b70c6ce1728ff8699623f83e2de49cb3e4dbc739, CI https://github.com/jjasnek-ops/first-person-boxing-hub/actions/runs/38685252885 succeeded. Actual production deployment f9dfab8f-cb21-410c-ab4e-31e7e99f0c0f succeeded and formal deploy marker matches that SHA. Later report-only commits use the same pipeline.
- Formal https://firstpersonboxinghub.wiki and apex/www custom bindings are Active; Pages fallback https://first-person-boxing-hub.pages.dev.

Native push association did not initially trigger builds. Added a project-only GitHub CI main deploy hook; verified exact-commit arrival at Pages. GitHub stores only that project's hook URL in CLOUDFLARE_PAGES_DEPLOY_HOOK, without broad Cloudflare or registrar credentials. CI calls it only after required main push checks pass.

Formal audit: all 21 sitemap URLs 200 with correct metadata, robots, aliases and 404; www-to-apex and HTTP-to-HTTPS permanent redirects retain paths/query strings. See formal-http-audit.json and formal-redirect-audit.json.

Public DNS acceptance passed 14/14 at 05:24:53Z. SITE_LAUNCHED=true then enabled; final IndexNow run/result is recorded in launch-verification.md. Acceptance by a notification endpoint does not prove search-engine indexing.
