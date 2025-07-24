#!/bin/bash

# ===========================================
# Google Drive Test 快速啟動腳本
# 版本：2.0 (2025-07-24)
# ===========================================

echo "🚀 Google Drive Test 快速啟動"
echo "=============================="

# 檢查 Python 3.12
if ! command -v python3.12 &> /dev/null; then
    echo "❌ Python 3.12 未安裝"
    echo "請先安裝 Python 3.12"
    exit 1
fi

# 檢查必要檔案
if [[ ! -f "main.py" ]]; then
    echo "❌ 找不到 main.py"
    echo "請確認您在正確的專案目錄中"
    exit 1
fi

# 檢查套件
echo "🔍 檢查套件..."
if ! python3.12 -c "import tkinter, gdown" &> /dev/null; then
    echo "⚠️  正在安裝必要套件..."
    python3.12 -m pip install -r requirements.txt
fi

echo "✅ 環境檢查完成"
echo "🎯 啟動程式..."
echo ""

# 啟動程式
python3.12 main.py 