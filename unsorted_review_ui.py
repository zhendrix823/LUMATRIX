# ✅ Full unsorted_review_ui.py for LUMATRIX v0.3.5 — supports after_review callback

import webview

def run(pdf_files, after_review):
    rows = ""

    if pdf_files:
        for file in pdf_files:
            rows += f"<li>{file}</li>"
    else:
        rows = "<li>No unsorted PDFs found.</li>"

    html = f"""
    <html>
    <head>
    <title>Unsorted PDFs</title>
    <style>
        body {{
            background-color: #1e1e1e;
            color: #dcdcdc;
            font-family: monospace;
            padding: 20px;
        }}
        h1 {{
            font-size: 20px;
            color: #80ff80;
        }}
        ul {{
            list-style-type: disc;
        }}
    </style>
    </head>
    <body>
        <h1>Review _Unsorted PDFs</h1>
        <ul>{rows}</ul>
    </body>
    </html>
    """

    window = webview.create_window("Review _Unsorted PDFs", html=html)

    def on_closed():
        print("✅ Review window closed.")
        after_review()

    window.events.closed += on_closed

    webview.start()