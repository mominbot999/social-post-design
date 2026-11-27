# Story CTA

**Use for:** Full-screen 9:16 stories, Reels covers, WhatsApp status.

## Structure

- Respect the unsafe zones (the `story` class pads 220 px top, 340 px bottom).
- Big headline in the middle third → short line → CTA pointing to where the user taps ("Tap the link ↑", "Swipe up", "DM us").
- Use 2–3 big blocks only; stories are seen for ~2 seconds.

## Starter

```html
<section class="canvas story" data-name="story">
  <div class="eyebrow">Today only</div>
  <h1 class="display" style="margin-top:auto; font-size:calc(var(--u)*13)">Free delivery<br><span class="accent">all day</span></h1>
  <p class="body" style="margin-top:calc(var(--u)*4)">On every order in [AREA].</p>
  <span class="pill" style="margin-top:auto; align-self:center; font-size:calc(var(--u)*4)">DM us to order</span>
</section>
```

**Avoid:** Don't put text in the top 200 px or bottom 300 px.
