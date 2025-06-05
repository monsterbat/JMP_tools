# -*- mode: python ; coding: utf-8 -*-

import os

a = Analysis(
    ['app/main.py'],
    pathex=['modules'],
    binaries=[],
    datas=[
        ('scripts/jsl/best_fit_distribution.jsl', 'scripts/jsl'), 
        ('scripts/jsl/jmp_pc_report_generate_best_fit.jsl', 'scripts/jsl'),
        ('scripts/jsl/duplicate_process.jsl', 'scripts/jsl'),
        ('scripts/jsl/box_plot_tool.jsl', 'scripts/jsl'),
        ('scripts/jsl/correlation_tool.jsl', 'scripts/jsl'),
        ('scripts/jsl/jmp_pc_report_generate_normal.jsl', 'scripts/jsl'),
        ('scripts/jsl/exclude_fail.jsl', 'scripts/jsl'),
        ('docs/user_guide.md', 'docs'),
        ('temp', 'temp')  # 包含temp目錄
        ],
    hiddenimports=[
        'modules.core.file_operations', 
        'modules.core.jsl_parser', 
        'modules.ui.components',
        'modules.ui.box_plot_ui',
        'modules.utils.path_helper',
        'modules.utils.version'
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
