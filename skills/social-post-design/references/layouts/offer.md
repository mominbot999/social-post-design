# Offer

**Use for:** A product or service with a price, discount or deal.

## Structure

- Product name (headline) → price block (big) → 2–3 short benefits → CTA pill.
- Show the old price struck through only if the user gave it. Never invent discounts or deadlines.
- If there's a product photo, use the Product spotlight layout instead.

## Starter

```html
<section class="canvas square" data-name="offer">
  <div class="eyebrow">Weekend offer</div>
  <h1 class="headline" style="margin-top:calc(var(--u)*3)">Power Tiller<br>GX-160</h1>
  <div class="row" style="align-items:baseline; margin-top:calc(var(--u)*5)">
    <span class="display accent">[PRICE]</span>
    <span class="body" style="text-decoration:line-through">[OLD PRICE]</span>
  </div>
  <ul class="body stack" style="list-style:none; gap:calc(var(--u)*1.5); margin-top:calc(var(--u)*4)">
    <li>✓ 1-year service warranty</li><li>✓ Free delivery in [AREA]</li>
  </ul>
  <span class="pill bottom">Message us to order</span>
</section>
```

**Avoid:** Don't stack more than one price or more than three benefits.
