# Stat

**Use for:** One impressive, real number with context.

## Structure

- Giant number (`.display` at ~2× size or more) → what it means (title) → source/time frame (small).
- The number must come from the user. Always show the time frame or source.

## Starter

```html
<section class="canvas portrait center" data-name="stat">
  <div class="eyebrow">2025 in numbers</div>
  <div class="display accent" style="font-size:calc(var(--u)*30); margin:calc(var(--u)*4) 0">12k</div>
  <p class="title" style="max-width:80%">farmers now use our machines</p>
  <p class="small bottom">Source: our sales records, Jan–Dec 2025</p>
</section>
```

**Avoid:** Don't use more than one big number; don't round in a misleading way.
