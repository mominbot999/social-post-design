---
name: social-post-design
description: Use when asked to design a social media graphic — Instagram/Facebook post, carousel, story, ad creative, LinkedIn image, YouTube thumbnail, Facebook cover, announcement, offer or quote card. Produces one self-contained HTML file at exact platform sizes, self-checks it, and exports PNG/JPG.
---

# Social post design

Design social media graphics as **one self-contained HTML file** where each `<section class="canvas …">` is one image at the platform's exact pixel size. Then check it and export to PNG.

The look is editorial and confident: big type, one accent colour, lots of space, no clip-art, no drop shadows, no gradients-everywhere, no stock "business people" imagery.

## Workflow

1. **Understand the brief.** Find out (ask once, briefly, only what's missing): the platform(s), the one message, the call to action, brand colours/fonts/logo, language, and real facts (prices, dates, numbers). Never invent prices, statistics, testimonials or dates — use clear placeholders like `[PRICE]`.
2. **Pick the format(s)** from `references/formats.md`. If the user says "a post", default to `portrait` (1080×1350) — it takes the most feed space on Instagram and Facebook.
3. **Pick a layout** from the index below and read only that layout's file in `references/layouts/`.
4. **Write the HTML** starting from `assets/template.html`. Inline the entire `assets/base.css` into `<style>`, then add theme overrides (`--accent`, `--bg`, fonts) and layout-specific CSS. Size everything in `var(--u)` (1% of canvas width) so it scales.
5. **Self-check:** run `python3 scripts/check.py design.html` and fix every ✗ error. Treat "small text" and "story unsafe zone" warnings as errors unless there's a reason.
6. **Export:** `python3 scripts/export.py design.html` (add `--scale 2` for crisp retina output). Look at the PNG before delivering — if it doesn't look good as a thumbnail on a phone, fix it.
7. **Deliver** the HTML and the PNG(s). Offer 2–3 variants (e.g. light/dark, different headline) when the user is choosing a direction.

If the scripts can't run (no Python/Playwright), deliver the HTML and tell the user to open it in a browser and screenshot each canvas, or run the export script locally.

## Layout index

| Layout | Use for | File |
|---|---|---|
| Statement | Announcements, big news, one-line messages | `layouts/statement.md` |
| Offer | Product + price, discount, sale | `layouts/offer.md` |
| Stat | One big number with context | `layouts/stat.md` |
| List | Tips, steps, "5 things…" | `layouts/list.md` |
| Carousel | Multi-slide stories and tutorials | `layouts/carousel.md` |
| Quote | Quotes from the brand's own people or a real, attributed customer | `layouts/quote.md` |
| Split | Before/after, this vs that, problem → solution | `layouts/split.md` |
| Event | Webinars, launches, store openings, dates | `layouts/event.md` |
| Hiring | Job openings | `layouts/hiring.md` |
| Product spotlight | Feature a product photo with 3 key specs | `layouts/product.md` |
| Story CTA | Full-screen story with a tap/swipe action | `layouts/story.md` |
| Thumbnail | YouTube / video covers | `layouts/thumbnail.md` |

## Rules that make it look professional

- **One idea per image.** If you need more, make a carousel.
- **Hierarchy in three steps max:** eyebrow → headline → one supporting line (+ brand/CTA).
- **Headline ≤ 8 words**, readable in a 2-second scroll. Body text ≥ 2.2% of canvas width (the check enforces this).
- **One accent colour** used on ≤ 15% of the area. Everything else is `--bg`, `--fg`, `--muted`.
- **Keep the safe area.** Nothing important within `--safe` padding of the edge; stories keep text out of the top 200px and bottom 300px (UI covers them).
- **Contrast:** text must pass WCAG AA (4.5:1 for body, 3:1 for large headlines). Never put text on a busy photo without a solid panel behind it.
- **Brand:** if the user gives a website or brand colours, use them; otherwise pick a palette from `references/style.md`.
- **Photos:** only use images the user provides (or plain shapes). Never hot-link random images; leave an `.photo` placeholder block with a note instead.
- **Language:** for Bangla or other non-Latin scripts set `lang` on the element and use a font that supports it (Hind Siliguri / Noto Sans Bengali for Bangla). See `references/style.md`.
- **Ads:** keep text short; avoid claims platforms reject ("guaranteed", before/after body images, personal attributes like "Are you overweight?").
