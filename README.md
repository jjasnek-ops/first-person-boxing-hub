# First Person Boxing Hub

Unofficial, source-checked English guides for [First Person Boxing on Roblox](https://www.roblox.com/games/132956556682909/First-Person-Boxing), by Can You Box?.

- Intended domain: https://firstpersonboxinghub.wiki
- Cloudflare Pages: https://first-person-boxing-hub.pages.dev
- Stack: [AnvilWiki](https://github.com/PNGTRID/AnvilWiki) v2.37.0, Astro 7, MDX, Tailwind CSS and Pagefind.
- Upstream base: cab46ec2beda72cd6d4e8482ad0060bfa8d8815e, MIT license retained.

## Development

Use Node 22.13+ and the packageManager version in package.json. Run pnpm install --frozen-lockfile, pnpm dev, and pnpm build. The build outputs dist and includes the Pagefind index.

On this Windows host, the installed pnpm 12 may need npm_config_manage_package_manager_versions=false to avoid an automatic-version bootstrap junction error. CI uses the pinned pnpm 11.1.1.

## Checks

pnpm lint, pnpm typecheck, pnpm test, pnpm check-config, pnpm check-content, pnpm check-i18n --strict-ui, pnpm build, pnpm check-links. Test scope for this production fork is documented in reports/test-scope.md. AnvilWiki demo-only contracts are retained but excluded from the production site test gate.

## Publishing and identity

GitHub main is linked to Cloudflare Pages. SITE_URL in wrangler.toml is the intended canonical domain. Ads, analytics and comments are disabled at launch. Original ring artwork and diagrams are editorial illustrations, not gameplay screenshots.

The research directory records sources, keyword evidence and publishing decisions. The reports directory records launch gates and blockers. Do not commit credentials, private sessions, or full third-party source HTML.

Unofficial fan-made guide. Not affiliated with or endorsed by Roblox, Can You Box?, or the game's developer.
