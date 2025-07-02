from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import sys
import os

# ✅ Fix import path for bundled and unbundled modes
if getattr(sys, 'frozen', False):
    current_dir = sys._MEIPASS
else:
    current_dir = os.path.dirname(os.path.abspath(__file__))

sys.path.append(current_dir)

try:
    import parse_fixture
except ImportError as e:
    print("❌ Failed to import parse_fixture:", e)
    parse_fixture = None


class WebhookHandler(BaseHTTPRequestHandler):
    def _set_response(self, status_code=200):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        self._set_response()
        self.wfile.write(json.dumps({"message": "LUMATRIX Webhook is live"}).encode("utf-8"))

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        print("✅ Received request to /parse")
        print("📦 Payload:", post_data.decode("utf-8"))

        try:
            if parse_fixture:
                print("🛠️ Running parse_fixture.main()...")
                parse_fixture.main()
                response = {"status": "parsed"}
            else:
                raise RuntimeError("parse_fixture module not available.")
        except Exception as e:
            print("❌ Error during parsing:", e)
            response = {"status": "error", "message": str(e)}

        self._set_response()
        self.wfile.write(json.dumps(response).encode("utf-8"))


def run(server_class=HTTPServer, handler_class=WebhookHandler, port=53000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"✅ Webhook server listening on http://localhost:{port}")
    httpd.serve_forever()


if __name__ == '__main__':
    run()