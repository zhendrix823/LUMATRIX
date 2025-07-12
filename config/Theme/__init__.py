import json
import os
import pprint

from .slate import SLATE
from .matrix import MATRIX
from .colorful import COLORFUL
from .light import LIGHT

THEMES = {
    'slate': SLATE,
    'matrix': MATRIX,
    'colorful': COLORFUL,
    'light': LIGHT
}

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.json")

def get_theme_styles():
    try:
        with open(CONFIG_PATH, "r") as f:
            config = json.load(f)
        theme_name = config.get("active_theme", "slate").lower()
    except Exception:
        theme_name = "slate"

    print("\n🔍 Using theme name:", theme_name)
    print("🔍 Available THEMES:", THEMES.keys())

    theme = THEMES.get(theme_name, SLATE)
    print("🔍 FINAL theme loaded:")
    pprint.pprint(theme)

    return theme