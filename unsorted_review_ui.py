# ✅ Full unsorted_review_ui.py for LUMATRIX v0.3.5

import webview
import parse_fixture.parse_engine as parse_engine

def run(pdf_files):
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

    # Create the window
    window = webview.create_window("Review _Unsorted PDFs", html=html)

    # Register a callback to run the parser when the window closes
    def on_closed():
        print("✅ Reviewer closed — running parse_engine.main()...")
        parse_engine.main()

    window.events.closed += on_closed

    webview.start()