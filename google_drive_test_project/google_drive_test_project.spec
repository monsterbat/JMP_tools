# -*- mode: python ; coding: utf-8 -*-

"""
Google Drive 測試專案 PyInstaller 配置檔案

功能：打包 Google Drive 測試專案為獨立執行檔
作者：Data Analysis Tools
"""

import os
import sys
from pathlib import Path

# 獲取當前目錄
current_dir = Path(os.getcwd())

# 分析設定
a = Analysis(
    # 主程式檔案
    [os.path.join(current_dir, 'main.py')],
    
    # 隱藏的導入模組
    pathex=[str(current_dir)],
    
    # 需要包含的模組
    binaries=[],
    
    # 需要包含的套件
    datas=[
        # 包含 README 和說明文件（可選）
        (os.path.join(current_dir, 'README.md'), '.'),
        (os.path.join(current_dir, 'USAGE_GUIDE.md'), '.'),
    ],
    
    # 隱藏的導入模組
    hiddenimports=[
        'tkinter',
        'tkinter.messagebox',
        'tkinter.filedialog',
        'gdown',
        'requests',
        'urllib3',
        'certifi',
        'charset_normalizer',
        'idna',
        'tempfile',
        'platform',
        'subprocess',
        'os',
        're',
        'sys',
    ],
    
    # 排除的模組（減少檔案大小）
    excludes=[
        'matplotlib',
        'numpy',
        'pandas',
        'scipy',
        'PIL',
        'cv2',
        'torch',
        'tensorflow',
        'jupyter',
        'IPython',
        'notebook',
        'sphinx',
        'docutils',
        'pytest',
        'unittest',
    ],
    
    # 鉤子函數
    hookspath=[],
    
    # 鉤子配置
    hooksconfig={},
    
    # 執行時鉤子
    runtime_hooks=[],
    
    # 排除的檔案
    excludes_binaries=[],
    
    # 是否包含所有檔案
    noarchive=False,
)

# 清理分析結果
pyz = PYZ(a.pure, a.zipped_data, cipher=None)

# 執行檔設定
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    
    # 執行檔名稱
    name='Google_Drive_Test',
    
    # 除錯模式
    debug=False,
    
    # 啟動模式
    bootloader_ignore_signals=False,
    
    # 是否為控制台應用程式
    console=False,  # 設為 False 隱藏控制台視窗
    
    # 是否為 Windows 服務
    disable_windowed_traceback=False,
    
    # 目標架構
    target_arch=None,
    
    # 代碼簽名標識
    codesign_identity=None,
    
    # 權利檔案
    entitlements_file=None,
    
    # 圖示檔案（可選）
    # icon=os.path.join(current_dir, 'icon.ico'),  # Windows
    # icon=os.path.join(current_dir, 'icon.icns'), # macOS
    
    # 版本資訊（可選）
    version_file=None,
)

# 應用程式設定（macOS 專用）
app = BUNDLE(
    exe,
    
    # 應用程式名稱
    name='Google Drive Test.app',
    
    # 圖示檔案（macOS）
    # icon=os.path.join(current_dir, 'icon.icns'),
    
    # 應用程式資訊
    info_plist={
        'CFBundleName': 'Google Drive Test',
        'CFBundleDisplayName': 'Google Drive Test',
        'CFBundleIdentifier': 'com.dataanalysis.google-drive-test',
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0.0',
        'NSHighResolutionCapable': True,
        'LSMinimumSystemVersion': '10.10',
        'NSRequiresAquaSystemAppearance': False,
    },
) 