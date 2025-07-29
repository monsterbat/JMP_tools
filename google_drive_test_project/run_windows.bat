@echo off
REM ===========================================
REM Google Drive Test Windows 啟動腳本
REM 版本：2.0 (2025-07-24)
REM ===========================================

echo ========================================
echo Google Drive Test Windows 啟動
echo ========================================
echo.

REM 設定編碼為 UTF-8
chcp 65001 >nul
set PYTHONIOENCODING=utf-8
set LANG=en_US.UTF-8

REM 檢查 Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python 未安裝或未加入 PATH
    echo 請先安裝 Python 並執行 install_windows.bat
    pause
    exit /b 1
)

REM 檢查主程式
if not exist "main.py" (
    echo ❌ 找不到 main.py
    echo 請確認您在正確的專案目錄中
    pause
    exit /b 1
)

REM 檢查套件
echo 🔍 檢查套件安裝...
python -c "import tkinter, gdown" >nul 2>&1
if %errorlevel% neq 0 (
    echo ⚠️  套件未安裝，正在自動安裝...
    call install_windows.bat
    if %errorlevel% neq 0 (
        echo ❌ 套件安裝失敗
        pause
        exit /b 1
    )
)

echo ✅ 環境檢查完成
echo 🚀 啟動程式...
echo.

REM 啟動程式
python main.py

echo.
echo 程式已結束
pause 