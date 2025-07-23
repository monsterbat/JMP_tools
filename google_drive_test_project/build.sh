#!/bin/bash

# Google Drive 測試專案一鍵打包腳本

echo "=== Google Drive 測試專案打包工具 ==="
echo "🎯 目標：將專案打包為獨立執行檔"
echo ""

# 檢查 Python 3.12
if ! command -v python3.12 &> /dev/null; then
    echo "❌ Python 3.12 未找到"
    exit 1
fi
echo "✅ Python 3.12 可用"

# 檢查 PyInstaller
if ! python3.12 -c "import PyInstaller" &> /dev/null; then
    echo "⚠️  正在安裝 PyInstaller..."
    python3.12 -m pip install pyinstaller
fi
echo "✅ PyInstaller 已安裝"

# 檢查必要套件
echo "🔍 檢查必要套件..."
python3.12 -c "import gdown, tkinter" &> /dev/null
if [ $? -ne 0 ]; then
    echo "⚠️  正在安裝必要套件..."
    python3.12 -m pip install -r requirements.txt
fi
echo "✅ 必要套件已安裝"

# 清理舊的打包檔案
echo "🧹 清理舊的打包檔案..."
rm -rf build/ dist/ __pycache__/ *.spec

# 測試程式是否正常運行
echo "🧪 測試程式運行..."
if python3.12 main.py &> /dev/null & then
    sleep 2
    pkill -f "python3.12 main.py" &> /dev/null
    echo "✅ 程式測試通過"
else
    echo "❌ 程式測試失敗"
    exit 1
fi

echo ""
echo "🚀 開始打包..."
echo "📦 使用 spec 檔案進行打包..."

# 執行打包
python3.12 -m PyInstaller google_drive_test_project.spec

# 檢查打包結果
if [ -f "dist/Google_Drive_Test" ] || [ -d "dist/Google Drive Test.app" ]; then
    echo ""
    echo "✅ 打包成功！"
    echo ""
    echo "📁 打包結果："
    ls -lh dist/
    echo ""
    echo "🎉 打包完成！"
    echo ""
    echo "📋 使用說明："
    echo "• macOS: 雙擊 'Google Drive Test.app' 或執行 './dist/Google_Drive_Test'"
    echo "• Windows: 雙擊 'Google_Drive_Test.exe'"
    echo "• Linux: 執行 './dist/Google_Drive_Test'"
    echo ""
    echo "💡 提示："
    echo "• 執行檔已包含所有必要依賴，無需安裝 Python"
    echo "• 可以直接分發給其他使用者"
    echo "• 檔案位置：dist/ 目錄"
else
    echo ""
    echo "❌ 打包失敗"
    echo "請檢查錯誤訊息並重試"
    exit 1
fi 