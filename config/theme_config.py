# config/theme_config.py

def get_theme_styles():
    """
    Theme style guide for the LUMATRIX app.
    This file defines all colors and styles used across the UI.
    """
    return {
        "background": "#1e1e1e",      # Dark background
        "text": "#f0f0f0",            # Light text
        "font_family": "Arial, sans-serif",
        "table_border": "#555555",    # Table border color
        "input_bg": "#2e2e2e",        # Input fields background
        "input_text": "#f0f0f0",      # Input fields text color
        "input_border": "#888888",    # Input field border color
        "button_bg": "#3e3e3e",       # Button background color
        "button_text": "#f0f0f0",     # Button text color
        "accent": "#00ff00"           # ✅ Accent color for highlights and active states
    }