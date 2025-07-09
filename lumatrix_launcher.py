# ✅ Full lumatrix_launcher.py for LUMATRIX v0.3.5 — pipeline + brand sorting

import os
import sys
import glob

# Import your modules
import unsorted_review_ui as unsorted_ui
import parse_fixture.parse_engine as parse_engine

# --------------------------------------

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
TO_PROCESS = os.path.join(PROJECT_ROOT, "_To_Process")
MANUALS_PATH = os.path.join(PROJECT_ROOT, "manuals")
UNSORTED_PATH = os.path.join(MANUALS_PATH, "_Unsorted")

def main():
    print("🌸 Launching LUMATRIX v0.3.5...")

    # Check _To_Process
    if not os.path.exists(TO_PROCESS):
        print(f"⚠️ '_To_Process' folder not found: {TO_PROCESS}")
        sys.exit(1)

    # Make sure manuals and _Unsorted exist
    if not os.path.exists(MANUALS_PATH):
        os.makedirs(MANUALS_PATH)
        print(f"✅ Created manuals/ folder.")

    if not os.path.exists(UNSORTED_PATH):
        os.makedirs(UNSORTED_PATH)
        print(f"✅ Created _Unsorted/ folder inside manuals/.")

    # Get unsorted PDFs
    pdf_files = [os.path.basename(f) for f in glob.glob(os.path.join(TO_PROCESS, "*.pdf"))]

    if not pdf_files:
        print("✅ No unsorted PDFs found — nothing to review.")
        return

    print(f"✅ Using _To_Process folder at: {TO_PROCESS}")
    print(f"✅ Found {len(pdf_files)} unsorted PDFs.")
    for f in pdf_files:
        print(f"   • {f}")

    # Open the unsorted reviewer
    def after_review():
        print("✅ Reviewer closed — moving files to _Unsorted...")
        for file_name in pdf_files:
            src = os.path.join(TO_PROCESS, file_name)
            dest = os.path.join(UNSORTED_PATH, file_name)
            if os.path.exists(src):
                os.rename(src, dest)
                print(f"   ➡️ Moved {file_name} to _Unsorted/")
            else:
                print(f"   ⚠️ File not found in _To_Process: {file_name}")

        print("✅ Files moved. Running brand sort next...")
        parse_engine.main()
        print("✅ LUMATRIX run complete.")

    # Attach after_review to the UI
    unsorted_ui.run(pdf_files, after_review)

# --------------------------------------

if __name__ == "__main__":
    main()