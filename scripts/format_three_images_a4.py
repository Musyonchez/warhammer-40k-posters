#!/usr/bin/env python3
"""
Format three specific images to A4 print specifications.
Processes: Sanguinius, Emperor, and Ahriman
"""

from PIL import Image
import os

# A4 dimensions at 300 DPI
A4_WIDTH = 2480
A4_HEIGHT = 3508
QUALITY = 95

def format_to_a4(input_path, output_path):
    """Resize image to A4 specifications"""
    print(f"Processing: {input_path}")

    # Open and convert to RGB (for JPEG compatibility)
    img = Image.open(input_path)
    if img.mode != 'RGB':
        img = img.convert('RGB')

    # Resize to exact A4 dimensions (stretch to fill)
    img_resized = img.resize((A4_WIDTH, A4_HEIGHT), Image.Resampling.LANCZOS)

    # Save as JPEG
    img_resized.save(output_path, 'JPEG', quality=QUALITY)
    print(f"  → Saved: {output_path}")

def main():
    base_dir = "/home/musyonchez/Code/warhammer-40k-posters"

    images_to_process = [
        {
            "input": os.path.join(base_dir, "main_wall/row_1_primarchs/sanguinius/Sanguinius.jpeg"),
            "output": os.path.join(base_dir, "main_wall/row_1_primarchs/sanguinius/Sanguinius_A4.jpeg")
        },
        {
            "input": os.path.join(base_dir, "main_wall/row_2_emperor_forces/emperor/Emperor.jpeg"),
            "output": os.path.join(base_dir, "main_wall/row_2_emperor_forces/emperor/Emperor_A4.jpeg")
        },
        {
            "input": os.path.join(base_dir, "wall_2_left/chaos_champions/ahriman/Ahriman.jpeg"),
            "output": os.path.join(base_dir, "wall_2_left/chaos_champions/ahriman/Ahriman_A4.jpeg")
        }
    ]

    print("=" * 60)
    print("Formatting 3 images to A4 print specifications")
    print(f"Target dimensions: {A4_WIDTH}x{A4_HEIGHT}px @ 300 DPI")
    print("=" * 60)
    print()

    for img_data in images_to_process:
        if os.path.exists(img_data["input"]):
            format_to_a4(img_data["input"], img_data["output"])
        else:
            print(f"WARNING: File not found - {img_data['input']}")
        print()

    print("=" * 60)
    print("Processing complete!")
    print("=" * 60)

if __name__ == "__main__":
    main()
