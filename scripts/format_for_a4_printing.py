#!/usr/bin/env python3
"""
Format Space Marine images for A4 printing without white spaces or cropped edges.
This script resizes all images in subfolders 1 and 4 to fit A4 paper perfectly.
"""

from PIL import Image
import os
from pathlib import Path

# A4 dimensions at 300 DPI for high-quality printing
A4_WIDTH_PX = 2480   # 210mm at 300 DPI
A4_HEIGHT_PX = 3508  # 297mm at 300 DPI

def format_image_for_a4(input_path, output_path):
    """
    Resize image to fit A4 perfectly without white space or cropping.
    Images are scaled to fill the entire A4 page.
    """
    try:
        # Open the image
        img = Image.open(input_path)

        # Convert to RGB if necessary (for JPEG compatibility)
        if img.mode != 'RGB':
            img = img.convert('RGB')

        # Resize to A4 dimensions (this will stretch slightly to fit perfectly)
        img_resized = img.resize((A4_WIDTH_PX, A4_HEIGHT_PX), Image.Resampling.LANCZOS)

        # Save with high quality
        img_resized.save(output_path, 'JPEG', quality=95, dpi=(300, 300))

        return True
    except Exception as e:
        print(f"Error processing {input_path}: {e}")
        return False

def process_legion_folders():
    """Process all images in subfolders 1 and 4 for all legions."""
    base_path = Path("space marine legions")

    if not base_path.exists():
        print("Error: 'space marine legions' folder not found!")
        return

    # Track statistics
    processed_count = 0
    skipped_count = 0
    error_count = 0
    empty_folders = []

    # Process each legion
    for legion_path in sorted(base_path.iterdir()):
        if not legion_path.is_dir():
            continue

        legion_name = legion_path.name
        legionnaire_path = legion_path / "legionnaire"

        if not legionnaire_path.exists():
            continue

        # Process subfolders 1 and 4
        for subfolder in ["1", "4"]:
            source_folder = legionnaire_path / subfolder

            if not source_folder.exists():
                continue

            # Check if folder is empty
            image_files = list(source_folder.glob("*.jpeg")) + \
                         list(source_folder.glob("*.jpg")) + \
                         list(source_folder.glob("*.png"))

            if not image_files:
                empty_folders.append(f"{legion_name}/legionnaire/{subfolder}")
                continue

            # Create output folder
            output_folder = legionnaire_path / f"{subfolder}_A4_formatted"
            output_folder.mkdir(exist_ok=True)

            # Process each image
            for img_path in image_files:
                output_path = output_folder / img_path.name

                # Skip if already processed
                if output_path.exists():
                    print(f"Skipping (already exists): {legion_name}/{subfolder}/{img_path.name}")
                    skipped_count += 1
                    continue

                print(f"Processing: {legion_name}/{subfolder}/{img_path.name}")

                if format_image_for_a4(img_path, output_path):
                    processed_count += 1
                else:
                    error_count += 1

    # Print summary
    print("\n" + "="*60)
    print("PROCESSING COMPLETE")
    print("="*60)
    print(f"Images processed: {processed_count}")
    print(f"Images skipped (already formatted): {skipped_count}")
    print(f"Errors: {error_count}")

    if empty_folders:
        print(f"\nEmpty folders found ({len(empty_folders)}):")
        for folder in empty_folders:
            print(f"  - {folder}")

    print("\n" + "="*60)
    print("IMPORTANT: Print the images from the *_A4_formatted folders")
    print("These images are sized at 2480x3508 pixels (300 DPI)")
    print("They will fill A4 paper completely with no white space")
    print("="*60)

if __name__ == "__main__":
    print("Space Marine A4 Image Formatter")
    print("="*60)
    print("This script formats images in subfolders 1 and 4")
    print("to fit A4 paper perfectly (no white space, no cropping)")
    print("="*60 + "\n")

    process_legion_folders()
