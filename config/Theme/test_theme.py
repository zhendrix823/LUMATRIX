# test_theme.py

from config.Theme import get_theme_styles

if __name__ == "__main__":
    theme = get_theme_styles()
    print("\n✅ Loaded theme dict:\n")
    print(theme)

    print("\n✅ Theme keys:", list(theme.keys()))
    print("✅ Button section:", theme.get("button", "MISSING!"))