@echo off
REM ===========================================
REM Google Drive Test 專案 Windows 安裝腳本
REM 版本：2.0 (2025-07-24)
REM ===========================================

echo ========================================
echo Google Drive Test Windows 安裝工具
echo ========================================
echo.

REM 設定編碼為 UTF-8
chcp 65001 >nul
set PYTHONIOENCODING=utf-8
set LANG=en_US.UTF-8

REM 檢查 Python 版本
echo [1/4] 檢查 Python 環境...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python 未安裝或未加入 PATH
    echo 請先安裝 Python 3.8+ 並加入系統 PATH
    pause
    exit /b 1
)

for /f "tokens=2" %%i in ('python --version') do set PYTHON_VERSION=%%i
echo ✅ Python 版本: %PYTHON_VERSION%

REM 升級 pip
echo.
echo [2/4] 升級 pip...
python -m pip install --upgrade pip --no-warn-script-location
if %errorlevel% neq 0 (
    echo ⚠️  pip 升級失敗，繼續安裝...
)

REM 安裝套件
echo.
echo [3/4] 安裝必要套件...
echo 正在安裝核心套件...

REM 分別安裝每個套件，避免編碼問題
python -m pip install gdown==5.2.0 --no-warn-script-location
python -m pip install requests==2.32.3 --no-warn-script-location
python -m pip install urllib3==2.2.2 --no-warn-script-location
python -m pip install certifi==2024.7.4 --no-warn-script-location

echo 正在安裝 Google API 套件...
python -m pip install google-api-python-client==2.144.0 --no-warn-script-location
python -m pip install google-auth-httplib2==0.2.0 --no-warn-script-location
python -m pip install google-auth-oauthlib==1.2.1 --no-warn-script-location
python -m pip install google-auth==2.32.0 --no-warn-script-location

echo 正在安裝資料處理套件...
python -m pip install pandas==2.2.3 --no-warn-script-location
python -m pip install openpyxl==3.1.5 --no-warn-script-location

REM 測試導入
echo.
echo [4/4] 測試套件安裝...
python -c "import tkinter; import gdown; import google.auth; print('✅ 所有套件安裝成功！')" 2>nul
if %errorlevel% neq 0 (
    echo ❌ 套件測試失敗
    echo 請檢查錯誤訊息並重新執行
    pause
    exit /b 1
)

echo.
echo ========================================
echo ✅ 安裝完成！
echo ========================================
echo.
echo 🚀 現在可以執行程式：
echo    python main.py
echo.
echo 💡 提示：
echo    • 如需企業版功能，請準備 credentials.json
echo    • 下載的檔案會保存在 temp\ 目錄
echo.
pause 