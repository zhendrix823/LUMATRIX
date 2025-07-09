import os
import json

# ✅ Load brands from JSON instead of hardcoding
PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BRANDS_FILE = os.path.join(PROJECT_PATH, "brands.json")

def load_brand_keywords():
    if not os.path.exists(BRANDS_FILE):
        print(f"⚠️ brands.json not found — using empty brand map.")
        return {}
    with open(BRANDS_FILE, "r") as f:
        return json.load(f)

BRAND_KEYWORDS = load_brand_keywords()