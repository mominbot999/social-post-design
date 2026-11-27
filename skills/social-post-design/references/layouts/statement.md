# Statement

**Use for:** Announcements, big news, a single strong message.

## Structure

- Eyebrow (category or date) → display headline (≤ 8 words) → optional one-line body → brand at the bottom.
- Put the headline in the upper-middle third; let empty space do the work.
- Highlight one word with `.mark` or `.accent`.

## Starter

```html
<section class="canvas portrait" data-name="statement">
  <div class="eyebrow">New · March 2026</div>
  <h1 class="display" style="margin-top:calc(var(--u)*8)">We now deliver <span class="mark">nationwide</span>.</h1>
  <p class="body" style="margin-top:calc(var(--u)*4); max-width:80%">Order before 5 pm, get it in 48 hours.</p>
  <div class="row bottom" style="justify-content:space-between">
    <div class="brand"><span class="logo">A</span>Acme Store</div>
    <span class="pill">Order now →</span>
  </div>
</section>
```

**Avoid:** Don't add a second message or a list — that's a carousel.
