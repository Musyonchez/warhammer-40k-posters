#!/usr/bin/env python3
"""
Format primarch images for A4 printing and save alongside originals.
Pattern: {Legion}_primarch_A4.{ext}
"""

from PIL import Image
from pathlib import Path

# A4 dimensions at 300 DPI for high-quality printing
A4_WIDTH_PX = 2480   # 210mm at 300 DPI
A4_HEIGHT_PX = 3508  # 297mm at 300 DPI

def format_primarch_for_a4(input_path, output_path):
    """
    Resize primarch image to fit A4 perfectly without white space or cropping.
    """
    try:
        # Open the image
        img = Image.open(input_path)

        # Convert to RGB if necessary (for JPEG compatibility)
        if img.mode != 'RGB':
            img = img.convert('RGB')

        # Resize to A4 dimensions (stretches to fit perfectly)
        img_resized = img.resize((A4_WIDTH_PX, A4_HEIGHT_PX), Image.Resampling.LANCZOS)

        # Save with high quality
        img_resized.save(output_path, 'JPEG', quality=95, dpi=(300, 300))

        return True
    except Exception as e:
        print(f"  ❌ Error processing {input_path.name}: {e}")
        return False

def format_all_primarchs():
    """Format all primarch images for A4 printing."""
    base_path = Path("space marine legions")

    if not base_path.exists():
        print("Error: 'space marine legions' folder not found!")
        return

    processed_count = 0
    skipped_count = 0
    error_count = 0
    empty_count = 0

    # Process each legion
    for legion_path in sorted(base_path.iterdir()):
        if not legion_path.is_dir():
            continue

        legion_name = legion_path.name
        primarch_path = legion_path / "primarch"

        if not primarch_path.exists():
            continue

        # Find image files (should match the pattern {Legion}_primarch.{ext})
        image_files = list(primarch_path.glob("*.jpeg")) + \
                     list(primarch_path.glob("*.jpg")) + \
                     list(primarch_path.glob("*.png"))

        # Filter out already formatted images (with _A4 suffix)
        original_images = [img for img in image_files if "_A4" not in img.stem]

        if not original_images:
            empty_count += 1
            print(f"❌ {legion_name} - no primarch image found")
            continue

        # Process the primarch image
        for img_path in original_images[:1]:  # Should only be one
            # Build output filename with _A4 suffix
            stem = img_path.stem
            output_name = f"{stem}_A4.jpeg"
            output_path = primarch_path / output_name

            # Check if already formatted
            if output_path.exists():
                print(f"⏭️  {legion_name} - already formatted: {output_name}")
                skipped_count += 1
                continue

            # Format the image
            print(f"🖼️  {legion_name} - formatting: {img_path.name} → {output_name}")

            if format_primarch_for_a4(img_path, output_path):
                processed_count += 1
            else:
                error_count += 1

    # Print summary
    print("\n" + "="*60)
    print("PRIMARCH A4 FORMATTING COMPLETE")
    print("="*60)
    print(f"Primarchs formatted: {processed_count}")
    print(f"Already formatted: {skipped_count}")
    print(f"Errors: {error_count}")
    print(f"Empty folders: {empty_count}")
    print("="*60)
    print("\nEach primarch folder now contains:")
    print("  - {Legion}_primarch.jpg (original)")
    print("  - {Legion}_primarch_A4.jpeg (formatted for A4 printing)")
    print("="*60)

if __name__ == "__main__":
    print("Primarch A4 Formatter")
    print("="*60)
    print("Formatting primarch images for A4 printing (2480x3508px @ 300 DPI)")
    print("="*60 + "\n")

    format_all_primarchs()
