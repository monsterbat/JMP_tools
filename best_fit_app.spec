# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['app/main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('scripts/jsl/best_fit_distribution.jsl', 'scripts/jsl'),
        ('scripts/jsl/jmp_pc_report_generate_best_fit.jsl', 'scripts/jsl'),
        ('scripts/jsl/duplicate_process.jsl', 'scripts/jsl'),
        ('scripts/jsl/box_plot_tool.jsl', 'scripts/jsl'),
        ('scripts/jsl/correlation_tool.jsl', 'scripts/jsl'),
        ('scripts/jsl/jmp_pc_report_generate_normal.jsl', 'scripts/jsl'),
        ('scripts/jsl/exclude_fail.jsl', 'scripts/jsl'),
        ('scripts/jsl/explore_outliers.jsl', 'scripts/jsl'),
        ('scripts/jsl/spec_setup.jsl', 'scripts/jsl'),
        ('scripts/jsl/open_file.jsl', 'scripts/jsl'),
        ('docs/Data Analysis Tools SOP.pdf', 'docs'),
        ],
    hiddenimports=[
        'modules.core.file_operations', 
        'modules.core.jsl_parser',
        'modules.core.spec_setup',
        'modules.ui.components',
        'modules.ui.box_plot_ui',
        'modules.ui.quick_report_ui',
        'modules.utils.path_helper',
        'modules.utils.version',
        'modules.utils.ui_launcher',
        'modules.utils.constants',
        ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='DataAnalysisTools',
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
