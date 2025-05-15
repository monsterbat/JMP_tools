# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['app/main.py'],
    pathex=['modules'],
    binaries=[],
    datas=[
        ('config/best_fit_distribution.jsl', 'config'), 
        ('config/JMP_PC_report_generate_bestFit.jsl', 'config'),
        ('config/duplicate_process.jsl', 'config'),
        ('config/user_guide.md', 'config')
        ],
    hiddenimports=[
        'modules.file_operations', 
        'modules.jsl_parser', 
        'modules.ui_components',
        'modules.path_helper'
        ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='best_fit_app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
