# Hiring

**Use for:** Job openings.

## Structure

- "We're hiring" (eyebrow or display) → role title (headline) → 3 key facts (location, type, experience) as pills → how to apply.
- Only list facts the user gives (no invented salaries or perks).

## Starter

```html
<section class="canvas square" data-name="hiring">
  <div class="display">We're<br><span class="mark">hiring</span></div>
  <h2 class="title" style="margin-top:calc(var(--u)*6)">Graphic Designer</h2>
  <div class="row" style="flex-wrap:wrap; gap:calc(var(--u)*1.5); margin-top:calc(var(--u)*3)">
    <span class="pill ghost">[City]</span><span class="pill ghost">[Full-time]</span><span class="pill ghost">[2+ years]</span>
  </div>
  <p class="body bottom">Apply: [email or link]</p>
</section>
```

**Avoid:** Don't list more than three requirements on the image; put the rest in the caption.
