#!/usr/bin/env python3
"""
Create A4 versions of all newly renamed images.
Resizes to 2480x3508px (A4 @ 300 DPI) and saves as *_A4.jpeg
"""

from PIL import Image
import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).parent.parent

# A4 dimensions at 300 DPI
A4_WIDTH = 2480
A4_HEIGHT = 3508

# All folders with new images that need A4 versions
TARGET_FOLDERS = [
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

    # Wall 1 - traitor primarchs (special art set)
    "wall_1_right/traitor_primarchs/fulgrim",
    "wall_1_right/traitor_primarchs/angron",
    "wall_1_right/traitor_primarchs/magnus",
    "wall_1_right/traitor_primarchs/mortarion",
    "wall_1_right/traitor_primarchs/lorgar",
    "wall_1_right/traitor_primarchs/perturabo",

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


def format_image_to_a4(image_path):
    """
    Resize image to A4 format (2480x3508px @ 300 DPI).
    Returns True if successful, False otherwise.
    """
    try:
        # Open image
        img = Image.open(image_path)

        # Convert to RGB if needed (for JPEG compatibility)
        if img.mode != 'RGB':
            img = img.convert('RGB')

        # Resize to A4 dimensions (stretch to fit)
        img_resized = img.resize((A4_WIDTH, A4_HEIGHT), Image.Resampling.LANCZOS)

        # Generate output filename
        base_name = image_path.stem  # filename without extension
        output_path = image_path.parent / f"{base_name}_A4.jpeg"

        # Skip if A4 version already exists
        if output_path.exists():
            return False, "A4 version already exists"

        # Save as JPEG with high quality
        img_resized.save(output_path, 'JPEG', quality=95)

        return True, output_path.name

    except Exception as e:
        return False, f"Error: {str(e)}"


def process_folder(folder_path):
    """Process all images in a folder."""
    folder_path = BASE_DIR / folder_path

    if not folder_path.exists():
        print(f"⚠️  Folder not found: {folder_path}")
        return 0

    # Find all image files (originals, not A4 versions)
    image_files = []
    for ext in ['*.jpg', '*.jpeg', '*.png', '*.JPG', '*.JPEG', '*.PNG']:
        for img_file in folder_path.glob(ext):
            # Skip if it's already an A4 version
            if '_A4' not in img_file.stem:
                image_files.append(img_file)

    if not image_files:
        print(f"⚠️  No original images found in: {folder_path.name}")
        return 0

    processed_count = 0

    for img_file in image_files:
        success, result = format_image_to_a4(img_file)

        if success:
            print(f"  ✓ Created: {result}")
            processed_count += 1
        else:
            if "already exists" in result:
                print(f"  → Skipped: {img_file.name} ({result})")
            else:
                print(f"  ✗ Failed: {img_file.name} - {result}")

    return processed_count


def main():
    print("=" * 70)
    print("CREATING A4 VERSIONS OF NEW IMAGES")
    print(f"Target dimensions: {A4_WIDTH}x{A4_HEIGHT}px (A4 @ 300 DPI)")
    print("=" * 70)
    print()

    total_processed = 0

    for target in TARGET_FOLDERS:
        print(f"\n📁 Processing: {target}")
        print("-" * 70)
        count = process_folder(target)
        total_processed += count

    print()
    print("=" * 70)
    print(f"COMPLETE! Created {total_processed} A4 versions")
    print("=" * 70)
    print()
    print("All images are now ready for A4 printing!")
    print("Print settings: A4 paper, 100% scale, no margins, best quality")
    print()


if __name__ == "__main__":
    main()
