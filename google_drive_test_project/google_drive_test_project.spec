# -*- mode: python ; coding: utf-8 -*-

"""
Google Drive 測試專案 PyInstaller 配置檔案

功能：打包 Google Drive 測試專案為獨立執行檔
版本：2.0 (2025-07-24)
Python：3.12+
PyInstaller：6.9+
"""

import os
import sys
from pathlib import Path

# 獲取專案根目錄
project_root = Path(os.getcwd())
print(f"專案根目錄: {project_root}")

# 確保路徑存在
main_script = project_root / 'main.py'
if not main_script.exists():
    raise FileNotFoundError(f"找不到主程式檔案: {main_script}")

# ===========================================
# PyInstaller 分析配置
# ===========================================

a = Analysis(
    # 主程式檔案
    [str(main_script)],
    
    # 搜尋路徑
    pathex=[str(project_root)],
    
    # 二進位檔案 (通常為空)
    binaries=[],
    
    # 資料檔案
    datas=[
        # 說明文件
        (str(project_root / 'README.md'), '.'),
        (str(project_root / 'USAGE_GUIDE.md'), '.'),
        (str(project_root / 'ENTERPRISE_SETUP.md'), '.'),
        # 注意：不包含 credentials.json 和 token.json (安全考量)
    ],
    
    # 隱藏導入 (確保所有依賴都被包含)
    hiddenimports=[
        # 標準庫
        'tkinter',
        'tkinter.messagebox',
        'tkinter.filedialog',
        'tkinter.ttk',
        'webbrowser',
        'tempfile',
        'platform',
        'subprocess',
        'threading',
        'json',
        'os',
        're',
        'sys',
        'pathlib',
        'urllib.parse',
        'urllib.request',
        'urllib.error',
        
        # Google Drive 相關
        'gdown',
        'requests',
        'urllib3',
        'certifi',
        'charset_normalizer',
        'idna',
        
        # Google API 相關
        'google.auth',
        'google.auth.transport',
        'google.auth.transport.requests',
        'google_auth_oauthlib',
        'google_auth_oauthlib.flow',
        'googleapiclient',
        'googleapiclient.discovery',
        'googleapiclient.errors',
        'googleapiclient.http',
        'google_auth_httplib2',
        
        # 資料處理
        'pandas',
        'openpyxl',
        'csv',
        
        # 其他可能需要的模組
        'pkg_resources',
        'packaging',
        'setuptools',
    ],
    
    # 排除的模組 (減少檔案大小)
    excludes=[
        # 大型不需要的套件
        'matplotlib',
        'numpy.testing',
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
        'test',
        'tests',
        '_pytest',
        
        # 開發工具
        'black',
        'isort',
        'flake8',
        'mypy',
        
        # 不需要的標準庫模組
        'pdb',
        'pydoc',
        'doctest',
        'profile',
        'cProfile',
        'pstats',
    ],
    
    # 鉤子函數路徑
    hookspath=[],
    
    # 鉤子配置
    hooksconfig={},
    
    # 執行時鉤子
    runtime_hooks=[],
    
    # 不打包的二進位檔案
    excludes_binaries=[],
    
    # 是否使用存檔模式
    noarchive=False,
    
    # 最佳化設定
    optimize=0,
)

# ===========================================
# PYZ 配置 (Python 字節碼存檔)
# ===========================================

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

# ===========================================
# 執行檔配置
# ===========================================

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    
    # 執行檔名稱
    name='GoogleDriveTest',
    
    # 除錯設定
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,  # 啟用 UPX 壓縮 (如果可用)
    upx_exclude=[],
    
    # 控制台設定
    console=False,  # GUI 應用程式，隱藏控制台
    disable_windowed_traceback=False,
    
    # 目標架構 (None = 自動檢測)
    target_arch=None,
    
    # 代碼簽名 (macOS/Windows)
    codesign_identity=None,
    entitlements_file=None,
    
    # 圖示檔案 (可選)
    # icon='icon.ico',     # Windows
    # icon='icon.icns',    # macOS
)

# ===========================================
# macOS 應用程式包配置
# ===========================================

if sys.platform == 'darwin':  # macOS
    app = BUNDLE(
        exe,
        
        # 應用程式名稱
        name='Google Drive Test.app',
        
        # 圖示檔案
        # icon='icon.icns',
        
        # 應用程式資訊
        info_plist={
            'CFBundleName': 'Google Drive Test',
            'CFBundleDisplayName': 'Google Drive Test',
            'CFBundleIdentifier': 'com.dataanalysis.googledrive-test',
            'CFBundleVersion': '2.0.0',
            'CFBundleShortVersionString': '2.0.0',
            'CFBundleExecutable': 'GoogleDriveTest',
            
            # macOS 特定設定
            'NSHighResolutionCapable': True,
            'LSMinimumSystemVersion': '10.15',  # macOS Catalina+
            'NSRequiresAquaSystemAppearance': False,
            'LSApplicationCategoryType': 'public.app-category.productivity',
            
            # 權限設定
            'NSNetworkUsageDescription': '需要網路存取權限來下載 Google Drive 檔案',
            'NSFileSystemUsageDescription': '需要檔案系統存取權限來儲存下載的檔案',
        },
        
        # 包含的框架 (如果需要)
        bundle_identifier='com.dataanalysis.googledrive-test',
    )

# ===========================================
# 建置資訊
# ===========================================

print("=" * 50)
print("Google Drive Test 專案建置配置")
print("=" * 50)
print(f"主程式: {main_script}")
print(f"專案目錄: {project_root}")
print(f"目標平台: {sys.platform}")
print(f"Python 版本: {sys.version}")
print("=" * 50) 