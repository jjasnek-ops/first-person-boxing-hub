import { fileURLToPath } from 'node:url';
import { defineConfig } from 'vitest/config';

export default defineConfig({
  resolve: {
    alias: {
      // fileURLToPath 还原 percent-encoding；`.pathname` 在含中文的目录下会得到 %E7... 导致模块解析失败
      '~': fileURLToPath(new URL('./src/', import.meta.url)),
    },
  },
  test: {
    environment: 'node',
    include: ['tests/**/*.test.ts'],
    // Upstream template/demo contracts require intentionally removed marketing,
    // Japanese demo codes and initialization fixtures. Preserve them in Git,
    // but keep this single-game site's gate scoped to its applicable suites.
    exclude: ['tests/{apply-template,changelog,codes-consistency,community-digest,handbook,landing-paths,redirects,workflows}.test.ts'],
  },
});
