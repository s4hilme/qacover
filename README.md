# qacover.com — production build

This repository contains the **built production output** of https://qacover.com exactly as deployed on Netlify on 2026-10-18. It is **not editable source code** (it is a compiled Vite/React bundle).

- Every file was downloaded from the live site. The only change: a hard-coded third-party API token in `assets/index-FpVXcGDL.js` was replaced with an empty string before publishing.
- `_redirects` (SPA fallback) and `_headers` are not publicly fetchable, so they were recreated from the project's config.

## Netlify
- Build command: *(none)*
- Publish directory: `.` (repo root)
