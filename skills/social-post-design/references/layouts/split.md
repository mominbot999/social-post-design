# Split

**Use for:** Before/after, this vs that, problem → solution, myth vs fact.

## Structure

- Two equal halves (vertical on `portrait`/`story`, side by side on `square`/`landscape`).
- Each half: small label ("Before" / "After") + 1–3 words or a photo.
- Use `--surface` for one half and `--accent` (with `--accent-fg` text) for the "better" half.

## Starter

```html
<section class="canvas square" data-name="split" style="padding:0; flex-direction:row">
  <div class="grow stack" style="padding:var(--safe); background:var(--surface)">
    <div class="eyebrow" style="color:var(--muted)">Manual</div>
    <div class="headline bottom">3 days per acre</div>
  </div>
  <div class="grow stack" style="padding:var(--safe); background:var(--accent); color:var(--accent-fg)">
    <div class="eyebrow" style="color:inherit">With a reaper</div>
    <div class="headline bottom">4 hours per acre</div>
  </div>
</section>
```

**Avoid:** Don't use before/after body or health photos in ads — platforms reject them.
