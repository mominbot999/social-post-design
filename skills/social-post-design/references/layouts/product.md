# Product spotlight

**Use for:** A product photo with its name and up to three key specs.

## Structure

- Photo takes 50–60% of the canvas (in a `.photo` block with rounded corners).
- Below or beside it: product name (headline), 2–3 specs as label/value pairs, price or CTA.
- Use only the user's photo; otherwise leave the `.photo` placeholder and say so.

## Starter

```html
<section class="canvas portrait" data-name="product">
  <div class="photo" style="height:55%"><!-- <img src="product.jpg" alt=""> --></div>
  <h1 class="headline" style="margin-top:calc(var(--u)*5)">Rice Transplanter RT-4</h1>
  <div class="row" style="margin-top:calc(var(--u)*3); gap:calc(var(--u)*6)">
    <div><div class="small">Rows</div><div class="title">4</div></div>
    <div><div class="small">Engine</div><div class="title">[HP]</div></div>
    <div><div class="small">Price</div><div class="title accent">[PRICE]</div></div>
  </div>
</section>
```

**Avoid:** Don't put text over the busy part of a photo.
