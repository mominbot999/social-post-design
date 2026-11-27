# Event

**Use for:** Webinars, launches, workshops, store openings.

## Structure

- Event type (eyebrow) → event name (headline) → date block (big day number + month) → time, place/link → CTA.
- Date and time must come from the user; include the time zone for online events.

## Starter

```html
<section class="canvas portrait" data-name="event">
  <div class="eyebrow">Free workshop</div>
  <h1 class="headline" style="margin-top:calc(var(--u)*3)">Facebook ads for small shops</h1>
  <div class="row card" style="margin-top:calc(var(--u)*8); gap:calc(var(--u)*5)">
    <div class="display accent">[DD]</div>
    <div class="stack" style="gap:var(--u)"><div class="title">[Month, Day]</div><div class="body">[Time, time zone] · [Place / Online]</div></div>
  </div>
  <span class="pill bottom">Register — link in bio</span>
</section>
```

**Avoid:** Don't hide the date in small text — it's the second thing people look for.
