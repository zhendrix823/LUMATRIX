#!/usr/bin/env python3

"""
brand_admin_ui.py

🧩 LUMATRIX Brand Admin UI
CLI + UI helper to review unmatched files in Unsorted/ and update brands.json.

Run:
    python3 admin_tools/brand_admin_ui.py
"""

import os
import json
import webview
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.theme_config import get_theme_styles

# === CONFIG ===
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
PROJECT_PATH = os.path.dirname(PROJECT_PATH)  # up one level to v0_3_5
MANUALS_PATH = os.path.join(PROJECT_PATH, "manuals")
UNSORTED_PATH = os.path.join(MANUALS_PATH, "Unsorted")
BRANDS_FILE = os.path.join(PROJECT_PATH, "brands.json")

# === HELPERS ===
def find_unmatched_files():
    unmatched = []
    for filename in os.listdir(UNSORTED_PATH):
        if filename.endswith(".pdf"):
            unmatched.append(filename)
    return unmatched

def load_brands():
    with open(BRANDS_FILE, "r") as f:
        return json.load(f)

def save_brands(data):
    with open(BRANDS_FILE, "w") as f:
        json.dump(data, f, indent=4)

# === BUILD HTML ===
def build_html(files, brands):
    theme = get_theme_styles()

    html = f"""
    <!DOCTYPE html>
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
        border: 1px solid {theme['table_border']};
      }}
      th, td {{
        padding: 8px;
        border: 1px solid {theme['table_border']};
      }}
      select, input {{
        background: {theme['input_bg']};
        color: {theme['input_text']};
        border: 1px solid {theme['input_border']};
      }}
      button {{
        background: {theme['accent']};
        color: {theme['button_text']};
        padding: 6px 12px;
        margin-top: 10px;
        border: none;
        cursor: pointer;
      }}
      button:disabled {{
        background: grey;
        cursor: not-allowed;
      }}
    </style>
    </head>
    <body>
      <h1>LUMATRIX Brand Admin</h1>
      <table>
        <tr><th>Filename</th><th>Manufacturer</th><th>Model Name</th></tr>
    """

    for idx, file in enumerate(files):
        html += f"<tr><td>{file}</td><td><select class='brand-select' data-idx='{idx}'>"
        html += f"<option value=''>Select one</option>"
        for brand in brands.keys():
            html += f"<option value='{brand}'>{brand}</option>"
        html += "</select></td><td><input type='text' class='model-input' data-idx='{idx}' placeholder='Model name'></td></tr>"

    html += """
      </table>
      <button id="apply-btn" disabled>Apply</button>

      <script>
        const selects = document.querySelectorAll('.brand-select');
        const applyBtn = document.getElementById('apply-btn');

        selects.forEach(select => {
          select.addEventListener('change', () => {
            let anySelected = false;
            selects.forEach(s => {
              if (s.value) anySelected = true;
            });
            applyBtn.disabled = !anySelected;
          });
        });

        applyBtn.addEventListener('click', () => {
          let data = [];
          selects.forEach(select => {
            const idx = select.dataset.idx;
            const brand = select.value;
            const model = document.querySelector(`.model-input[data-idx='${idx}']`).value.trim();
            if (brand) {
              data.push({ brand, model });
            }
          });
          if (data.length > 0) {
            window.pywebview.api.saveBrands(data).then(() => {
              alert('Brands updated!');
            });
          }
        });
      </script>
    </body>
    </html>
    """
    return html

# === API ===
class Api:
    def saveBrands(self, data):
        brands = load_brands()
        for entry in data:
            brand = entry['brand']
            if not brand:
                continue
            if brand not in brands:
                brands[brand] = []
            keyword = entry['model']
            if keyword and keyword not in brands[brand]:
                brands[brand].append(keyword)
        save_brands(brands)

# === MAIN ===
if __name__ == "__main__":
    unmatched = find_unmatched_files()
    if not unmatched:
        print("✅ No unmatched files in Unsorted.")
    else:
        brands = load_brands()
        html = build_html(unmatched, brands)
        api = Api()
        webview.create_window(
            "LUMATRIX Brand Admin",
            html=html,
            width=1000,
            height=600
        )
        webview.start(http_server=True, gui="qt", debug=True)