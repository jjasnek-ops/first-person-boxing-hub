# First Person Boxing Hub 正式交付报告

2026-10-15，Asia/Shanghai。网站已在正式域名部署，最终验收状态：**COMPLETED**。以下为实际执行与验证结果。

## 1. 项目

- 正式站：https://firstpersonboxinghub.wiki。
- GitHub：https://github.com/jjasnek-ops/first-person-boxing-hub，main。
- 已验收实现提交：b70c6ce1728ff8699623f83e2de49cb3e4dbc739。后续报告提交走同一 CI/Pages 管道，不改变站点实现。
- AnvilWiki v2.37.0，基础 cab46ec2beda72cd6d4e8482ad0060bfa8d8815e，MIT；Astro / MDX。
- Pages：https://first-person-boxing-hub.pages.dev；实现部署 f9dfab8f-cb21-410c-ab4e-31e7e99f0c0f 成功，正式域名部署标记与实现 SHA 相符。
- main CI 通过后调用本站专用 Pages Hook。GitHub 没有上传 Cloudflare/Spaceship 广域 API 凭据。

## 2. SEO

- Google Suggest 共 34 个去重建议，其中 10 个主题相关；不等于已验证搜索量的关键词数。
- 优先长尾：first person boxing wiki、beginner guide、combat、mobile、codes。精确 controls/gloves 缺少当前游戏事实。
- Trends：用户历史输入显示 10 月 13–14 日上升，本次未独立复现；KD 0 / 1,481 的地域和周期未核实。
- Similarweb：实际查询并保存全球近 28 天可见观察；US 数据受套餐限制，状态 BLOCKED。未编造 US 月搜索量。
- SERP：实际 first person boxing roblox 浏览器样本包含官方站与独立攻略站，该样本分析评分 2/5；其他查询混有不同游戏/现实拳击，不能推广为全词竞争结论。
- 可先占据可核验攻略的内容窗口，但需求、排名及回报均待本站真实 GSC 数据验证。证据见 ../research/evidence-ledger.md。

## 3. 内容

以下已发布并在正式域名验收，状态 COMPLETED。

| 页面 | 正式 URL | 主关键词 | 证据等级与边界 |
| --- | --- | --- | --- |
| 首页 | https://firstpersonboxinghub.wiki/ | first person boxing wiki | A，官方游戏身份/机制 |
| 新手 | https://firstpersonboxinghub.wiki/guides/beginner-guide/ | first person boxing beginner guide | A + 明示编辑练习建议 |
| 战斗 | https://firstpersonboxinghub.wiki/guides/combat/ | first person boxing combat | A + 编辑建议，无猜测数值 |
| 移动端 | https://firstpersonboxinghub.wiki/guides/mobile/ | first person boxing mobile | A，官方平台支持；未冒充游戏设备实测 |
| 兑换码核验 | https://firstpersonboxinghub.wiki/guides/codes/ | first person boxing codes | A，有限来源核验；不宣称全网没有代码 |

About、Privacy、Terms、Copyright、Contact、FAQ 和标签索引按本站重写。sitemap 共 21 个 URL；22 个 HTML 包含真实 404。

Controls / Gloves 状态 BLOCKED，Training / Updates 为 NOT_STARTED：缺少可归属当前游戏的输入、属性、训练系统或更新公告证据。没有编造按键、触屏布局、手套数值、奖励、兑换码或实机体验。页面矩阵与已发布 URL 一致。

## 4. 工程与验收

- 构建、lint、类型和内容/配置/链接/重品牌检查通过。17 个适用套件、201 个测试通过；8 个上游模板专用套件明确排除，未声称其通过。最新实现 CI 38685252885 成功。
- 正式线上 21/21 sitemap 页面均 200，canonical、description 和单一 H1 正确；robots、sitemap 别名、攻略别名、真实 404 通过。
- 正式站实际浏览器手机模拟 375×812，首页/新手/战斗无整页横向溢出，图片加载、H1 正常；表格在自身容器滚动。桌面 1280px 正常。测试视口已清除并确认恢复。
- 搜索 stamina 返回四个相关结果，跳转体力段落正确；菜单、FAQ、目录操作通过。修复了 Pagefind 仅按 UI 计算缓存版本、内容更新不能失效的问题，并加入针对性回归测试。
- 原创 SVG 拳台/图示/封面，保留 MIT 许可与非官方声明；未复制竞品正文，也未把原创图冒充官方截图。
- HTTP 耗时为本机单次样本，不代表全球性能。未测得 Lighthouse 或现场 Core Web Vitals，不作分数保证。
- 证明：formal-http-audit.json、formal-redirect-audit.json、pagefind-formal-proof.json，以及 screenshots/formal-home-desktop.png / formal-home-mobile.png / formal-beginner-mobile.png。

## 5. 域名

- Cloudflare Zone Active；本 Zone 的 NS 为 armfazh.ns.cloudflare.com、laura.ns.cloudflare.com。
- Spaceship 已保存上述确切 NS，注册局委派已核实。
- 此域名原有 DNSSEC 和 DS，不适用从未开启 DNSSEC 的新域名捷径。收到用户“授权此次处理并继续上线”后，仅关闭该域名现有 Spaceship DNSSEC、撤销旧 DS；两个 .wiki 权威服务器确认无 DS 后切换 NS。未自动重新启用或恢复 DNSSEC。
- 已记录旧递归 DS 缓存造成的验证错误，并保留最终公共 DNS 门禁，未把注册局撤销等同全球缓存清空。最终结果：COMPLETED，05:24:53Z 的 Google/Cloudflare 共 14 项验证通过，无旧 DS 或 SERVFAIL；不保证全球所有缓存同时到期。
- 根域名和 www Pages 绑定 Active；Universal 证书 Active，HTTPS 浏览器无警告。
- www 永久跳到 HTTPS 根域名，HTTP 升级 HTTPS，路径及查询参数保留，四项线上测试通过。
- 正式站、robots、XML sitemap 和主要内容实际可访问。无须再次登录、提供密码或重复授权已批准的操作。

## 6. 运营

- GSC：正确 Domain Property 已验证，验证 TXT 保留；sitemap-index.xml 为 Success，Last read Oct 15，当前发现页数 0。首页与新手指南的 Request indexing 均获确认。
- Google 实际索引：检查时为 not indexed / unknown to Google；请求已受理不等于已收录。未声称展示、点击或自然流量。
- GA4：独立属性 559103339 / stream 16132040655 / G-P1MXKVMQVT。未同意不加载；同意后正式首页与新手指南 page_view 均 HTTP 204，正确属性 Realtime 收到两条页面路径。拒绝后刷新也不加载。所有数据是自测。
- IndexNow：DNS 门禁通过后已启用 SITE_LAUNCHED；最终发布通知正在核验，结果另附；不等于 Google 索引。
- 广告关闭。Day 3/7/14/28 维护日期为 10 月 18 日、10 月 22 日、10 月 29 日、11 月 12 日（中国时间）；已保存计划，没有声称创建定时任务。
- 用户待办：本次已授权上线无需新增凭据或权限；后续按维护计划检查真实收录和搜索数据。本次公共 DNS 等待已结束，未遗留需要用户处理的上线阻塞。

当前总表见 current-delivery-status.md；完整验收见 launch-verification.md；运维过程见 domain-api-operations.md；GSC/GA4 见 gsc-ga4-status.md。
