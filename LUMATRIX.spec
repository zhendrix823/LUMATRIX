# LUMATRIX.spec

import os
import sys
from PyInstaller.utils.hooks import collect_submodules, collect_data_files

# ✅ Use current working directory instead of __file__
project_root = os.getcwd()
sys.path.insert(0, project_root)

hiddenimports = collect_submodules("parse_fixture")
datas = collect_data_files("parse_fixture")

a = Analysis(
    ['main.py'],
    pathex=[project_root],
    binaries=[],
    datas=[
        ('manuals/*', 'manuals'),
        ('_To_Process/*', '_To_Process'),
    ] + datas,
    hiddenimports=hiddenimports,
    hookspath=['hooks'],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
)

pyz = PYZ(
    a.pure,
    a.zipped_data,
)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='LUMATRIX',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='LUMATRIX',
)