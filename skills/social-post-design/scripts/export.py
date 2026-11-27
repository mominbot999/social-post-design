#!/usr/bin/env python3
"""Export every .canvas in a design HTML file to PNG (or JPG/PDF).

Usage:
  python3 export.py design.html                 # → design-1.png, design-2.png ... next to the file
  python3 export.py design.html -o out/ --scale 2 --format jpg

Needs Playwright:  pip install playwright && python3 -m playwright install chromium
(or an installed Chrome: it is used automatically when found).
"""
import argparse
import shutil
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright


def find_chrome():
    for name in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser"):
        path = shutil.which(name)
        if path:
            return path
    return None


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("html", type=Path)
    ap.add_argument("-o", "--out", type=Path, help="output folder (default: next to the HTML file)")
    ap.add_argument("--scale", type=float, default=1, help="device scale factor, e.g. 2 for retina (default 1)")
    ap.add_argument("--format", choices=["png", "jpg", "pdf"], default="png")
    ap.add_argument("--wait", type=int, default=800, help="ms to wait for fonts/images (default 800)")
    args = ap.parse_args()

    html = args.html.resolve()
    if not html.exists():
        sys.exit(f"Not found: {html}")
    out = (args.out or html.parent).resolve()
    out.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        chrome = find_chrome()
        browser = p.chromium.launch(executable_path=chrome) if chrome else p.chromium.launch()
        page = browser.new_page(viewport={"width": 2400, "height": 2400}, device_scale_factor=args.scale)
        page.goto(html.as_uri())
        page.evaluate("document.fonts.ready")
        page.wait_for_timeout(args.wait)

        canvases = page.locator(".canvas")
        count = canvases.count()
        if count == 0:
            sys.exit("No .canvas elements found.")

        written = []
        for i in range(count):
            el = canvases.nth(i)
            name = el.get_attribute("data-name") or html.stem
            suffix = f"-{i + 1}" if count > 1 and not el.get_attribute("data-name") else ""
            target = out / f"{name}{suffix}.{args.format}"
            if args.format == "pdf":
                box = el.bounding_box()
                page.pdf(path=str(target), width=f"{box['width']}px", height=f"{box['height']}px",
                         print_background=True, page_ranges=str(i + 1))
            else:
                el.screenshot(path=str(target), type="jpeg" if args.format == "jpg" else "png",
                              **({"quality": 92} if args.format == "jpg" else {}))
            written.append(target)

        browser.close()

    for t in written:
        print(t)


if __name__ == "__main__":
    main()
