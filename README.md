# Warhammer 40K Poster Wall - A4 Layout

Organized collection of Warhammer 40K artwork for a multi-wall A4 poster display. Features Space Marines, Primarchs, Imperial forces, Chaos Gods, Xenos, and legendary champions.

## 📁 Project Structure

### Wall Layout Organization
```
pinterest_wall_prints/
├── main_wall/                # 13×3 grid (39 A4 posters)
│   ├── row_1_primarchs/      # Primarchs I-X (9 legions)
│   ├── row_2_emperor_forces/ # Emperor & Imperial organizations
│   │   ├── emperor/
│   │   ├── constantine_valdor/
│   │   ├── malcador/
│   │   ├── sisters_of_battle/
│   │   ├── sisters_of_silence/
│   │   ├── inquisition/
│   │   ├── tech_priest/
│   │   ├── grey_knights/
│   │   ├── emperor_class_titan/
│   │   └── assassins/        # 4 main temples
│   ├── row_3_primarchs/      # Primarchs XII-XX (9 legions)
│   ├── chaos_gods/           # Khorne, Tzeentch, Nurgle, Slaanesh
│   └── xenos/                # Necrons, Eldar, Tyranids, Tau
├── wall_1_right/             # 2×4 grid (8 A4 posters)
│   ├── traitor_primarchs/    # Special art set (6 primarchs)
│   └── assassins/            # Venenum, Vanus temples
└── wall_2_left/              # 2×4 grid (8 A4 posters)
    ├── chaos_champions/      # Abaddon, Kharn, Ahriman, Sevatar
    └── loyalist_champions/   # Sigismund, Tyberos, Logan, Amit
```

### Source Images
```
space marine legions/         # Original legion collection
├── {Legion Name}/
│   ├── legionnaire/
│   │   ├── 1/               # Legionnaire pose 1 (original + A4)
│   │   └── 4/               # Legionnaire pose 4 (original + A4)
│   └── primarch/            # Legion primarch (original + A4)
scripts/                     # A4 processing scripts
venv/                        # Python virtual environment
```

## 🖨️ Wall Layout

### Main Wall (13×3 = 39 posters)
**Row 1 (Top):** Primarchs I-X (spots 1-9), Khorne (10), Necrons (11), Eldar (12), Tzeentch (13)
**Row 2 (Middle):** Inquisition, Sisters of Battle, Sisters of Silence, Valdor, **Emperor**, Malcador, Tech Priest, Grey Knights, 4 Assassins, Titan
**Row 3 (Bottom):** Primarchs XII-XX (spots 1-9), Nurgle (10), Tyranids (11), Tau (12), Slaanesh (13)

### Wall 1 - Right (2×4 = 8 posters)
6 Traitor Primarchs (special art set) + 2 Assassin temples

### Wall 2 - Left (2×4 = 8 posters)
4 Chaos Champions vs 4 Loyalist Champions

**Total: 55 A4 posters**

## 🖨️ Printing

All images formatted as A4: 2480×3508px @ 300 DPI
- Printer: A4 paper, 100% scale, no margins
- Quality: Best/High recommended
- Paper: Photo paper for best results

## 🛠️ Scripts

### Legionnaires (subfolders 1 and 4)
```bash
venv/bin/python3 scripts/format_for_a4_printing.py
venv/bin/python3 scripts/reorganize_images.py
```
Resizes to A4 and consolidates original + formatted in same folder.

### Primarchs
```bash
venv/bin/python3 scripts/rename_primarchs.py
venv/bin/python3 scripts/format_primarchs_a4.py
```
Renames to clean pattern and formats for A4 printing.

### Emperor
Already processed - see `emperor/` folder.

**Result:** All folders contain both original and `*_A4.jpeg` print-ready versions.

## 🔄 Workflow

When adding new legionnaire images:
```bash
# Add to: space marine legions/{Legion}/legionnaire/1/ or /4/
venv/bin/python3 scripts/format_for_a4_printing.py
venv/bin/python3 scripts/reorganize_images.py
```

When adding new primarch images:
```bash
# Add to: space marine legions/{Legion}/primarch/
venv/bin/python3 scripts/rename_primarchs.py
venv/bin/python3 scripts/format_primarchs_a4.py
```

## 📋 Source Collection

**Space Marine Legions:** 18 legions with primarchs (stored in `space marine legions/`)

## 💻 Requirements

**Python 3** with **Pillow** library (installed in venv)

## 📐 Technical Details

**A4 Specifications:**
- 2480×3508 pixels (210mm × 297mm @ 300 DPI)
- JPEG quality: 95%
- Resampling: Lanczos (high quality)

## 📝 Notes

**Organization:**
- Primarch images copied from `space marine legions/` to organized wall layout folders
- Original legion structure preserved for reference and processing
- All wall layout folders ready for final poster images

**Image Processing:**
- Images stretched to fit A4 perfectly (no white space, no cropping)
- All scripts are idempotent (safe to re-run)
