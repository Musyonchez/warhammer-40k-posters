#!/usr/bin/env python3
"""
Copy all legionnaire A4 images from folders 1 and 4 to hold folder.
"""

import shutil
from pathlib import Path

def copy_legionnaires_to_hold():
    """Copy all legionnaire A4 formatted images to hold folder."""
    base_path = Path("space marine legions")
    hold_folder = Path("hold")

    # Create hold folder
    hold_folder.mkdir(exist_ok=True)
    print(f"Hold folder: {hold_folder.absolute()}\n")

    copied_count = 0
    skipped_count = 0

    # Process each legion
    for legion_path in sorted(base_path.iterdir()):
        if not legion_path.is_dir():
            continue

        legionnaire_path = legion_path / "legionnaire"

        if not legionnaire_path.exists():
            continue

        # Process folders 1 and 4
        for subfolder in ["1", "4"]:
            folder = legionnaire_path / subfolder

            if not folder.exists():
                continue

            # Find A4 formatted images (with _A4 suffix)
            a4_images = list(folder.glob("*_A4.jpeg")) + \
                       list(folder.glob("*_A4.jpg")) + \
                       list(folder.glob("*_A4.png"))

            for img_path in a4_images:
                dest_path = hold_folder / img_path.name

                # Check if already exists
                if dest_path.exists():
                    print(f"⏭️  Already in hold: {img_path.name}")
                    skipped_count += 1
                    continue

                # Copy the file
                print(f"📁 Copying: {img_path.name}")
                shutil.copy2(img_path, dest_path)
                copied_count += 1

    # Print summary
    print("\n" + "="*60)
    print("COPY COMPLETE")
    print("="*60)
    print(f"Legionnaires copied to hold: {copied_count}")
    print(f"Already in hold: {skipped_count}")
    print(f"Total A4 images in hold: {len(list(hold_folder.glob('*_A4.*')))}")
    print("="*60)
    print(f"\n📁 All legionnaire print-ready images in: {hold_folder.absolute()}")
    print("="*60)

if __name__ == "__main__":
    print("Copy Legionnaire A4 Images to Hold")
    print("="*60)
    print("Copying all *_A4 images from folders 1 and 4 to hold/")
    print("="*60 + "\n")

    copy_legionnaires_to_hold()
