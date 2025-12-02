#!/usr/bin/env python3
"""
Rename formatted images to: {Legion_Name}_legionnaire_{subfolder}.{extension}
"""

import os
from pathlib import Path

def rename_formatted_images():
    """Rename all images in *_A4_formatted folders with standardized names."""
    base_path = Path("space marine legions")

    if not base_path.exists():
        print("Error: 'space marine legions' folder not found!")
        return

    renamed_count = 0
    skipped_count = 0

    # Process each legion
    for legion_path in sorted(base_path.iterdir()):
        if not legion_path.is_dir():
            continue

        legion_name = legion_path.name.replace(" ", "_")
        legionnaire_path = legion_path / "legionnaire"

        if not legionnaire_path.exists():
            continue

        # Process formatted subfolders
        for formatted_folder in legionnaire_path.glob("*_A4_formatted"):
            # Extract subfolder number (1 or 4)
            subfolder_num = formatted_folder.name.replace("_A4_formatted", "")

            # Process each image in the folder
            for img_path in formatted_folder.iterdir():
                if img_path.is_file() and img_path.suffix.lower() in ['.jpeg', '.jpg', '.png']:
                    # Build new filename
                    new_name = f"{legion_name}_legionnaire_{subfolder_num}{img_path.suffix}"
                    new_path = formatted_folder / new_name

                    # Check if already renamed
                    if img_path.name == new_name:
                        print(f"Already named: {legion_name}/{subfolder_num}_A4_formatted/{new_name}")
                        skipped_count += 1
                        continue

                    # Check if target filename already exists
                    if new_path.exists():
                        print(f"WARNING: Target exists, skipping: {new_path}")
                        skipped_count += 1
                        continue

                    # Rename the file
                    print(f"Renaming: {img_path.name} → {new_name}")
                    img_path.rename(new_path)
                    renamed_count += 1

    # Print summary
    print("\n" + "="*60)
    print("RENAMING COMPLETE")
    print("="*60)
    print(f"Images renamed: {renamed_count}")
    print(f"Images skipped: {skipped_count}")
    print("="*60)
    print("\nExample filenames:")
    print("  - World_Eaters_legionnaire_1.jpeg")
    print("  - World_Eaters_legionnaire_4.jpeg")
    print("  - Blood_Angels_legionnaire_1.jpeg")
    print("="*60)

if __name__ == "__main__":
    print("Space Marine Image Renamer")
    print("="*60)
    print("Renaming pattern: {Legion_Name}_legionnaire_{subfolder}.ext")
    print("="*60 + "\n")

    rename_formatted_images()
