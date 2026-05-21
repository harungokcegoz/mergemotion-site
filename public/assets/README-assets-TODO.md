# Assets TODO — requires image tooling (ImageMagick or similar)

These files are referenced in `public/index.html` and `public/site.webmanifest`
but could not be generated on this VPS (no ImageMagick / `convert` available).
Generate them on a machine with ImageMagick before deploying to production.

## og-image.png (1200x630)

Dark `#0A0A0F` background. "Merge" wordmark centered, below it the line
"Turn any photo into an AI motion video." in near-white (`#F5F5F5`).
Purple accent bar or glow element (`#7C3AED`–`#A855F7` gradient).

Example command (adjust font path as needed):
```bash
convert -size 1200x630 xc:'#0A0A0F' \
  -font DejaVu-Sans-Bold -pointsize 96 -fill '#F5F5F5' \
  -gravity Center -annotate -0+(-60) 'Merge' \
  -font DejaVu-Sans -pointsize 40 -fill '#A855F7' \
  -gravity Center -annotate -0+(+60) 'Turn any photo into an AI motion video.' \
  public/assets/og-image.png
```

## favicon.ico

"M" on a purple gradient background (`#7C3AED`→`#A855F7`), 32x32 + 16x16 multi-size ICO.

Example (single-size fallback):
```bash
convert -size 64x64 gradient:'#7C3AED-#A855F7' \
  -font DejaVu-Sans-Bold -pointsize 44 -fill white \
  -gravity Center -annotate 0 'M' \
  favicon_64.png
convert favicon_64.png -define icon:auto-resize=32,16 public/assets/favicon.ico
```

## apple-touch-icon.png (180x180)

Same "M" on purple gradient as favicon, at 180x180.

```bash
convert -size 180x180 gradient:'#7C3AED-#A855F7' \
  -font DejaVu-Sans-Bold -pointsize 120 -fill white \
  -gravity Center -annotate 0 'M' \
  public/assets/apple-touch-icon.png
```

Until these are generated the references will 404, which is acceptable for
development. The `<meta og:image>` and `<link rel="icon">` tags are already in
place in the HTML so no further code changes are needed once the files exist.
