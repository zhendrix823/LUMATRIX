#!/usr/bin/env python3

"""
parse_engine.py

📂 LUMATRIX Parse Engine
- Sort fixture manuals by brand using brands.json
- Unmatched files go to manuals/Unsorted
"""

import os
import shutil
import json

# === CONFIG ===
PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANUALS_PATH = os.path.join(PROJECT_PATH, "manuals")
TO_PROCESS_PATH = os.path.join(MANUALS_PATH, "To_Process")
UNSORTED_PATH = os.path.join(MANUALS_PATH, "Unsorted")
BRANDS_FILE = os.path.join(PROJECT_PATH, "brands.json")

# === Ensure required folders exist ===
for path in [TO_PROCESS_PATH, UNSORTED_PATH]:
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"✅ Created missing folder: {path}")

# === Load brands.json ===
if not os.path.exists(BRANDS_FILE):
    print(f"⚠️ brands.json not found. Nothing to parse.")
    exit(0)

with open(BRANDS_FILE, "r") as f:
    BRAND_KEYWORDS = json.load(f)

# === Parse ===
print("🚀 Starting parse engine...")
files = os.listdir(TO_PROCESS_PATH)
if not files:
    print("✅ No files to process.")
    exit(0)

for filename in files:
    filepath = os.path.join(TO_PROCESS_PATH, filename)
    moved = False

    if not filename.lower().endswith(".pdf"):
        print(f"⚠️ Skipped (not a PDF): {filename}")
        continue

    for brand, keywords in BRAND_KEYWORDS.items():
        for keyword in keywords:
            if keyword.lower() in filename.lower():
                dest_dir = os.path.join(MANUALS_PATH, brand)
                if not os.path.exists(dest_dir):
                    os.makedirs(dest_dir)
                    print(f"✅ Created folder for {brand}: {dest_dir}")

                shutil.move(filepath, os.path.join(dest_dir, filename))
                print(f"📂 Moved: {filename} -> {brand}/")
                moved = True
                break
        if moved:
            break

    if not moved:
        shutil.move(filepath, os.path.join(UNSORTED_PATH, filename))
        print(f"📁 Unmatched: {filename} -> Unsorted/")

print("✅ Parsing complete!")