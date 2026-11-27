# Quote

**Use for:** A quote from the brand's own people, or a real customer the user names and has permission to quote.

## Structure

- Big quotation mark (accent) → quote (≤ 25 words, `.headline` or `.title`) → name, role (small).
- Only use text the user supplies. Never write fake testimonials or invent people.

## Starter

```html
<section class="canvas square" data-name="quote">
  <div class="display accent" style="font-size:calc(var(--u)*24); line-height:0.6">“</div>
  <p class="headline" style="margin-top:calc(var(--u)*4)">[QUOTE TEXT FROM THE USER]</p>
  <div class="row bottom"><div class="rule"></div><span class="small"><b>[Name]</b>, [Role]</span></div>
</section>
```

**Avoid:** Don't fabricate quotes, star ratings or review counts.
