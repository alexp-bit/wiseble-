# wiseble-site

Marketing site for **wiseble.ai** — agent-payable interface for existing data APIs.

## Stack

- Plain HTML5 + Tailwind CSS via CDN (no build step)
- Inter + Space Grotesk + Material Symbols (Google Fonts)
- Vanilla JS for mobile menu and code-block copy buttons

Design system: **Wiseble Virtual System** — dark console aesthetic, `#000000` background, `#FFFFFF` text, `#FF5C00` accent. Reference: `../stitch_wiseble_design_framework/DESIGN.md`.

Content source: `../WISEBLE/wiseble_website_content_v2.md`.

## Pages

| Path | File | Status |
|---|---|---|
| `/` | `index.html` | shipped |
| `/providers` | `providers.html` | shipped |
| `/developers` | `developers.html` | shipped |
| `/pricing` | `pricing.html` | shipped |
| `/partner` | `partner.html` | shipped (form posts to `mailto:`; replace with Tally/Formspree) |
| `/about` | `about.html` | shipped |
| `/use-cases` | `use-cases/index.html` | shipped |
| `/use-cases/<slug>` | `use-cases/<slug>.html` | 10 detail pages, generated |

## Local development

No install step. Open files directly:

```bash
open index.html
```

For a proper local server (clean URLs, etc.):

```bash
npx serve .
# or
python3 -m http.server 8000
```

## Shared assets

- `assets/styles.css` — design tokens, components, type scale
- `assets/tailwind-config.js` — Tailwind CDN config
- `assets/app.js` — burger menu, code-copy buttons
- `assets/favicon.svg`

Each HTML page includes:
```html
<script src="https://cdn.tailwindcss.com"></script>
<script src="assets/tailwind-config.js"></script>
<link rel="stylesheet" href="assets/styles.css" />
```
(Use `../assets/...` from `use-cases/`.)

## Use-case generator

10 use-case detail pages share a single template. Edit `_scripts/generate-use-cases.py` and run:

```bash
python3 _scripts/generate-use-cases.py
```

## Deploy (Vercel)

```bash
vercel       # preview
vercel --prod
```

`vercel.json` configures:
- `cleanUrls` — `/providers` resolves to `providers.html`
- `Cache-Control` headers for `/assets/*`

Production: `wiseble.ai` (TBD — DNS to be configured).

## Forms & analytics

- `/partner` form: currently `mailto:`. Replace with Tally embed or Formspree endpoint when ready.
- Plausible analytics: snippet commented out in each `<head>`. Uncomment after DNS is live.
- Custom events: `code_snippet_copied`, `partner_form_submitted` (TODO once form backend is set).

## Contact

`partners@wiseble.ai` · `hello@wiseble.ai` · `alex@wiseble.ai`
