import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  site: 'https://saitaliuymaz.com',
  output: 'static',
  integrations: [tailwind({ applyBaseStyles: false })],
});
