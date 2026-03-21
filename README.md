# Katsuki Bakugo: Rising — Opera GX mod

Full **My Hero Academia**–style mod for Opera GX themed around **Katsuki Bakugo**: animated wallpaper, background music, sounds, **orange-on-black** hero-suit colours, shaders, and web modding for 21+ sites (same layout as the Izuku Midoriya: Rising pack).

## Structure

```
Katsuki Bakugo Rising/
├── manifest.json
├── Bakugo_Icon.png        # 512×512 mod icon (`manifest.json` → `icons.512`)
├── license.txt
├── wallpaper/
├── music/
├── sound/
├── keyboard/
├── shader/                # Explosion Glow, Howitzer Impact
├── webmodding/            # theme, site CSS, micro-nuance, GX surfaces — see below
├── MOD_BROWSER.md       # What mods can/can’t style (address bar, etc.)
└── scripts/
```

## Extra polish (v1.1+)

- **`micro-nuance.css`** — Injected on every modded site: orange/black **text selection**, **scrollbar** thumb, **`:focus-visible`** rings, **placeholder** tint. Does **not** change the native address bar (see [MOD_BROWSER.md](MOD_BROWSER.md)).
- **`gx-surfaces.css`** — Bakugo styling on **GX web** tabs: `gx.games`, `create.gx.games`, `gx.me`, `store.gx.me`.
- **`opera.css`** — Richer rules for **`*.opera.com`** (typography, links, form controls, code blocks).
- **Wallpaper labels** — `manifest.json` → `wallpaper.*.text_color` / `text_shadow`: dark mode uses **orange titles** on a **black** shadow; light mode uses **near-black** text with a **soft orange** shadow.

## Assets

The **mod icon** is `Bakugo_Icon.png`, wired in `manifest.json` under `icons` → `"512"`. **Wallpaper** uses `wallpaper/katsuki-bakugo.3840x2160.mp4` plus `wallpaper/katsuki-bakugo.first_frame.png` (see `wallpaper/README.md`). **Background music** is a single track: `music/Butterfly Effect.mp3`. Browser/keyboard sounds may still be placeholders from the Izuku pack; swap paths in `manifest.json` if you replace them.

## Theme

- **Look**: orange accents (`#FF8C1E` and variants) on **true black** (`#000000`) with charcoal surfaces (`#121212`) — same vibe as Bakugo’s costume.
- **GX UI**: `gx_accent` / `gx_secondary_base` HSL in `manifest.json` drives **native** chrome (tabs, highlights, etc.). There is no separate “URL bar text colour” field in the public schema — see [MOD_BROWSER.md](MOD_BROWSER.md).
- **Shaders**: **Explosion Glow** (orange pop on dark), **Howitzer Impact** (animated wave).

## Load & test

1. `opera:extensions` → Developer mode → **Load unpacked** → this folder  
2. `opera:mods` → enable the mod  

## Publish

See [PUBLISHING.md](PUBLISHING.md) and [GX.create](https://create.gx.games/mods).
