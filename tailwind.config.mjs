/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: { navy: { 50: '#f3f7fb', 100: '#e5eef7', 600: '#174a7c', 700: '#103a63', 800: '#0b2b4b', 900: '#081f36' } },
      fontFamily: { sans: ['Inter', 'ui-sans-serif', 'system-ui', 'sans-serif'], serif: ['Georgia', 'Cambria', 'serif'] }
    }
  },
  plugins: []
};
