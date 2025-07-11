#!/usr/bin/env python3

"""
brand_admin_ui.py

🧩 LUMATRIX Brand Admin UI
HTML-based helper to review unmatched files in manuals/Unsorted/
and update brands.json with matched brands and ignored files.

Run:
    python3 admin_tools/brand_admin_ui.py
"""

import os
import json
import webview
import sys

# Ensure the parent dir is in sys.path for config import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.theme_config import get_theme_styles

# === CONFIG ===
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
PROJECT_PATH = os.path.dirname(PROJECT_PATH)  # go up one level to v0_3_5
MANUALS_PATH = os.path.join(PROJECT_PATH, "manuals")
UNSORTED_PATH = os.path.join(MANUALS_PATH, "Unsorted")
BRANDS_FILE = os.path.join(PROJECT_PATH, "brands.json")

# === HELPERS ===
def find_unmatched_files():
    unmatched = []
    if not os.path.exists(UNSORTED_PATH):
        os.makedirs(UNSORTED_PATH)
    for filename in os.listdir(UNSORTED_PATH):
        if filename.lower().endswith(".pdf"):
            unmatched.append(filename)
    return unmatched

def load_brands():
    if os.path.exists(BRANDS_FILE):
        with open(BRANDS_FILE, "r") as f:
            return json.load(f)
    else:
        return {}

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
      }}
      input[type='checkbox'] {{
        transform: scale(1.2);
      }}
      button {{
        background: {theme['button']['inactive_bg']};
        color: {theme['button']['inactive_text']};
        padding: 6px 12px;
        margin-top: 10px;
        border: none;
        cursor: pointer;
      }}
      button.active {{
        background: {theme['button']['active_bg']};
        color: {theme['button']['active_text']};
      }}
    </style>
    </head>
    <body>
      <h1>LUMATRIX Brand Admin</h1>
      <table>
        <tr><th>Filename</th><th>Manufacturer</th><th>Model</th><th>Ignore</th></tr>
    """

    for file in files:
        html += f"<tr><td>{file}</td>"
        html += f"<td><select onchange='checkApplyActive()'>"
        html += f"<option value=''>Select one</option>"
        for brand in brands.keys():
            html += f"<option value='{brand}'>{brand}</option>"
        html += "</select></td>"
        html += f"<td><input type='text' placeholder='Model name' oninput='checkApplyActive()'></td>"
        html += f"<td><input type='checkbox' onchange='checkApplyActive()'></td></tr>"

    html += """
      </table>
      <button id="applyBtn" onclick="apply()">Apply</button>

      <script>
        function checkApplyActive() {
          const selects = document.querySelectorAll('select');
          const inputs = document.querySelectorAll('input[type="text"]');
          const checks = document.querySelectorAll('input[type="checkbox"]');
          let active = false;

          selects.forEach(s => { if (s.value) active = true; });
          inputs.forEach(i => { if (i.value.trim()) active = true; });
          checks.forEach(c => { if (c.checked) active = true; });

          const btn = document.getElementById('applyBtn');
          if (active) {
            btn.classList.add('active');
          } else {
            btn.classList.remove('active');
          }
        }

        function apply() {
          const rows = document.querySelectorAll('table tr');
          const data = [];

          rows.forEach((row, index) => {
            if (index === 0) return; // skip header
            const cells = row.querySelectorAll('td');
            const modelFile = cells[0].innerText.trim();
            const select = cells[1].querySelector('select');
            const brand = select.value;
            const modelInput = cells[2].querySelector('input[type="text"]');
            const keyword = modelInput.value.trim();
            const ignored = cells[3].querySelector('input[type="checkbox"]').checked;

            data.push({
              model: modelFile,
              brand: brand,
              keyword: keyword,
              ignored: ignored
            });
          });

          window.pywebview.api.saveBrands(data);
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

        ignored_files = brands.get("ignored_files", [])

        for entry in data:
            model = entry['model']
            brand = entry['brand']
            keyword = entry['keyword'].strip()
            ignored = entry['ignored']

            if ignored:
                if model not in ignored_files:
                    ignored_files.append(model)
                continue

            if brand:
                if brand == "__new__":
                    continue  # Add custom brand logic later if needed
                if brand not in brands:
                    brands[brand] = []
                if keyword and keyword not in brands[brand]:
                    brands[brand].append(keyword)

        brands['ignored_files'] = ignored_files
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
            width=900,
            height=600
        )
        webview.start(http_server=True, gui="qt", debug=True)