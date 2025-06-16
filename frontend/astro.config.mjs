// @ts-check
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';

import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
  base: "/crawlers/",
  outDir: "../dist",
  site: 'https://nicolascuadram.github.io/crawlers/',
  integrations: [mdx(), sitemap()],

  vite: {
    plugins: [tailwindcss()],
  },
});