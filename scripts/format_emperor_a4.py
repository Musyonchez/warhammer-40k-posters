#!/usr/bin/env python3
"""
Format Emperor image for A4 printing.
"""

from PIL import Image
from pathlib import Path

# A4 dimensions at 300 DPI
A4_WIDTH_PX = 2480
A4_HEIGHT_PX = 3508

def format_emperor():
    """Format the Emperor image for A4 printing."""
    emperor_path = Path("emperor")

    if not emperor_path.exists():
        print("Error: emperor folder not found!")
        return

    # Find the original image
    original = emperor_path / "Emperor.jpg"

    if not original.exists():
        print("Error: Emperor.jpg not found!")
        return

    # Output path
    output = emperor_path / "Emperor_A4.jpeg"

    if output.exists():
        print("✅ Emperor already formatted: Emperor_A4.jpeg")
        return

    try:
        print(f"🖼️  Formatting Emperor image for A4...")

        # Open and process
        img = Image.open(original)

        if img.mode != 'RGB':
            img = img.convert('RGB')

        # Resize to A4
        img_resized = img.resize((A4_WIDTH_PX, A4_HEIGHT_PX), Image.Resampling.LANCZOS)

        # Save
        img_resized.save(output, 'JPEG', quality=95, dpi=(300, 300))

        print(f"✅ Emperor formatted successfully!")
        print(f"   Original: Emperor.jpg")
        print(f"   Formatted: Emperor_A4.jpeg (2480x3508px @ 300 DPI)")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("Emperor A4 Formatter")
    print("="*60)
    format_emperor()
    print("="*60)
