#!/usr/bin/env python3
"""Create a minimal 512x512 placeholder icon for the mod."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ICON_PATH = ROOT / "Bakugo_Icon.png"


def main():
    try:
        from PIL import Image

        img = Image.new("RGB", (512, 512), color=(255, 140, 30))  # explosion orange
        img.save(ICON_PATH)
        print(f"Created {ICON_PATH}")
    except ImportError:
        print("Install Pillow for icon: pip install Pillow")
        print("Or add your own 512×512 Bakugo_Icon.png")


if __name__ == "__main__":
    main()
