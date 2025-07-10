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
from lumatrix_config import get_theme_styles

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
      select, input[type='text'] {{
        background: {theme['input_bg']};
        color: {theme['input_text']};
        border: 1px solid {theme['input_border']};
        width: 95%;
      }}
      input[type='checkbox'] {{
        transform: scale(1.2);
      }}
      #apply {{
        background: lightgray;
        color: black;
        padding: 8px 16px;
        margin-top: 10px;
        border: none;
        cursor: not-allowed;
      }}
      #apply.active {{
        background: {theme['button_bg']};
        color: {theme['button_text']};
        cursor: pointer;
      }}
      #toast {{
        display: none;
        position: fixed;
        bottom: 30px;
        left: 50%;
        transform: translateX(-50%);
        background: {theme['accent']};
        color: {theme['background']};
        padding: 10px 20px;
        border-radius: 4px;
        font-weight: bold;
      }}
    </style>
    </head>
    <body>
      <h1>LUMATRIX Brand Admin</h1>
      <table>
        <tr><th>Filename</th><th>Manufacturer</th><th>Model Name</th><th>Ignore</th></tr>
    """

    for file in files:
        html += f"<tr>"
        html += f"<td>{file}</td>"

        html += "<td><select onchange='enableApply()'>"
        html += "<option value=''>Select one</option>"
        for brand in brands.keys():
            html += f"<option value='{brand}'>{brand}</option>"
        html += "</select></td>"

        html += "<td><input type='text' oninput='enableApply()' /></td>"
        html += "<td><input type='checkbox' onchange='enableApply()' /></td>"
        html += "</tr>"

    html += """
      </table>
      <button id="apply" onclick="applyChanges()">Apply</button>
      <div id="toast">Changes Applied ✅</div>

      <script>
        let applyBtn = document.getElementById('apply');

        function enableApply() {
          applyBtn.classList.add('active');
          applyBtn.style.cursor = 'pointer';
        }

        function applyChanges() {
          if (!applyBtn.classList.contains('active')) return;

          // Here you’d call the API to save brands, omitted for brevity.
          showToast();
          applyBtn.classList.remove('active');
          applyBtn.style.cursor = 'not-allowed';
        }

        function showToast() {
          let toast = document.getElementById('toast');
          toast.style.display = 'block';
          setTimeout(() => {{
            toast.style.display = 'none';
          }}, 2000);
        }
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
            height=650
        )
        webview.start(http_server=True, gui="qt", debug=True)