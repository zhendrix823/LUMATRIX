# theme_config.py

THEMES = {
    "Dark": {
        "background": "#121212",
        "text_primary": "#FFFFFF",
        "text_secondary": "#AAAAAA",
        "accent": "#00FF66",
        "button_bg": "#00FF66",
        "button_text": "#000000",
        "input_bg": "#1E1E1E",
        "input_text": "#FFFFFF",
        "font_family": "Arial, sans-serif",
        "header_font_size": "28px",
        "body_font_size": "16px",
        "toast_text_color": "#FFFFFF",
        "toast_bg": "#00FF66",
    }
}

def get_theme_styles(name="Dark"):
    return THEMES.get(name, THEMES["Dark"])