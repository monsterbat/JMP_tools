#!/bin/bash

# Google Drive 測試專案啟動腳本

echo "=== Google Drive 測試專案 ==="
echo "🎯 啟動簡化版 Google Drive 檔案下載工具"
echo ""

# 檢查 Python 3.12
if command -v python3.12 &> /dev/null; then
    echo "✅ Python 3.12 可用"
else
    echo "❌ Python 3.12 未找到"
    exit 1
fi

# 檢查必要套件
echo "🔍 檢查必要套件..."
python3.12 -c "import gdown, tkinter" &> /dev/null
if [ $? -eq 0 ]; then
    echo "✅ 必要套件已安裝"
else
    echo "⚠️  正在安裝必要套件..."
    python3.12 -m pip install gdown==5.2.0 requests==2.32.3
fi

# 創建 temp 目錄
mkdir -p temp
echo "📁 下載目錄: $(pwd)/temp"

echo ""
echo "🚀 啟動應用程式..."
echo "💡 點擊 'Fetch Data From Google Drive' 按鈕開始使用"
echo ""

# 啟動應用程式
python3.12 main.py 