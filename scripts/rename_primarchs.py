#!/usr/bin/env python3
"""
Rename primarch images to: {Legion_Name}_primarch.{extension}
"""

from pathlib import Path

def rename_primarch_images():
    """Rename all primarch images with standardized names."""
    base_path = Path("space marine legions")

    if not base_path.exists():
        print("Error: 'space marine legions' folder not found!")
        return

    renamed_count = 0
    skipped_count = 0
    empty_count = 0

    # Process each legion
    for legion_path in sorted(base_path.iterdir()):
        if not legion_path.is_dir():
            continue

        legion_name = legion_path.name.replace(" ", "_")
        primarch_path = legion_path / "primarch"

        if not primarch_path.exists():
            continue

        # Find image files
        image_files = list(primarch_path.glob("*.jpeg")) + \
                     list(primarch_path.glob("*.jpg")) + \
                     list(primarch_path.glob("*.png"))

        if not image_files:
            empty_count += 1
            print(f"❌ {legion_path.name} - no primarch image")
            continue

        # Process first image found (should only be one per legion)
        for img_path in image_files[:1]:  # Only process first image
            # Build new clean filename
            new_name = f"{legion_name}_primarch{img_path.suffix}"
            new_path = primarch_path / new_name

            # Check if already renamed
            if img_path.name == new_name:
                print(f"✅ {legion_path.name} - already named: {new_name}")
                skipped_count += 1
                continue

            # Check if target exists
            if new_path.exists():
                print(f"⚠️  {legion_path.name} - WARNING: {new_name} already exists, skipping")
                skipped_count += 1
                continue

            # Rename the file
            print(f"✏️  {legion_path.name} - Renaming: {img_path.name} → {new_name}")
            img_path.rename(new_path)
            renamed_count += 1

        # Warn if multiple images found
        if len(image_files) > 1:
            print(f"   ⚠️  Multiple images found, only renamed first one")

    # Print summary
    print("\n" + "="*60)
    print("PRIMARCH RENAMING COMPLETE")
    print("="*60)
    print(f"Primarchs renamed: {renamed_count}")
    print(f"Already named correctly: {skipped_count}")
    print(f"Empty primarch folders: {empty_count}")
    print("="*60)
    print("\nExample filenames:")
    print("  - World_Eaters_primarch.jpeg")
    print("  - Death_Guard_primarch.jpeg")
    print("  - Space_Wolves_primarch.jpeg")
    print("="*60)

if __name__ == "__main__":
    print("Primarch Image Renamer")
    print("="*60)
    print("Renaming pattern: {Legion_Name}_primarch.ext")
    print("="*60 + "\n")

    rename_primarch_images()
