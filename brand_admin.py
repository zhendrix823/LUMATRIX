#!/usr/bin/env python3

"""
brand_admin.py

🗂️ CLI helper to review unmatched files in _Unsorted/ and update brands.json.
Run: python3 brand_admin.py
"""

import os
import json

# === CONFIG ===
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
MANUALS_PATH = os.path.join(PROJECT_PATH, "manuals")
UNSORTED_PATH = os.path.join(MANUALS_PATH, "_Unsorted")
BRANDS_FILE = os.path.join(PROJECT_PATH, "brands.json")

# === Load brand map ===
def load_brands():
    if not os.path.exists(BRANDS_FILE):
        print("⚠️ No brands.json found. Starting fresh.")
        return {}
    with open(BRANDS_FILE, "r") as f:
        return json.load(f)

def save_brands(data):
    with open(BRANDS_FILE, "w") as f:
        json.dump(data, f, indent=2)
    print("✅ brands.json updated!")

# === Find unmatched files ===
def find_unmatched_files():
    files = []
    for file in os.listdir(UNSORTED_PATH):
        if file.lower().endswith(".pdf"):
            files.append(file)
    return files

# === Match file to brand ===
def match_brand(file, brands):
    file_lower = file.lower()
    for brand, keywords in brands.items():
        for keyword in keywords:
            if keyword.lower() in file_lower:
                return brand
    return None

# === CLI Trainer ===
def admin_loop():
    brands = load_brands()
    files = find_unmatched_files()

    if not files:
        print("✅ No unmatched files in _Unsorted/. All done!")
        return

    print("\n🔍 Unmatched PDFs in _Unsorted/:")
    for i, file in enumerate(files, 1):
        print(f"  {i}. {file}")

    for file in files:
        current = match_brand(file, brands)
        if current:
            print(f"\n✅ {file} already matches: {current}")
            continue

        print(f"\n⚡️ {file} has no brand match.")
        print("Known brands:")
        for idx, brand in enumerate(brands.keys(), 1):
            print(f"  {idx}. {brand}")

        choice = input("Select a brand number or type 'new': ").strip()

        if choice.lower() == "new":
            new_brand = input("Enter new brand name: ").strip()
            if new_brand not in brands:
                brands[new_brand] = []
            keyword = input(f"Enter keyword/alias for '{new_brand}' to match: ").strip()
            brands[new_brand].append(keyword)
            print(f"✅ Added new brand '{new_brand}' with keyword '{keyword}'")
        else:
            try:
                idx = int(choice) - 1
                brand = list(brands.keys())[idx]
                keyword = input(f"Enter keyword/alias for '{brand}' to match: ").strip()
                brands[brand].append(keyword)
                print(f"✅ Added keyword '{keyword}' to brand '{brand}'")
            except (ValueError, IndexError):
                print("⚠️ Invalid choice. Skipping this file.")

    save_brands(brands)
    print("\n🎉 Done! Your brand map is now smarter.\n")

if __name__ == "__main__":
    admin_loop()