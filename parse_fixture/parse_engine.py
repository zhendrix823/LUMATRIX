# ✅ Full parse_fixture/parse_engine.py for LUMATRIX v0.3.5
# Now with smart brand sorting from _Unsorted

import os

# Add any brand keywords here
BRAND_KEYWORDS = {
    "Robe": ["Robe", "Robin"],
    "Elation": ["Elation"],
    "Martin": ["Martin", "MAC", "Aura"]
}

def main():
    print("🔍 parse_engine.main() is running...")

    PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
    PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)

    MANUALS_PATH = os.path.join(PROJECT_ROOT, "manuals")
    UNSORTED_PATH = os.path.join(MANUALS_PATH, "_Unsorted")

    if not os.path.exists(UNSORTED_PATH):
        print(f"⚠️ '_Unsorted' folder not found: {UNSORTED_PATH}")
        return

    files = [f for f in os.listdir(UNSORTED_PATH) if f.lower().endswith(".pdf")]
    print(f"🔎 Found {len(files)} PDFs in _Unsorted to sort by brand.")

    if not files:
        print("✅ No files to sort.")
        return

    for file_name in files:
        matched = False
        lower_name = file_name.lower()

        for brand, keywords in BRAND_KEYWORDS.items():
            for keyword in keywords:
                if keyword.lower() in lower_name:
                    brand_folder = os.path.join(MANUALS_PATH, brand)
                    if not os.path.exists(brand_folder):
                        os.makedirs(brand_folder)
                        print(f"✅ Created brand folder: {brand}")

                    src = os.path.join(UNSORTED_PATH, file_name)
                    dest = os.path.join(brand_folder, file_name)
                    os.rename(src, dest)
                    print(f"✅ Moved '{file_name}' to '{brand}/'")
                    matched = True
                    break

            if matched:
                break

        if not matched:
            print(f"⚠️ No brand match for '{file_name}'. Left in _Unsorted/.")

    print("✅ Brand sorting completed.")

if __name__ == "__main__":
    main()