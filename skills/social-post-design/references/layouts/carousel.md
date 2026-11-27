# Carousel

**Use for:** Stories and tutorials across 5–8 slides of the same format.

## Structure

- **Slide 1 (hook):** a promise or a question in `.display`, plus "Swipe →".
- **Middle slides:** one point each — number, title, one line of body. Keep the same grid so swiping feels smooth.
- **Last slide:** summary + one CTA (save, share, follow, message).
- Add `.slide-no` (e.g. "2/6") to every slide. Name canvases `slide-01`, `slide-02`… so exports sort.

## Starter

```html
<section class="canvas portrait" data-name="slide-01">
  <span class="slide-no">1/6</span>
  <div class="eyebrow">Guide</div>
  <h1 class="display" style="margin-top:calc(var(--u)*8)">How to price your first product</h1>
  <span class="pill ghost bottom">Swipe →</span>
</section>
<section class="canvas portrait" data-name="slide-02">
  <span class="slide-no">2/6</span>
  <div class="display accent">01</div>
  <h2 class="headline" style="margin-top:calc(var(--u)*4)">Know your real cost</h2>
  <p class="body" style="margin-top:calc(var(--u)*3)">Materials + delivery + payment fees + your time.</p>
</section>
```

**Avoid:** Don't change layouts between middle slides; don't cram two points on one slide.
