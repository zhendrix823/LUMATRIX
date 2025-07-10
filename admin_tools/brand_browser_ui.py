#!/usr/bin/env python3

"""
brand_browser_ui.py

🗂️ Simple Browser UI to view your current brands.json.
Run:  python3 admin_tools/brand_browser_ui.py
"""

import os
import json
import webview

# === CONFIG ===
PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BRANDS_FILE = os.path.join(PROJECT_PATH, "brands.json")

def load_brands():
    if not os.path.exists(BRANDS_FILE):
        return {}
    with open(BRANDS_FILE, "r") as f:
        return json.load(f)

def build_html(data):
    html = """
    <html>
    <head>
        <title>Brand Map Viewer</title>
        <style>
            body { background: #111; color: #0f0; font-family: monospace; padding: 20px; }
            h1 { color: #0f0; }
            pre { background: #000; padding: 10px; border: 1px solid #0f0; overflow-x: auto; }
        </style>
    </head>
    <body>
        <h1>✅ Current Brand Map</h1>
        <pre>{}</pre>
    </body>
    </html>
    """.format(json.dumps(data, indent=2))
    return html

if __name__ == "__main__":
    brands = load_brands()
    html = build_html(brands)
    webview.create_window("Brand Browser UI", html=html, width=800, height=600)
    webview.start(http_server=True, gui="qt", debug=True)