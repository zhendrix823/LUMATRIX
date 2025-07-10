#!/usr/bin/env python3

import os
import json
import webview
from lumatrix_config import get_theme_styles

print("🤘🏻🖤NEO, Im LEARNING!🤘🏻🖤")

PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANUALS_PATH = os.path.join(PROJECT_PATH, "manuals")
UNSORTED_PATH = os.path.join(MANUALS_PATH, "_Unsorted")
BRANDS_FILE = os.path.join(PROJECT_PATH, "brands.json")

def load_brands():
    if not os.path.exists(BRANDS_FILE):
        print("⚠️  No brands.json found. Starting fresh.")
        return {}
    with open(BRANDS_FILE, "r") as f:
        return json.load(f)

def save_brands(data):
    with open(BRANDS_FILE, "w") as f:
        json.dump(data, f, indent=2)
    print("✅ brands.json updated!")

def find_unmatched_files():
    files = []
    if not os.path.exists(UNSORTED_PATH):
        print(f"⚠️  '_Unsorted' folder not found: {UNSORTED_PATH}")
        return files
    for file in os.listdir(UNSORTED_PATH):
        if file.lower().endswith(".pdf"):
            files.append(file)
    return files

def build_html(files, brands):
    theme = get_theme_styles()

    brand_options = sorted(list(brands.keys()))
    options_html = "".join([f"<option value='{b}'>{b}</option>" for b in brand_options])

    rows = ""
    for f in files:
        rows += f"""
        <tr>
            <td>{f}</td>
            <td>
                <select name="{f}">
                    <option value="">-- Select Brand --</option>
                    {options_html}
                    <option value="__new__">Add New Brand...</option>
                </select>
            </td>
            <td>
                <input type="text" name="{f}_newbrand" placeholder="New Brand (if adding)">
                <input type="text" name="{f}_model" placeholder="Model Name">
            </td>
        </tr>
        """

    html = f"""
    <html>
    <head>
        <title>LUMATRIX Brand Admin</title>
        <style>
            body {{
                background: {theme['background']};
                color: {theme['text']};
                font-family: {theme['font_family']};
                padding: 20px;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
            }}
            td {{
                padding: 4px;
                border-bottom: 1px solid {theme['table_border']};
            }}
            select, input {{
                background: {theme['input_bg']};
                color: {theme['input_text']};
                border: 1px solid {theme['border']};
            }}
            button {{
                background: {theme['button_bg']};
                color: {theme['button_text']};
                padding: 6px 12px;
                margin-top: 10px;
                border: none;
                cursor: pointer;
            }}
        </style>
    </head>
    <body>
        <h1>🔍 Train Brand Map – Unmatched Files</h1>
        <form id="brandForm">
            <table>
                {rows}
            </table>
            <button type="button" onclick="save()">Save Brands</button>
        </form>
        <script>
            function save() {{
                const selects = document.querySelectorAll("select");
                const data = [];
                selects.forEach(s => {{
                    const file = s.name;
                    const brand = s.value;
                    const newBrand = document.querySelector(`[name='${{file}}_newbrand']`).value.trim();
                    const model = document.querySelector(`[name='${{file}}_model']`).value.trim();
                    data.push({{ file, brand, newBrand, model }});
                }});
                window.pywebview.api.saveBrands(data).then(() => {{
                    alert("✅ brands.json updated!");
                }});
            }}
        </script>
    </body>
    </html>
    """
    return html

class Api:
    def saveBrands(self, data):
        brands = load_brands()
        for entry in data:
            brand = entry['brand']
            if brand == "__new__":
                brand = entry['newBrand']
            if not brand:
                continue
            if brand not in brands:
                brands[brand] = []
            keyword = entry['model']
            if keyword and keyword not in brands[brand]:
                brands[brand].append(keyword)
        save_brands(brands)

if __name__ == "__main__":
    unmatched = find_unmatched_files()
    if not unmatched:
        print("✅ No unmatched files in _Unsorted/.")
    else:
        brands = load_brands()
        html = build_html(unmatched, brands)
        api = Api()
        webview.create_window("LUMATRIX Brand Admin", html=html, width=900, height=600)
        webview.start(http_server=True, gui="qt", debug=True)