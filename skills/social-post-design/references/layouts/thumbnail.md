# Thumbnail

**Use for:** YouTube and video covers (1280×720).

## Structure

- 2–5 words, huge (≥ 10% of width), heavy weight, high contrast. It must read at 160 px wide.
- One focal element: a face/photo from the user on one side, text on the other.
- Keep the bottom-right corner empty (video length badge).

## Starter

```html
<section class="canvas thumb theme-dark" data-name="thumbnail" style="flex-direction:row; align-items:center">
  <div class="grow">
    <div class="display" style="font-size:calc(var(--u)*10.5)">I tried<br><span class="mark">7 days</span><br>of AI ads</div>
  </div>
  <div class="photo" style="width:38%; height:78%; align-self:flex-start"><!-- user's photo; keep bottom-right empty --></div>
</section>
```

**Avoid:** Don't write a full sentence; don't use thin fonts; no clickbait claims the video doesn't deliver.
