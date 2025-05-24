# -*- mode: python ; coding: utf-8 -*-

import os

a = Analysis(
    ['app/main.py'],
    pathex=['modules'],
    binaries=[],
    datas=[
        ('config/best_fit_distribution.jsl', 'config'), 
        ('config/JMP_PC_report_generate_bestFit.jsl', 'config'),
        ('config/duplicate_process.jsl', 'config'),
        ('config/user_guide.md', 'config'),
        ('config/box_plot_tool.jsl', 'config'),
        ('config/correlation_tool.jsl', 'config'),
        ('temp', 'temp')  # 包含temp目錄
        ],
    hiddenimports=[
        'modules.file_operations', 
        'modules.jsl_parser', 
        'modules.ui_components',
        'modules.path_helper',
        'modules.box_plot_ui'
        ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

# 創建temp目錄（如果不存在）
os.makedirs('temp', exist_ok=True)  # 創建本地temp目錄供打包用

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
    console=False,  # 改為False來創建純GUI應用，不顯示控制台窗口
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
