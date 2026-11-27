# Contributing

Thanks for helping! Most contributions are small Markdown + HTML changes.

## Setup

```bash
git clone https://github.com/<you>/social-post-design.git
cd social-post-design
pip install playwright && python3 -m playwright install chromium
```

## Adding a layout

1. Create `skills/social-post-design/references/layouts/<name>.md` following the existing files: **Use for**, **Structure**, **Starter** (HTML using only `base.css` classes plus small inline styles), **Avoid**.
2. Add a row to the layout index table in `SKILL.md`.
3. Add an example to `examples/NN-<name>.html` (inline the full `assets/base.css`).
4. Run the checks and export:
   ```bash
   python3 skills/social-post-design/scripts/check.py examples/NN-<name>.html
   python3 skills/social-post-design/scripts/export.py examples/NN-<name>.html -o docs/gallery
   ```
5. Add the PNG to the README gallery if it shows something new.

## Other good contributions

- New platform formats (Pinterest 1000×1500, X header, LinkedIn banner…) in `formats.md` and `base.css`.
- Palettes in `style.md` (with contrast-checked values).
- Better support for a script/language you know.
- Improvements to `check.py` (e.g. contrast checking) — include a failing example.

## Rules

- Examples must use fictional brands (Acme, FieldWorks…) and no real people's photos.
- No invented testimonials or statistics in examples — mark sample data as such.
- Keep `SKILL.md` short: details belong in `references/` so agents load them only when needed.

Be kind — see [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
