# Style guide

## Palettes (when the user has no brand colours)

Set these as CSS variables on `:root` (or on a single `.canvas` for variants).

| Name | --bg | --fg | --accent | --accent-fg | Mood |
|---|---|---|---|---|---|
| Paper (default) | `#f6f3ee` | `#16130f` | `#e4572e` | `#ffffff` | Warm, editorial |
| Ink (`.theme-dark`) | `#111214` | `#f4f2ee` | `#ffb547` | `#111214` | Premium, night |
| Field | `#eef3ea` | `#14211a` | `#2f8f4e` | `#ffffff` | Agriculture, health, nature |
| Ocean | `#eaf1f7` | `#0d1b2a` | `#1f6feb` | `#ffffff` | Tech, finance, trust |
| Clay | `#f4ebe4` | `#2a1810` | `#b4532a` | `#ffffff` | Food, craft, fashion |
| Mono | `#ffffff` | `#000000` | `#000000` | `#ffffff` | Minimal; use `.mark` for emphasis |

Keep `--muted` around 55–65% contrast of `--fg` on `--bg` and check it still passes 4.5:1 for body text.

## Brand matching

If the user gives brand colours, map them: the most saturated colour → `--accent`; a near-white or near-black → `--bg`/`--fg`. If they give a website, ask for (or read from the site) the logo, primary colour and font name. Use the brand font through Google Fonts when it's available there; otherwise the closest free match.

## Typography

- Display/headlines: a tight grotesk (default **Inter Tight** 800). Other good free choices: Manrope, Space Grotesk, DM Serif Display (for elegant brands), Archivo Black (loud retail).
- Body: Inter 400–600.
- Don't use more than two families. Don't use thin weights (< 400) on images — they disappear when compressed.
- Use `.mark` (highlight) or `.accent` on **one** key word of the headline, not several.

### Non-Latin scripts

- **Bangla:** Hind Siliguri or Noto Sans Bengali; set `lang="bn"` (base.css then increases line height and removes letter-spacing). Never apply `text-transform`, letter-spacing or italic to Bangla.
- **Arabic/Urdu:** Noto Naskh Arabic / Noto Nastaliq Urdu, add `dir="rtl"` and mirror the layout.
- **Devanagari:** Noto Sans Devanagari / Hind.
- Always run `check.py` — it reports fonts that failed to load.

## Composition

- Align to a left edge by default; centre only for short statements and quotes.
- Leave at least 30% of the canvas empty.
- Decorative shapes (circles, bars, grids) are fine if they use `--line` or `--accent` and sit behind text. Mark them `data-decor` so the checker ignores them when they bleed off the edge on purpose.
- No emoji as icons in headlines; a single emoji in a pill is OK for casual brands.
