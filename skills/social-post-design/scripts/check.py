#!/usr/bin/env python3
"""Self-check a design before showing it: catches the mistakes that ruin social graphics.

  python3 check.py design.html

Checks every .canvas for:
  - wrong size (format class missing or overridden)
  - text or elements spilling outside the canvas
  - text clipped inside its own box (scrollHeight > clientHeight)
  - text too small to read on a phone (< 2.2% of canvas width)
  - content inside the platform's unsafe zones (story top/bottom bars)
  - fonts that failed to load (falls back silently otherwise)
Exit code 1 if any error is found.
"""
import json
import shutil
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

SIZES = {"square": (1080, 1080), "portrait": (1080, 1350), "story": (1080, 1920),
         "landscape": (1200, 628), "thumb": (1280, 720), "cover": (1640, 624)}

JS = r"""
(sizes) => {
  const out = [];
  document.querySelectorAll('.canvas').forEach((c, idx) => {
    const name = c.dataset.name || `canvas ${idx + 1}`;
    const cr = c.getBoundingClientRect();
    const fmt = Object.keys(sizes).find(k => c.classList.contains(k));
    const issues = [];
    if (!fmt) issues.push(['error', 'no format class (square/portrait/story/landscape/thumb/cover)']);
    else {
      const [w, h] = sizes[fmt];
      if (Math.round(cr.width) !== w || Math.round(cr.height) !== h)
        issues.push(['error', `size is ${Math.round(cr.width)}x${Math.round(cr.height)}, expected ${w}x${h}`]);
    }
    const minFont = cr.width * 0.022;
    c.querySelectorAll('*').forEach(el => {
      const r = el.getBoundingClientRect();
      if (r.width === 0 || r.height === 0) return;
      const label = (el.className && typeof el.className === 'string' ? '.' + el.className.split(' ')[0] : el.tagName.toLowerCase())
        + ' "' + (el.innerText || '').trim().slice(0, 30) + '"';
      const decorative = el.closest('[data-decor]');
      if (!decorative && (r.left < cr.left - 1 || r.top < cr.top - 1 || r.right > cr.right + 1 || r.bottom > cr.bottom + 1))
        issues.push(['error', `outside canvas: ${label}`]);
      const hasText = [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim());
      if (hasText) {
        const fs = parseFloat(getComputedStyle(el).fontSize);
        if (fs < minFont) issues.push(['warn', `small text ${fs.toFixed(0)}px (< ${minFont.toFixed(0)}px): ${label}`]);
        if (el.scrollHeight > el.clientHeight + 2 && getComputedStyle(el).overflow !== 'visible')
          issues.push(['error', `text clipped: ${label}`]);
        if (fmt === 'story' && !decorative && (r.top < cr.top + 200 || r.bottom > cr.bottom - 300))
          issues.push(['warn', `text in story unsafe zone (top 200px / bottom 300px): ${label}`]);
      }
    });
    out.push({ name, fmt, issues });
  });
  const fonts = [...document.fonts].filter(f => f.status === 'error').map(f => f.family);
  return { canvases: out, failedFonts: [...new Set(fonts)] };
}
"""


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    html = Path(sys.argv[1]).resolve()
    chrome = next((shutil.which(n) for n in ("google-chrome", "chromium", "chromium-browser") if shutil.which(n)), None)
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=chrome) if chrome else p.chromium.launch()
        page = browser.new_page(viewport={"width": 2400, "height": 2400})
        page.goto(html.as_uri())
        page.evaluate("document.fonts.ready")
        page.wait_for_timeout(600)
        result = page.evaluate(JS, SIZES)
        browser.close()

    errors = 0
    for c in result["canvases"]:
        print(f"■ {c['name']} ({c['fmt']})")
        if not c["issues"]:
            print("  ✓ ok")
        for level, msg in c["issues"]:
            errors += level == "error"
            print(f"  {'✗' if level == 'error' else '!'} {msg}")
    if result["failedFonts"]:
        print("! fonts failed to load (fallback used):", ", ".join(result["failedFonts"]))
    print(json.dumps({"errors": errors}))
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
