# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Warhammer 40K poster wall display project. Organized collection of A4 posters (2480×3508px @ 300 DPI) arranged across three walls:
- **Main wall:** 13×3 grid featuring Primarchs, Emperor, Imperial forces, Chaos Gods, and Xenos
- **Wall 1 (Right):** 2×4 grid with Traitor Primarchs and Assassins
- **Wall 2 (Left):** 2×4 grid with Chaos vs Loyalist champions

Total: 55 A4 posters organized by wall position and theme.

## Running Scripts

All scripts must be run with the virtual environment Python:

```bash
# Legionnaires
venv/bin/python3 scripts/format_for_a4_printing.py
venv/bin/python3 scripts/reorganize_images.py

# New images (primarchs, emperor forces, champions, etc.)
venv/bin/python3 scripts/rename_new_images.py
venv/bin/python3 scripts/format_new_images_a4.py
```

**Never** use system Python - always use `venv/bin/python3`.

## Architecture

### Directory Structure

**Wall Layout (organized by position):**
- `main_wall/` - 13×3 grid organized by rows and themes
  - `row_1_primarchs/` - Primarchs I, III-X (9 individual primarch folders)
    - lion_el_jonson, fulgrim, perturabo, jaghatai_khan, leman_russ, rogal_dorn, konrad_curze, sanguinius, ferrus_manus
  - `row_2_emperor_forces/` - Emperor and Imperial organizations
    - emperor, constantine_valdor, malcador, sisters_of_battle, sisters_of_silence, inquisition, tech_priest, grey_knights, emperor_class_titan
    - assassins/ (culexus, eversor, callidus, vindicare)
  - `row_3_primarchs/` - Primarchs XII-XX (9 individual primarch folders)
    - angron, roboute_guilliman, mortarion, magnus, horus, lorgar, vulkan, corvus_corax, alpharius
  - `chaos_gods/` - Khorne, Tzeentch, Nurgle, Slaanesh
  - `xenos/` - Necrons, Eldar, Tyranids, Tau
- `wall_1_right/` - Traitor primarchs (special art set: fulgrim, angron, magnus, mortarion, lorgar, perturabo) + assassins (venenum, vanus)
- `wall_2_left/` - Chaos champions (sevatar, abaddon, ahriman, kharn) vs Loyalist champions (amit, logan_grimnar, tyberos, sigismund)

**Source Images (original legion collection):**
- `space marine legions/{Legion}/primarch/` - Primarch originals + A4 formatted
- `space marine legions/{Legion}/legionnaire/1/` and `/4/` - Legionnaire images
- Files: `{Legion}_primarch.jpg` and `{Legion}_primarch_A4.jpeg`

### Processing Pipelines

**Legionnaires (2-script pipeline):**
1. **format_for_a4_printing.py** - Resizes to A4, creates temp folders
2. **reorganize_images.py** - Consolidates into folders 1 and 4, cleans up

**Primarchs (2-script pipeline):**
1. **rename_primarchs.py** - Standardizes to `{Legion}_primarch.{ext}`
2. **format_primarchs_a4.py** - Resizes to A4, saves as `*_A4.jpeg` in same folder

Both pipelines are idempotent and safe to re-run.

### Key Technical Details

**A4 Specifications:**
- Exact dimensions: 2480×3508 pixels (210mm × 297mm @ 300 DPI)
- Quality: 95% JPEG compression
- Resampling: Lanczos (high quality)
- No aspect ratio preservation - images stretch to fill completely

**Image Processing Behavior:**
- Original images are renamed but pixel data never modified
- Converts all images to RGB mode for JPEG compatibility during A4 formatting
- Scripts are idempotent - safe to run multiple times
- Both original and formatted versions stored in same folder for easy access

## Important Notes

**Wall Layout:**
- Total: 55 A4 posters capacity across 3 walls (39 + 8 + 8)
- Main wall: Emperor centered at position 5 with Imperial forces flanking
- Chaos Gods at corners (spots 10 & 13) of rows 1 & 3
- Primarchs: Individual folders by primarch name (18 folders, currently empty - awaiting new image set)
- Current status: 37 posters completed with A4 versions, 18 primarch folders empty

**Source Collection:**
- 18 Space Marine legions with primarchs
- Legionnaire subfolders: only `1` and `4` are processed by scripts (hardcoded)
- Print-ready files have `_A4` suffix
- All scripts work on `space marine legions/` structure, not wall layout folders
