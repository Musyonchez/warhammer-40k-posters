#!/usr/bin/env python3
"""
Copy all formatted images to a central 'hold' folder for easy printing.
"""

import shutil
from pathlib import Path

def copy_formatted_images_to_hold():
    """Copy all A4 formatted images to the hold folder."""
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

        # Find all A4_formatted folders
        for formatted_folder in legionnaire_path.glob("*_A4_formatted"):
            # Process each image
            for img_path in formatted_folder.iterdir():
                if img_path.is_file() and img_path.suffix.lower() in ['.jpeg', '.jpg', '.png']:
                    dest_path = hold_folder / img_path.name

                    # Check if already exists
                    if dest_path.exists():
                        print(f"Already exists: {img_path.name}")
                        skipped_count += 1
                        continue

                    # Copy the file
                    print(f"Copying: {img_path.name}")
                    shutil.copy2(img_path, dest_path)
                    copied_count += 1

    # Print summary
    print("\n" + "="*60)
    print("COPY COMPLETE")
    print("="*60)
    print(f"Images copied to hold: {copied_count}")
    print(f"Images skipped (already in hold): {skipped_count}")
    print(f"Total images in hold folder: {len(list(hold_folder.glob('*.jpeg'))) + len(list(hold_folder.glob('*.jpg'))) + len(list(hold_folder.glob('*.png')))}")
    print("="*60)
    print(f"\n📁 All print-ready images are in: {hold_folder.absolute()}")
    print("="*60)

if __name__ == "__main__":
    print("Copy Formatted Images to Hold Folder")
    print("="*60)
    print("This copies all A4 formatted images to one folder for easy printing")
    print("="*60 + "\n")

    copy_formatted_images_to_hold()
