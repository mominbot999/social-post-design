# List

**Use for:** Tips, steps, checklists, "5 things…" on a single image.

## Structure

- Headline (the promise) → 3–5 numbered items, each ≤ 7 words → brand.
- More than 5 items → use a Carousel.
- Numbers in the accent colour, items in `.title` weight 600.

## Starter

```html
<section class="canvas portrait" data-name="list">
  <div class="eyebrow">Save this</div>
  <h1 class="headline" style="margin:calc(var(--u)*3) 0 calc(var(--u)*6)">4 checks before you buy a used phone</h1>
  <ol class="stack" style="list-style:none; gap:calc(var(--u)*3.5)">
    <li class="row title" style="font-weight:600"><span class="accent" style="width:calc(var(--u)*8)">01</span>Battery health above 80%</li>
    <li class="row title" style="font-weight:600"><span class="accent" style="width:calc(var(--u)*8)">02</span>IMEI matches the box</li>
  </ol>
  <div class="brand bottom"><span class="logo">A</span>Acme</div>
</section>
```

**Avoid:** Don't write full sentences; don't add icons to every item.
