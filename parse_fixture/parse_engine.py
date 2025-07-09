# ✅ Full parse_fixture/parse_engine.py for LUMATRIX v0.3.5
# With smart _Unsorted folder

import os

def main():
    print("🔍 parse_engine.main() is running...")

    PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
    PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)

    TO_PROCESS_PATH = os.path.join(PROJECT_ROOT, "_To_Process")
    MANUALS_PATH = os.path.join(PROJECT_ROOT, "manuals")
    UNSORTED_PATH = os.path.join(MANUALS_PATH, "_Unsorted")

    print(f"✅ Using _To_Process: {TO_PROCESS_PATH}")

    if not os.path.exists(TO_PROCESS_PATH):
        print(f"⚠️ '_To_Process' folder not found: {TO_PROCESS_PATH}")
        return

    # Make sure manuals/ and _Unsorted/ exist
    if not os.path.exists(MANUALS_PATH):
        os.makedirs(MANUALS_PATH)
        print(f"✅ Created manuals/ folder.")
    if not os.path.exists(UNSORTED_PATH):
        os.makedirs(UNSORTED_PATH)
        print(f"✅ Created _Unsorted/ folder inside manuals/.")

    files = [f for f in os.listdir(TO_PROCESS_PATH) if f.lower().endswith(".pdf")]
    print(f"🔎 Found {len(files)} PDFs to parse.")

    if not files:
        print("✅ No files to parse.")
        return

    for file_name in files:
        src = os.path.join(TO_PROCESS_PATH, file_name)
        dest = os.path.join(UNSORTED_PATH, file_name)
        print(f"➡️ Moving {file_name} from _To_Process to manuals/_Unsorted/...")
        try:
            os.rename(src, dest)
            print(f"✅ Moved {file_name} to manuals/_Unsorted/")
        except Exception as e:
            print(f"❌ Failed to move {file_name}: {e}")

    print("✅ parse_engine.main() completed.")

if __name__ == "__main__":
    main()