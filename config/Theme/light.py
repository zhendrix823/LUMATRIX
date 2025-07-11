# config/theme/light.py

LIGHT = {
    'background': '#FFFFFF',      # Clean white
    'text': '#1A1A1A',            # Near black for max legibility
    'font_family': 'sans-serif',

    'table_border': '#DDDDDD',
    'input_bg': '#FFFFFF',
    'input_text': '#1A1A1A',
    'input_border': '#1677FF',    # Accent blue for focus/active border

    'accent': {
        'color': '#1677FF',       # Bright blue accent
        'on_dark': '#1677FF',     # Accent as text on dark (rare in light mode)
        'on_light': '#000000'     # Text on accent BG → black stays clearer than white here
    },

    'button': {
        'inactive_bg': '#F5F5F5',   # Light grey for inactive
        'inactive_text': '#1A1A1A',
        'active_bg': '#1677FF',
        'active_text': '#FFFFFF'    # Exception: white text on solid blue is readable here
    }
}