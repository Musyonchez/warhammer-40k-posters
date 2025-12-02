#!/usr/bin/env python3
"""
Reorganize images: consolidate originals and formatted into folders 1 and 4.
- Rename original images to clean pattern
- Move formatted images back to parent folders with _A4 suffix
- Delete empty _A4_formatted folders
"""

import shutil
from pathlib import Path

def reorganize_legion_images():
    """Consolidate original and formatted images into folders 1 and 4."""
    base_path = Path("space marine legions")

    if not base_path.exists():
        print("Error: 'space marine legions' folder not found!")
        return

    renamed_originals = 0
    moved_formatted = 0
    deleted_folders = 0
    errors = []

    # Process each legion
    for legion_path in sorted(base_path.iterdir()):
        if not legion_path.is_dir():
            continue

        legion_name = legion_path.name.replace(" ", "_")
        legionnaire_path = legion_path / "legionnaire"

        if not legionnaire_path.exists():
            continue

        # Process subfolders 1 and 4
        for subfolder in ["1", "4"]:
            original_folder = legionnaire_path / subfolder
            formatted_folder = legionnaire_path / f"{subfolder}_A4_formatted"

            if not original_folder.exists():
                continue

            print(f"\n{'='*60}")
            print(f"Processing: {legion_path.name} - Subfolder {subfolder}")
            print('='*60)

            # Step 1: Rename original images in folder 1 or 4
            image_files = list(original_folder.glob("*.jpeg")) + \
                         list(original_folder.glob("*.jpg")) + \
                         list(original_folder.glob("*.png"))

            for img_path in image_files:
                # Build new clean filename
                new_name = f"{legion_name}_legionnaire_{subfolder}{img_path.suffix}"
                new_path = original_folder / new_name

                # Skip if already renamed
                if img_path.name == new_name:
                    print(f"  Original already named: {new_name}")
                    continue

                # Check if target exists
                if new_path.exists():
                    error_msg = f"  WARNING: Can't rename {img_path.name}, {new_name} already exists"
                    print(error_msg)
                    errors.append(error_msg)
                    continue

                # Rename original
                print(f"  Renaming original: {img_path.name} → {new_name}")
                img_path.rename(new_path)
                renamed_originals += 1

            # Step 2: Move formatted images from *_A4_formatted folder
            if formatted_folder.exists():
                formatted_images = list(formatted_folder.glob("*.jpeg")) + \
                                  list(formatted_folder.glob("*.jpg")) + \
                                  list(formatted_folder.glob("*.png"))

                for formatted_img in formatted_images:
                    # Add _A4 suffix before extension
                    stem = formatted_img.stem
                    # If it already ends with _A4, don't add again
                    if not stem.endswith("_A4"):
                        new_name = f"{stem}_A4{formatted_img.suffix}"
                    else:
                        new_name = formatted_img.name

                    dest_path = original_folder / new_name

                    # Check if already exists
                    if dest_path.exists():
                        print(f"  Formatted already exists: {new_name}")
                        # Delete the formatted folder version
                        formatted_img.unlink()
                        continue

                    # Move formatted image
                    print(f"  Moving formatted: {formatted_img.name} → {new_name}")
                    shutil.move(str(formatted_img), str(dest_path))
                    moved_formatted += 1

                # Step 3: Delete empty _A4_formatted folder
                remaining = list(formatted_folder.iterdir())
                if not remaining:
                    print(f"  Deleting empty folder: {formatted_folder.name}")
                    formatted_folder.rmdir()
                    deleted_folders += 1
                else:
                    print(f"  WARNING: {formatted_folder.name} not empty, skipping deletion")

    # Print summary
    print("\n" + "="*60)
    print("REORGANIZATION COMPLETE")
    print("="*60)
    print(f"Original images renamed: {renamed_originals}")
    print(f"Formatted images moved: {moved_formatted}")
    print(f"Empty folders deleted: {deleted_folders}")

    if errors:
        print(f"\nErrors encountered ({len(errors)}):")
        for error in errors:
            print(error)

    print("\n" + "="*60)
    print("New structure: Folders 1 and 4 contain:")
    print("  - {Legion}_legionnaire_{#}.jpeg (original)")
    print("  - {Legion}_legionnaire_{#}_A4.jpeg (formatted)")
    print("="*60)

if __name__ == "__main__":
    print("Image Reorganization Script")
    print("="*60)
    print("Consolidating original and formatted images into folders 1 and 4")
    print("="*60)

    reorganize_legion_images()
