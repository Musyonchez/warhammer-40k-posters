# Warhammer 40K Poster Wall - A4 Layout

Organized collection of Warhammer 40K artwork for a multi-wall A4 poster display. Features Space Marines, Primarchs, Imperial forces, Chaos Gods, Xenos, and legendary champions.

## 📁 Project Structure

### Wall Layout Organization
```
pinterest_wall_prints/
├── main_wall/                # 13×3 grid (39 A4 posters)
│   ├── row_1_primarchs/      # Primarchs I, III-X (9 primarchs)
│   │   ├── lion_el_jonson/       # I - Dark Angels
│   │   ├── fulgrim/              # III - Emperor's Children
│   │   ├── perturabo/            # IV - Iron Warriors
│   │   ├── jaghatai_khan/        # V - White Scars
│   │   ├── leman_russ/           # VI - Space Wolves
│   │   ├── rogal_dorn/           # VII - Imperial Fists
│   │   ├── konrad_curze/         # VIII - Night Lords
│   │   ├── sanguinius/           # IX - Blood Angels
│   │   └── ferrus_manus/         # X - Iron Hands
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
│   │   └── assassins/            # Culexus, Eversor, Callidus, Vindicare
│   ├── row_3_primarchs/      # Primarchs XII-XX (9 primarchs)
│   │   ├── angron/               # XII - World Eaters
│   │   ├── roboute_guilliman/    # XIII - Ultramarines
│   │   ├── mortarion/            # XIV - Death Guard
│   │   ├── magnus/               # XV - Thousand Sons
│   │   ├── horus/                # XVI - Sons of Horus
│   │   ├── lorgar/               # XVII - Word Bearers
│   │   ├── vulkan/               # XVIII - Salamanders
│   │   ├── corvus_corax/         # XIX - Raven Guard
│   │   └── alpharius/            # XX - Alpha Legion
│   ├── chaos_gods/           # Khorne, Tzeentch, Nurgle, Slaanesh
│   └── xenos/                # Necrons, Eldar, Tyranids, Tau
├── wall_1_right/             # 2×4 grid (8 A4 posters)
│   ├── traitor_primarchs/    # Fulgrim, Angron, Magnus, Mortarion, Lorgar, Perturabo
│   └── assassins/            # Venenum, Vanus temples
└── wall_2_left/              # 2×4 grid (8 A4 posters)
    ├── chaos_champions/      # Abaddon, Kharn, Ahriman, Sevatar
    └── loyalist_champions/   # Sigismund, Tyberos, Logan Grimnar, Amit
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

**Row 1 (Top - Spots 1-13):**
1-9: Primarchs I, III-X (Lion, Fulgrim, Perturabo, Jaghatai, Russ, Dorn, Curze, Sanguinius, Ferrus)
10: Khorne | 11: Necrons | 12: Eldar | 13: Tzeentch

**Row 2 (Middle - Spots 1-13):**
1: Inquisition | 2: Sisters of Battle | 3: Sisters of Silence | 4: Constantin Valdor | 5: **THE EMPEROR** | 6: Malcador | 7: Tech Priest | 8: Grey Knights | 9-12: Four Assassins (Vindicare, Callidus, Eversor, Culexus) | 13: Emperor-class Titan

**Row 3 (Bottom - Spots 1-13):**
1-9: Primarchs XII-XX (Angron, Guilliman, Mortarion, Magnus, Horus, Lorgar, Vulkan, Corax, Alpharius)
10: Nurgle | 11: Tyranids | 12: Tau | 13: Slaanesh

### Wall 1 - Right (2×4 = 8 posters)

**Traitor Primarchs (Rows 1-3, special art set):**
Row 1: Fulgrim | Perturabo
Row 2: Angron | Lorgar
Row 3: Mortarion | Magnus

**Assassin Temples (Row 4):**
Row 4: Venenum | Vanus

### Wall 2 - Left (2×4 = 8 posters)

**Chaos vs Loyalist Champions:**
Row 1: Abaddon | Sigismund
Row 2: Tyberos | Khârn
Row 3: Ahriman | Logan Grimnar
Row 4: Amit | Sevatar

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
# Add images to: main_wall/row_1_primarchs/{primarch_name}/ or
#                main_wall/row_3_primarchs/{primarch_name}/
venv/bin/python3 scripts/rename_new_images.py
venv/bin/python3 scripts/format_new_images_a4.py
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
