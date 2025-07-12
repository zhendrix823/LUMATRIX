import json
import os
import tkinter as tk
from tkinter import messagebox, ttk
import webview

from config.Theme import get_theme_styles  # ✅ Correct absolute import


# Load theme styles
THEME = get_theme_styles()


# === Brand Admin Window ===
def save_brand():
    name = entry_name.get()
    website = entry_website.get()
    notes = text_notes.get("1.0", tk.END)

    if not name.strip():
        messagebox.showwarning("Missing Info", "Brand name is required.")
        return

    brand_data = {
        "name": name.strip(),
        "website": website.strip(),
        "notes": notes.strip()
    }

    brands = []
    if os.path.exists("brands.json"):
        with open("brands.json", "r") as f:
            try:
                brands = json.load(f)
            except json.JSONDecodeError:
                brands = []

    brands.append(brand_data)

    with open("brands.json", "w") as f:
        json.dump(brands, f, indent=2)

    messagebox.showinfo("Success", f"Brand '{name}' saved!")
    entry_name.delete(0, tk.END)
    entry_website.delete(0, tk.END)
    text_notes.delete("1.0", tk.END)


def launch_gui():
    global entry_name, entry_website, text_notes

    root = tk.Tk()
    root.title("Brand Admin")
    root.configure(bg=THEME['background'])

    # === Styles ===
    style = ttk.Style()
    style.theme_use('clam')

    style.configure('TLabel', background=THEME['background'], foreground=THEME['text'], font=(THEME['font_family'], 12))
    style.configure('TButton',
                    background=THEME['button']['inactive_bg'],
                    foreground=THEME['button']['inactive_text'],
                    font=(THEME['font_family'], 12))
    style.map('TButton',
              background=[('active', THEME['button']['active_bg'])],
              foreground=[('active', THEME['button']['active_text'])])

    # === Widgets ===
    label_name = ttk.Label(root, text="Brand Name:")
    label_name.pack(pady=(10, 0))
    entry_name = ttk.Entry(root, width=40)
    entry_name.pack(pady=(0, 10))

    label_website = ttk.Label(root, text="Website:")
    label_website.pack()
    entry_website = ttk.Entry(root, width=40)
    entry_website.pack(pady=(0, 10))

    label_notes = ttk.Label(root, text="Notes:")
    label_notes.pack()
    text_notes = tk.Text(root, height=5, width=40, bg=THEME['input_bg'], fg=THEME['input_text'])
    text_notes.pack(pady=(0, 10))

    button_save = ttk.Button(root, text="Save Brand", command=save_brand)
    button_save.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    launch_gui()