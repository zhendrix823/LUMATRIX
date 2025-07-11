# config/theme/__init__.py

from .slate import SLATE
from .matrix import MATRIX
from .colorful import COLORFUL

# 🔑 All available themes:
THEMES = {
    'slate': SLATE,
    'matrix': MATRIX,
    'colorful': COLORFUL
}

# ✅ Function your app calls — returns the active theme
def get_theme_styles():
    # 👇 Pick which one is active by changing this key:
    return THEMES['slate']  # 'slate', 'matrix', or 'colorful'