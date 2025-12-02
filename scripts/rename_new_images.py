#!/usr/bin/env python3
"""
Rename newly added images to follow standard naming convention.
Converts folder name to proper filename format.
"""

import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).parent.parent

# Define all folders that need renaming (excluding primarchs which are already good)
RENAME_TARGETS = [
    # Main wall - row 2 emperor forces
    "main_wall/row_2_emperor_forces/malcador",
    "main_wall/row_2_emperor_forces/sisters_of_battle",
    "main_wall/row_2_emperor_forces/tech_priest",
    "main_wall/row_2_emperor_forces/grey_knights",
    "main_wall/row_2_emperor_forces/assassins/culexus",
    "main_wall/row_2_emperor_forces/assassins/eversor",
    "main_wall/row_2_emperor_forces/assassins/callidus",
    "main_wall/row_2_emperor_forces/assassins/vindicare",
    "main_wall/row_2_emperor_forces/emperor_class_titan",
    "main_wall/row_2_emperor_forces/constantine_valdor",
    "main_wall/row_2_emperor_forces/sisters_of_silence",
    "main_wall/row_2_emperor_forces/inquisition",

    # Main wall - chaos gods
    "main_wall/chaos_gods/tzeentch",
    "main_wall/chaos_gods/khorne",
    "main_wall/chaos_gods/slaanesh",
    "main_wall/chaos_gods/nurgle",

    # Main wall - xenos
    "main_wall/xenos/tau",
    "main_wall/xenos/tyranids",
    "main_wall/xenos/necrons",
    "main_wall/xenos/eldar",

    # Wall 1 - assassins (remaining temples)
    "wall_1_right/assassins/venenum",
    "wall_1_right/assassins/vanus",

    # Wall 2 - chaos champions
    "wall_2_left/chaos_champions/sevatar",
    "wall_2_left/chaos_champions/abaddon",
    "wall_2_left/chaos_champions/ahriman",
    "wall_2_left/chaos_champions/kharn",

    # Wall 2 - loyalist champions
    "wall_2_left/loyalist_champions/amit",
    "wall_2_left/loyalist_champions/logan_grimnar",
    "wall_2_left/loyalist_champions/tyberos",
    "wall_2_left/loyalist_champions/sigismund",
]


def get_proper_name(folder_name):
    """Convert folder name to proper capitalized filename format."""
    # Split by underscore and capitalize each word
    words = folder_name.split('_')
    # Capitalize first letter of each word, keep rest as-is
    proper_name = '_'.join(word.capitalize() for word in words)
    return proper_name


def rename_images_in_folder(folder_path):
    """Rename all images in a folder to match the folder name."""
    folder_path = BASE_DIR / folder_path

    if not folder_path.exists():
        print(f"⚠️  Folder not found: {folder_path}")
        return

    # Get folder name (last part of path)
    folder_name = folder_path.name
    proper_name = get_proper_name(folder_name)

    # Find all image files
    image_files = list(folder_path.glob("*.jpg")) + \
                  list(folder_path.glob("*.jpeg")) + \
                  list(folder_path.glob("*.png")) + \
                  list(folder_path.glob("*.JPG")) + \
                  list(folder_path.glob("*.JPEG")) + \
                  list(folder_path.glob("*.PNG"))

    if not image_files:
        print(f"⚠️  No images found in: {folder_path}")
        return

    for img_file in image_files:
        old_name = img_file.name

        # Skip if already properly named
        if old_name.startswith(proper_name):
            print(f"✓ Already correct: {folder_path.name}/{old_name}")
            continue

        # Determine extension
        ext = img_file.suffix.lower()

        # Check if this is an A4 version (unlikely for new images, but handle it)
        if "_A4" in old_name or "_a4" in old_name:
            new_name = f"{proper_name}_A4{ext}"
        else:
            # This is the original, keep original extension
            new_name = f"{proper_name}{ext}"

        new_path = folder_path / new_name

        # Check if target already exists
        if new_path.exists():
            print(f"⚠️  Target exists, skipping: {folder_path.name}/{old_name} -> {new_name}")
            continue

        # Rename the file
        img_file.rename(new_path)
        print(f"✓ Renamed: {folder_path.name}/{old_name} -> {new_name}")


def main():
    print("=" * 70)
    print("RENAMING NEW IMAGES TO STANDARD FORMAT")
    print("=" * 70)
    print()

    renamed_count = 0

    for target in RENAME_TARGETS:
        print(f"\nProcessing: {target}")
        print("-" * 70)
        rename_images_in_folder(target)
        renamed_count += 1

    print()
    print("=" * 70)
    print(f"COMPLETE! Processed {renamed_count} folders")
    print("=" * 70)
    print()
    print("Next steps:")
    print("1. Review the renamed files")
    print("2. Run format_primarchs_a4.py to create A4 versions")
    print()


if __name__ == "__main__":
    main()
