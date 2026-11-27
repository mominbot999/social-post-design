# Formats

| Class | Size (px) | Ratio | Use |
|---|---|---|---|
| `portrait` | 1080 × 1350 | 4:5 | **Default feed post** — Instagram, Facebook, LinkedIn. Takes the most screen space. |
| `square` | 1080 × 1080 | 1:1 | Feed post when the grid matters; works everywhere. |
| `story` | 1080 × 1920 | 9:16 | Stories, Reels covers, TikTok, WhatsApp status, full-screen mobile ads. |
| `landscape` | 1200 × 628 | ~1.91:1 | Link previews, LinkedIn/X shared images, Facebook link ads. |
| `thumb` | 1280 × 720 | 16:9 | YouTube thumbnails, video covers, slides. |
| `cover` | 1640 × 624 | ~2.63:1 | Facebook page cover. Keep text in the centre ~1100 px: mobile crops the sides and the profile picture covers the bottom-left. |

## Safe zones

- Feed formats: `--safe` = 7% padding. Keep logos and text inside it.
- `story`: top 200 px (profile bar) and bottom 300 px (reply bar / CTA sticker) are covered by the app. The `story` class already pads 220 px top and 340 px bottom.
- `thumb`: YouTube puts the video length in the bottom-right corner — keep that corner empty.

## Carousels

A carousel is several `.canvas` elements of the **same format** in one file. Give each a `data-name` like `slide-01` so exports sort correctly. 5–8 slides is the sweet spot; slide 1 is the hook, the last slide is the CTA.

## Multiple platforms

When asked for "all sizes", make the same design in `portrait`, `square` and `story` in one file — re-flow the layout for each (don't just scale it). Because everything is sized in `var(--u)`, most of the CSS carries over.
