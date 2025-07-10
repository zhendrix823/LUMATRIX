import os

# ------------------------------
# 🗂️ Paths
# ------------------------------
PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UNSORTED_PATH = os.path.join(PROJECT_PATH, "manuals", "Unsorted")

# ------------------------------
# ✅ Make sure Unsorted folder exists
# ------------------------------
def ensure_unsorted_folder():
    if not os.path.exists(UNSORTED_PATH):
        os.makedirs(UNSORTED_PATH)
        print(f"✅ Created missing folder: {UNSORTED_PATH}")
    else:
        print(f"✅ Unsorted folder exists: {UNSORTED_PATH}")

# ------------------------------
# 🔍 Your actual parse logic
# ------------------------------
def parse_fixtures():
    print("🚀 Parsing fixtures...")
    # TODO: Add your actual parsing logic here
    # Example:
    for filename in os.listdir(UNSORTED_PATH):
        print(f"📄 Found file: {filename}")
    print("✅ Parsing complete!")

# ------------------------------
# 🚦 Main
# ------------------------------
if __name__ == "__main__":
    ensure_unsorted_folder()
    parse_fixtures()