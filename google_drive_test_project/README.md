# Google Drive 測試專案

這是一個簡化版的 Google Drive 檔案下載工具，專門用於測試 Google Drive 功能。

## 🎯 功能特色

✅ **簡單界面**: 只有一個主要按鈕  
✅ **Google Drive 整合**: 支援 Google Drive 檔案直接下載  
✅ **多格式支援**: Excel, CSV, JMP 等格式  
✅ **自動開啟**: 下載後自動用系統預設程式開啟  
✅ **本地下載**: 檔案保存在專案的 `temp/` 目錄  

## 🚀 快速開始

### 1. 安裝依賴套件

```bash
pip install -r requirements.txt
```

### 2. 啟動應用程式

```bash
python3.12 main.py
```

### 3. 使用步驟

1. 點擊 **"Fetch Data From Google Drive"** 按鈕
2. 在彈出的對話框中輸入 Google Drive 檔案連結
3. 點擊 **"下載並開啟檔案"**
4. 等待下載完成，檔案會自動開啟

## 📋 支援的連結格式

✅ `https://drive.google.com/file/d/FILE_ID/view?usp=sharing`  
✅ `https://drive.google.com/file/d/FILE_ID/view?usp=drive_link`  
✅ `https://drive.google.com/open?id=FILE_ID`  

## ⚠️ 重要事項

1. **檔案權限**: Google Drive 檔案必須設定為「任何人都可以檢視」
2. **網路連線**: 需要穩定的網路連線
3. **檔案格式**: 支援 Excel (.xlsx, .xls), CSV (.csv), JMP (.jmp)
4. **下載位置**: 檔案會下載到專案的 `temp/` 目錄

## 🔧 故障排除

### 錯誤：請先安裝 gdown 套件

```bash
pip install gdown==5.2.0
```

### 檔案權限問題

1. 在 Google Drive 中右鍵點擊檔案
2. 選擇「共用」→「變更」
3. 設定為「任何人都可以檢視」
4. 複製連結

### 檔案開啟問題

如果檔案下載成功但開啟失敗：
1. 檢查 `temp/` 目錄中的檔案
2. 手動開啟該檔案
3. 確認系統有相應的應用程式可以開啟該格式

## 📁 專案結構

```
google_drive_test_project/
├── main.py                 # 主程式 (GUI界面)
├── google_drive_utils.py   # Google Drive 工具模組
├── requirements.txt        # 依賴套件
├── README.md              # 使用說明
└── temp/                  # 下載檔案目錄 (自動創建)
```

## 🛠️ 開發說明

這個專案是從主專案中分離出來的簡化版本，專門用於測試 Google Drive 功能。

### 主要模組

- `main.py`: 提供簡單的 GUI 界面
- `google_drive_utils.py`: 包含所有 Google Drive 相關功能

### 與主專案的差異

- 移除了複雜的分析功能
- 簡化了 UI 設計
- 專注於 Google Drive 下載功能
- 使用預設的 UI 顏色和樣式

## 📧 技術支援

如果遇到問題，請檢查：
1. Python 版本 (建議 3.8+)
2. 依賴套件安裝
3. 網路連線狀況
4. Google Drive 檔案權限設定 