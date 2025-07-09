# ✅ Full lumatrix_launcher.py for LUMATRIX v0.3.5

import os
import sys
import parse_fixture.parse_engine as parse_engine
import unsorted_review_ui as review_ui

def main():
    print("🌸 Launching LUMATRIX v0.3.5...")

    PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
    TO_PROCESS_PATH = os.path.join(PROJECT_ROOT, "_To_Process")

    print(f"✅ Using _To_Process folder at: {TO_PROCESS_PATH}")

    if not os.path.exists(TO_PROCESS_PATH):
        print(f"⚠️ '_To_Process' folder not found: {TO_PROCESS_PATH}")
        sys.exit(1)

    pdf_files = [
        f for f in os.listdir(TO_PROCESS_PATH)
        if f.lower().endswith(".pdf")
    ]

    if not pdf_files:
        print("✅ No unsorted PDFs found — nothing to review.")
    else:
        print(f"✅ Found {len(pdf_files)} unsorted PDFs.")
        for f in pdf_files:
            print(f"   • {f}")

        # Show the review UI
        review_ui.run(pdf_files)

        # After review window closes, run parser
        print("✅ Closing reviewer — running parser next.")
        parse_engine.main()

    print("✅ LUMATRIX run complete.")

if __name__ == "__main__":
    main()