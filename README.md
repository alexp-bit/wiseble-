# wiseble-site

Marketing site for **wiseble.ai** — agent-payable interface for existing data APIs.

## Stack

- Plain HTML5 + Tailwind CSS (via CDN, no build step)
- Inter + Space Grotesk + Material Symbols (Google Fonts)
- Vanilla JS for mobile menu and code-block copy buttons

Design system: `Wiseble Virtual System` — dark console aesthetic, `#000000` background, `#FFFFFF` text, `#FF5C00` accent. Reference: `../stitch_wiseble_design_framework/DESIGN.md`.

Content source: `../WISEBLE/wiseble_website_content_v2.md`.

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

## Pages

| Path | Status |
|---|---|
| `/` (`index.html`) | shipped — full v2 content |
| `/providers` | TODO |
| `/developers` | TODO |
| `/use-cases/` | TODO (10 detail pages + index) |
| `/pricing` | TODO |
| `/partner` | TODO (Tally embed) |
| `/about` | TODO |

## Deploy

Deployed on Vercel. Production: `wiseble.ai` (TBD).

```bash
vercel       # preview
vercel --prod
```

`vercel.json` configures clean URLs (`/providers` → `providers.html`).

## Forms

`/partner` form is a Tally embed (env-gated). Custom analytics events:

- `partner_form_submitted`
- `code_snippet_copied`
- `pricing_page_viewed`

## Contact

`partners@wiseble.ai` · `hello@wiseble.ai`
