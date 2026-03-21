# Wallpaper

| File | Role |
|------|------|
| `katsuki-bakugo.3840x2160.mp4` | Animated wallpaper (dark + light in `manifest.json`) |
| `katsuki-bakugo.first_frame.png` | First frame / still shown before video plays (regenerate if you replace the MP4) |

Legacy placeholders (`dark.webm`, `light.webm`, `dark.png`, `light.png`) are unused while the manifest points at the MP4; you can delete them to save space.

**Regenerate first frame** (if you change the video):

```bash
ffmpeg -i katsuki-bakugo.3840x2160.mp4 -vframes 1 katsuki-bakugo.first_frame.png
```

Or use any tool that exports frame 0 as PNG.
