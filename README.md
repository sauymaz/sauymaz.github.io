# Sait Ali UYMAZ - Academic Website

Static academic personal website for Assoc. Prof. Dr. Sait Ali UYMAZ, built with Astro, TypeScript, and Tailwind CSS.

## Requirements

- Node.js 20 or later
- npm

Install the current Node.js LTS release from [nodejs.org](https://nodejs.org/). Node.js includes npm.

## Local setup

### Windows

Install Node.js 20+ using the official Windows installer, then open PowerShell in this project folder:

```powershell
npm install
npm run dev
```

### macOS

Install Node.js 20+ using the official macOS installer or a package manager such as Homebrew (`brew install node`), then run:

```bash
npm install
npm run dev
```

### Linux

Install Node.js 20+ through your distribution's NodeSource packages, version manager, or the official Linux binaries. Then, from the project directory, run:

```bash
npm install
npm run dev
```

Astro starts a local development server and prints its URL (normally `http://localhost:4321`).

## Production build

```bash
npm run build
npm run preview
```

The static output is generated in `dist/`. `npm run build` runs Astro's type/content checks before creating the production site.

## Project structure

```text
src/
  components/   Reusable interface components
  content/      Long-form Markdown content
  data/         JSON data used by pages
  layouts/      Shared BaseLayout, Header, and Footer
  pages/        Static Astro routes
  styles/       Global Tailwind styles
```

All routes are static and use the shared `BaseLayout`, which provides the common header, footer, and page SEO metadata.

## Content maintenance

Structured content is stored in `src/data/`:

- `profile.json` — identity, affiliation, contact, and academic profiles
- `research-areas.json`, `publications.json`, `projects.json`, `courses.json` — site sections
- `aaa-info.json`, `aaa-citations.json`, `aaa-code.json` — Artificial Algae Algorithm resources

The publication, project, course, code, and citation records currently include clearly marked placeholder data. Replace them with verified records before public release. Extended Markdown material can live in `src/content/`.

## GitHub Pages deployment

1. Commit and push the project to the `main` branch on GitHub.
2. In the repository's **Settings > Pages**, choose **GitHub Actions** as the build and deployment source.
3. The included `.github/workflows/deploy.yml` workflow runs on each push to `main` (and can be started manually). It uses Node.js 20, runs `npm ci` and `npm run build`, then deploys the generated `dist/` directory.
4. After the first successful run, open the repository's **Actions** or **Pages** page to find the deployed URL.
5. If deploying to a project site such as `https://username.github.io/repository/`, add `base: '/repository'` in `astro.config.mjs`. Do not add it for a user/organization site or the custom domain.
6. Configure `saitaliuymaz.com` in the GitHub Pages custom-domain setting and set the necessary DNS records at the domain provider.

The current `site` value in `astro.config.mjs` is already set to `https://saitaliuymaz.com`, and the project uses Astro static output, so it does not require a server or database.
