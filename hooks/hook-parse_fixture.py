from PyInstaller.utils.hooks import collect_submodules, collect_data_files

hiddenimports = collect_submodules("parse_fixture")
datas = collect_data_files("parse_fixture")