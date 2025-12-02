#!/usr/bin/env python3
"""
Copy all primarch A4 images and Emperor A4 to hold folder.
"""

import shutil
from pathlib import Path

def copy_primarchs_and_emperor():
    """Copy primarchs and emperor to hold folder."""
    base_path = Path("space marine legions")
    emperor_path = Path("emperor")
    hold_folder = Path("hold")

    # Ensure hold folder exists
    hold_folder.mkdir(exist_ok=True)

    copied_count = 0
    skipped_count = 0

    print(f"Hold folder: {hold_folder.absolute()}\n")

    # Copy primarchs
    print("Copying Primarchs...")
    print("-" * 60)
    for legion_path in sorted(base_path.iterdir()):
        if not legion_path.is_dir():
            continue

        primarch_path = legion_path / "primarch"

        if not primarch_path.exists():
            continue

        # Find A4 formatted primarch images
        a4_images = list(primarch_path.glob("*_A4.jpeg")) + \
                   list(primarch_path.glob("*_A4.jpg")) + \
                   list(primarch_path.glob("*_A4.png"))

        for img_path in a4_images:
            dest_path = hold_folder / img_path.name

            if dest_path.exists():
                print(f"⏭️  {img_path.name}")
                skipped_count += 1
                continue

            print(f"📁 {img_path.name}")
            shutil.copy2(img_path, dest_path)
            copied_count += 1

    # Copy Emperor
    print("\nCopying Emperor...")
    print("-" * 60)
    emperor_a4 = emperor_path / "Emperor_A4.jpeg"

    if emperor_a4.exists():
        dest_path = hold_folder / emperor_a4.name

        if dest_path.exists():
            print(f"⏭️  Emperor_A4.jpeg")
            skipped_count += 1
        else:
            print(f"📁 Emperor_A4.jpeg")
            shutil.copy2(emperor_a4, dest_path)
            copied_count += 1

    # Print summary
    print("\n" + "="*60)
    print("COPY COMPLETE")
    print("="*60)
    print(f"New files copied: {copied_count}")
    print(f"Already in hold: {skipped_count}")
    print(f"Total A4 images in hold: {len(list(hold_folder.glob('*_A4.*')))}")
    print("="*60)
    print(f"\n📁 All print-ready images in: {hold_folder.absolute()}")
    print("="*60)

if __name__ == "__main__":
    print("Copy Primarchs and Emperor to Hold")
    print("="*60 + "\n")

    copy_primarchs_and_emperor()
