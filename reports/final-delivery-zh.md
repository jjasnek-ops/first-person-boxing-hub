# First Person Boxing Hub 交付报告

2026-10-15，Asia/Shanghai。整体状态：**BLOCKED**（正式域名接入）；网站开发、GitHub、Pages 和 GA4 自测：**COMPLETED**。

## 项目与发布

- 正式域名：https://firstpersonboxinghub.wiki，尚未接入成功，不宣称正式上线。
- 可访问版本：https://first-person-boxing-hub.pages.dev。
- GitHub：https://github.com/jjasnek-ops/first-person-boxing-hub，main。
- 已验收实现提交：27ffe9ad2bc80c569fae93cd1b72de855bbf6bba；后续报告提交不改变站点实现。
- AnvilWiki v2.37.0，基础提交 cab46ec2beda72cd6d4e8482ad0060bfa8d8815e，MIT；Astro / MDX。
- 自动部署已验证：main CI 通过后调用本站专用 Pages Hook，精确提交号到达 Pages。没有向 GitHub 上传 Cloudflare/Spaceship API 密钥。

## SEO 与窗口

- Google Suggest 共 34 个去重建议，其中 10 个与目标主题有关；不等于 10 个已验证搜索量的关键词。
- 优先意图：Roblox 游戏身份、beginner、combat、mobile、codes；controls/gloves 有线索但缺少可发布事实。
- Trends：用户历史输入显示 10 月 13–14 日上升；本次请求未独立复现。KD 0 / 1,481 的地域与周期未核实。
- Similarweb：已记录全球近 28 天可见结果；US 地域数据受套餐限制。未编造指定关键词的 US 月搜索量。
- SERP：实际浏览器样本中，first person boxing roblox 的普通网页结果包含官方站和一个独立攻略站；该样本的分析评分 2/5。其他游戏和现实拳击混杂，不能把这个评分推广到所有查询。
- 存在较早的内容竞争窗口，但需求规模、排名和流量回报均不能保证。优先发布可核验内容，后续以真实 GSC 查询迭代。

## 已发布内容

下列链接为已通过 HTTPS 验收的 Pages 版本；canonical 指向正式域名。

| 页面 | 实际 URL | 主关键词 | 证据 |
| --- | --- | --- | --- |
| 首页 | https://first-person-boxing-hub.pages.dev/ | first person boxing wiki | 官方 A 级 |
| 新手 | https://first-person-boxing-hub.pages.dev/guides/beginner-guide/ | first person boxing beginner guide | 官方事实 + 明示的编辑练习建议 |
| 战斗 | https://first-person-boxing-hub.pages.dev/guides/combat/ | first person boxing combat | 官方事实 + 编辑建议；无数值猜测 |
| 移动端 | https://first-person-boxing-hub.pages.dev/guides/mobile/ | first person boxing mobile | 官方支持声明；未冒充设备实测 |
| 兑换码核验 | https://first-person-boxing-hub.pages.dev/guides/codes/ | first person boxing codes | 有限官方来源核验，未断言全网不存在代码 |

精确 Controls、Training、Gloves、Updates 暂缓：缺少目标游戏的当前输入、系统或公告证据。没有编造按键、手套属性、奖励、更新说明，也没有声称玩过实机。About、Privacy、Terms、Copyright、Contact 和 FAQ 已按本站重写。

## 工程与验收

- 构建、lint、类型检查通过；16 个适用测试套件共 200 项通过。模板示例专用测试的排除范围见 test-scope.md，未冒称全部上游套件通过。
- 最终线上 HTTP 检查：21 个 sitemap URL 全部 200，canonical / description / 单一 H1 正确；robots、sitemap 别名、攻略别名和真实 404 通过。
- 手机实测 375×812：核心样本无整页横向溢出；表格在自身容器滚动。搜索、FAQ、菜单、目录展开与体力锚点跳转通过；补齐菜单无障碍名称。
- 原创 SVG 拳台、图示和封面；保留 MIT 许可。没有复制竞品正文或把原创图冒充官方截图。
- 线上请求耗时仅为本机单次 HTTP 样本；未测得 Lighthouse 分数或现场 Core Web Vitals，不作相关保证。
- 截图与报告已保存。测试标签的手机模拟已清除；随后浏览器级清理/保留页面操作超时，其完成状态不作保证，不影响线上部署。

## 域名

- Cloudflare Zone：pending；根域名和 www Pages 绑定也为 pending。
- 本 Zone 分配 NS：armfazh.ns.cloudflare.com、laura.ns.cloudflare.com。
- 注册商 NS 保留 launch1.spaceship.net、launch2.spaceship.net。
- 此域名已由两个 .wiki 权威服务器核实存在 DS（key tag 63051 / algorithm 13），当前链有效。目标 Cloudflare 无匹配链，直接切 NS 不兼容。
- 已按最新指令记录简化流程：已知从未启用 DNSSEC 的新域名跳过相关操作；本站已有 DS 证据，属于实际例外。未启用、关闭、恢复 DNSSEC，也未修改 DS 或 NS。
- GSC TXT 已精确写入现用 Spaceship DNS，并复制到目标 Cloudflare；根域名和 www 的目标记录已准备，未删除无关记录。
- 正式域名的站点、HTTPS 和 sitemap 实际访问尚未成功；不是普通传播等待已完成。阻塞为注册商会话过期及已知 DS 兼容处理。

## 运营与最少交接

- GSC Domain Property 所有权验证：COMPLETED。正式域名可访问后才能提交并核验 sitemap；Google 发现、收录、展示、点击尚未验证。
- GA4：COMPLETED（Pages 自测）。独立属性 559103339 / stream 16132040655 / G-P1MXKVMQVT。未同意不加载；同意后 page_view 请求 HTTP 204；正确属性 Realtime 收到 page_view 与 session_start。拒绝后刷新也不加载。均为自测，不是自然流量。
- 广告关闭。Day 3/7/14/28 计划已保存，正式上线日期未建立，未声称已创建定时任务。
- 需要用户恢复 Spaceship 浏览器登录并回复“已登录”，无需提供密码。恢复后先查看该域名实际 DNSSEC/NS 界面，确认兼容迁移能力；仍不主动启停 DNSSEC。随后继续安全 NS 切换、Active、正式 HTTPS、GSC sitemap 与正式域名 GA4 自测。

完整断点见 next-actions.md；事实证据见 ../research/evidence-ledger.md；域名证据见 domain-api-operations.md 和 dns-preflight.json；统计证据见 ga4-network-proof.json。
