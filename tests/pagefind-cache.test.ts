import { describe, expect, it } from 'vitest';

const { pagefindCacheVersion } = await import('../scripts/transpile-pagefind.mjs') as {
  pagefindCacheVersion: (ui: string, entry: string) => string;
};

describe('Pagefind cache generation', () => {
  it('invalidates content-only rebuilds even when the UI bundle is unchanged', () => {
    const ui = 'unchanged search UI';
    const firstIndex = '{"languages":{"en":{"hash":"index-before"}}}';
    const updatedIndex = '{"languages":{"en":{"hash":"index-after"}}}';
    const before = pagefindCacheVersion(ui, firstIndex);
    expect(pagefindCacheVersion(ui, firstIndex)).toBe(before);
    expect(pagefindCacheVersion(ui, updatedIndex)).not.toBe(before);
    expect(pagefindCacheVersion('updated UI', firstIndex)).not.toBe(before);
  });
});
