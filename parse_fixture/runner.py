import os
import shutil
import sys

def main():
    print("✅ parse_fixture.main() was called")

    # Detect runtime path (inside PyInstaller vs normal)
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS  # PyInstaller temp path
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))

    source_dir = os.path.join(base_path, "_To_Process")
    dest_dir = os.path.join(base_path, "manuals")

    # Ensure destination folder exists
    os.makedirs(dest_dir, exist_ok=True)

    moved_files = []

    # If the _To_Process folder is missing, stop gracefully
    if not os.path.exists(source_dir):
        print("⚠️ '_To_Process' folder not found at runtime:", source_dir)
        return

    # Move PDFs
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)

        if not os.path.isfile(file_path):
            continue

        if filename.lower().endswith(".pdf"):
            dest_path = os.path.join(dest_dir, filename)
            shutil.move(file_path, dest_path)
            moved_files.append(filename)

    print(f"📁 Moved {len(moved_files)} PDFs: {moved_files}")