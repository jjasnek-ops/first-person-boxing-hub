/** Site-specific editorial and legal copy; launch configuration, 15 October 2026. */
export const correctionUrl = 'https://github.com/jjasnek-ops/first-person-boxing-hub/issues';
export const legalPages: Record<string, {intro: string; sections: {heading: string; paragraphs: string[]}[]}> = {
  about: {intro:'First Person Boxing Hub is an independent English-language guide to First Person Boxing, the Roblox experience by Can You Box?.',sections:[
    {heading:'What we cover',paragraphs:['Beginner practice, officially described combat mechanics, mobile access and code verification. We withhold exact keybinds, numerical stats and other systems when reliable evidence is missing.']},
    {heading:'How we verify information',paragraphs:['Official Roblox listings and APIs come first, followed by attributable developer announcements and clear game footage. Other guide sites and community reports are leads rather than proof. Guides state their check dates and evidence scope.','Our launch guides were prepared with AI assistance and source verification. We have not played a live session. Practice drills are editorial suggestions, not measured mechanics. We do not invent codes, damage values, timing windows or patch notes.']},
    {heading:'Freshness and corrections',paragraphs:['A check date records a source review, not firsthand testing. An API update timestamp is not a patch announcement. Send the affected URL, original source, platform and date when reporting a correction.']},
    {heading:'Independent identity',paragraphs:["Unofficial fan-made guide. Not affiliated with or endorsed by Roblox, Can You Box?, or the game's developer."]},
    {heading:'Template and artwork',paragraphs:['Built with AnvilWiki v2.37.0 (MIT), Astro and MDX. Our ring illustration, diagrams and cover art are original editorial graphics, not gameplay screenshots or official game branding.']}
  ]},
  'privacy-policy': {intro:'This policy describes First Person Boxing Hub at launch on 15 October 2026.',sections:[
    {heading:'Browsing this website',paragraphs:['This is a static website with no registration, checkout or personal-data submission form. Cloudflare hosts the site and may process request details such as IP address, URL and browser information to deliver and protect it.']},
    {heading:'Advertising and analytics',paragraphs:['Advertising, Cloudflare Web Analytics, embedded video and comments are disabled. Google Analytics 4 loads only after you accept the cookie banner. It measures visits and interactions such as page paths, scrolls and outbound clicks; Google may process browser, device and network information. Declining leaves these analytics scripts unloaded. Do not put personal information in URLs or search queries.','Your cookie choice is stored in your browser. To change it, clear this website\'s local storage and cookies in your browser settings and reload. Google describes its processing at https://policies.google.com/technologies/partner-sites.']},
    {heading:'Local storage and search',paragraphs:['Theme preferences and interface choices may be stored locally in your browser. Pagefind search uses an index served by this website; search queries are not sent to a third-party search provider. You can clear local storage in your browser settings.']},
    {heading:'External links and contact',paragraphs:['Linked destinations such as Roblox and GitHub operate under their own policies. GitHub Issues is our public correction channel; do not post passwords, cookies or sensitive personal information there. Use that channel for questions about this website.']}
  ]},
  'terms-of-service': {intro:'This website provides independent informational guides. It does not operate the Roblox experience or provide account services.',sections:[
    {heading:'Accuracy and scope',paragraphs:['Game interfaces and features can change. Each guide states its sources and limitations. Verify important current details in the game or with the developer. Practice suggestions do not guarantee wins or rewards.']},
    {heading:'Content and attribution',paragraphs:['You may read and link to these guides. Original writing and graphics are credited to First Person Boxing Hub. AnvilWiki code retains its MIT license. Third-party content and trademarks remain subject to their respective owners\' rights.']},
    {heading:'External services',paragraphs:['Roblox controls game access, accounts and purchases. External links are provided for reference. We do not distribute cheats, modified clients, code generators or account tools.']},
    {heading:'Corrections',paragraphs:['Report errors with an affected URL and original evidence through the public channel below. Do not send credentials or private account information.']}
  ]},
  copyright: {intro:'Game names identify the subject of this unofficial fan-made guide.',sections:[
    {heading:'Original work and template',paragraphs:['Original writing, ring artwork, diagrams and branded covers are created for this site. They are not official artwork or gameplay screenshots. AnvilWiki is used under MIT; its license is preserved in the repository.']},
    {heading:'Trademarks',paragraphs:['Roblox and game-related names, trademarks and assets belong to their respective owners. We claim no affiliation, endorsement or ownership of those rights. We do not reproduce competitor prose or host copied gameplay videos.']},
    {heading:'Copyright concerns',paragraphs:['Use the public correction channel below to identify the affected URL, the work concerned and the basis of a request. Avoid posting sensitive personal information in a public issue.']}
  ]},
  contact: {intro:'Use this project\'s GitHub Issues channel below for source corrections and website questions.',sections:[
    {heading:'Useful correction evidence',paragraphs:['Include the affected URL, an original source, date, platform and a short explanation. For controls, clear footage of the current game interface is more useful than an unsupported key list.']},
    {heading:'Account privacy',paragraphs:['Do not post Roblox passwords, session cookies, email codes or private account details. This wiki does not handle Roblox account or payment support; use Roblox\'s official support for those matters.']},
    {heading:'Who operates what',paragraphs:['Can You Box? develops the game. This wiki is independent. The official Roblox link opens the game listing and is not a contact route for the wiki.']}
  ]}
};
