# main.py

import sys
import os
sys.path.insert(0, os.path.abspath("."))  # ✅ Add current dir to sys.path

from parse_fixture.runner import main # ✅ Now this will work

if __name__ == "__main__":
    print("🌸 Launching LUMATRIX v0.3.5...")

    try:
        main()
    except Exception as e:
        print("❌ Error during launch:", e)