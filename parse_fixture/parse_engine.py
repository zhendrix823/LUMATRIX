#!/usr/bin/env python3

"""
parse_engine.py

🧩 LUMATRIX Parse Engine
Searches 'To_Process' folder, matches files to brand keywords, moves them to brand folders.
Unmatched files go to 'Unsorted'.
"""

import os
import shutil
import json

# === CONFIG ===
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
PROJECT_PATH = os.path.dirname(PROJECT_PATH)  # go up one level from /parse_fixture/
TO_PROCESS_PATH = os.path.join(PROJECT_PATH, "_To_Process")
MANUALS_PATH = os.path.join(PROJECT_PATH, "manuals")
UNSORTED_PATH = os.path.join(MANUALS_PATH, "Unsorted")
BRANDS_FILE = os.path.join(PROJECT_PATH, "brands.json")

# === Ensure folders exist ===
def ensure_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"✅ Created missing folder: {path}")

ensure_folder(TO_PROCESS_PATH)
ensure_folder(UNSORTED_PATH)

# === Load brand keywords ===
def load_brand_keywords():
    if not os.path.exists(BRANDS_FILE):
        print("⚠️ brands.json not found.")
        return {}
    with open(BRANDS_FILE, "r") as f:
        return json.load(f)

BRAND_KEYWORDS = load_brand_keywords()

# === Parse files ===
def parse_files():
    processed = 0
    for filename in os.listdir(TO_PROCESS_PATH):
        file_lower = filename.lower()
        matched_brand = None
        for brand, keywords in BRAND_KEYWORDS.items():
            for keyword in keywords:
                if keyword.lower() in file_lower:
                    matched_brand = brand
                    break
            if matched_brand:
                break

        src_path = os.path.join(TO_PROCESS_PATH, filename)

        if matched_brand:
            brand_folder = os.path.join(MANUALS_PATH, matched_brand)
            ensure_folder(brand_folder)
            dst_path = os.path.join(brand_folder, filename)
            print(f"🔵 Matched '{filename}' → {matched_brand}")
        else:
            dst_path = os.path.join(UNSORTED_PATH, filename)
            print(f"🟡 Unmatched '{filename}' → Unsorted")

        shutil.move(src_path, dst_path)
        processed += 1

    if processed == 0:
        print("✅ No files to process.")
    else:
        print(f"✅ Done! Processed {processed} file(s).")

# === MAIN ===
if __name__ == "__main__":
    print("🚀 Starting parse engine...")
    parse_files()