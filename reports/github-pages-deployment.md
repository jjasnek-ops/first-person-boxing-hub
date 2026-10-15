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

The first push did not immediately produce a Pages deployment, so a documented API deployment request triggered the Git-connected build. This was a source build, not an untracked local upload. Future push-trigger behavior must be confirmed on the follow-up report commit.

Remote HTTP audit verifies 21 sitemap URLs, metadata, robots, aliases, 404 and deployed commit marker. See live-http-audit.json. Pages TLS works; formal-domain DNS/HTTPS remains separate and blocked.
