#!/usr/bin/env python3

"""
style_guide.py

🧩 Generates a visual style guide for your current THEME config.
Run:
    python3 style_guide.py
Then open the output HTML file in your browser!
"""

from theme_config import get_theme_styles

def build_style_guide_html():
    theme = get_theme_styles()

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>LUMATRIX Style Guide</title>
        <style>
            body {{
                background: {theme['background']};
                color: {theme['text_primary']};
                font-family: {theme['font_family']};
                padding: 40px;
            }}
            h1 {{
                font-size: {theme['header_font_size']};
                color: {theme['text_primary']};
            }}
            h2 {{
                font-size: 24px;
                color: {theme['text_secondary']};
            }}
            p {{
                font-size: {theme['body_font_size']};
                color: {theme['text_secondary']};
            }}
            .accent {{
                color: {theme['accent']};
            }}
            .button {{
                background: {theme['button_bg']};
                color: {theme['button_text']};
                padding: 10px 20px;
                border: none;
                cursor: pointer;
                margin: 10px 0;
            }}
            .input {{
                background: {theme['input_bg']};
                color: {theme['input_text']};
                padding: 8px;
                border: 1px solid {theme['accent']};
                margin: 10px 0;
            }}
            .toast {{
                background: {theme['toast_bg']};
                color: {theme['toast_text_color']};
                padding: 10px;
                display: inline-block;
                margin: 10px 0;
            }}
            .swatch {{
                display: inline-block;
                width: 100px;
                height: 30px;
                margin-right: 10px;
                border: 1px solid #333;
            }}
        </style>
    </head>
    <body>
        <h1>LUMATRIX Style Guide</h1>
        <p>This page shows all theme variables in context.</p>

        <h2>Colors</h2>
        <div>
            <div class="swatch" style="background:{theme['background']};"></div> Background<br>
            <div class="swatch" style="background:{theme['text_primary']};"></div> Text Primary<br>
            <div class="swatch" style="background:{theme['text_secondary']};"></div> Text Secondary<br>
            <div class="swatch" style="background:{theme['accent']};"></div> Accent<br>
            <div class="swatch" style="background:{theme['button_bg']};"></div> Button BG<br>
            <div class="swatch" style="background:{theme['input_bg']};"></div> Input BG<br>
            <div class="swatch" style="background:{theme['toast_bg']};"></div> Toast BG<br>
        </div>

        <h2>Typography</h2>
        <h1>Header Text</h1>
        <p>Body text example showing text_secondary color.</p>
        <p class="accent">Accent text example.</p>

        <h2>Buttons & Inputs</h2>
        <button class="button">Button Example</button><br>
        <input class="input" placeholder="Input Example">

        <h2>Toast Example</h2>
        <div class="toast">This is a toast message</div>

        <h2>Font</h2>
        <p>Font family: {theme['font_family']}</p>
        <p>Header font size: {theme['header_font_size']}</p>
        <p>Body font size: {theme['body_font_size']}</p>
    </body>
    </html>
    """

    return html

if __name__ == "__main__":
    html = build_style_guide_html()
    with open("style_guide.html", "w") as f:
        f.write(html)
    print("✅ Style guide generated: style_guide.html")