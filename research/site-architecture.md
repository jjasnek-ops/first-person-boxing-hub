# Site architecture

AnvilWiki's native content route is /guides/{slug}/. Keep that architecture rather than rewriting the content engine for flat URLs. Flat /codes, /mobile, /combat and /beginner-guide redirect permanently to the native article URLs. /controls is withheld and returns a genuine 404 until supported content is ready.

Home → Guides → Beginner / Combat / Mobile / Codes status. Supporting pages: About, FAQ, Contact, Privacy Policy, Terms of Service, Copyright, recent and tag navigation. English only. Search indexes the four article bodies. No duplicate localized fallback pages are published.

Sitemap index is /sitemap-index.xml; /sitemap.xml redirects to it. Canonical host is firstpersonboxinghub.wiki. No invented updates, glove system, training rewards or code strings.
