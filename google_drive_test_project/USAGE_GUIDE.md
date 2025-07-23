# Google Drive 測試專案使用指南

## 🎯 專案目標

這是一個從主專案分離出來的簡化版 Google Drive 測試工具，專門用於測試和開發 Google Drive 功能。

## 📋 與主專案的差異

| 項目 | 主專案 | 測試專案 |
|------|--------|----------|
| **界面複雜度** | 多功能整合 | 單一按鈕簡化界面 |
| **功能範圍** | 完整分析工具套件 | 專注 Google Drive |
| **UI 樣式** | ~~自訂顏色~~ (用戶反映看不清楚) | **預設顏色** ✅ |
| **依賴套件** | 完整套件 | 最小化依賴 |
| **測試性** | 生產環境 | 快速測試環境 |

## 🚀 快速啟動

### 1. 進入測試專案目錄
```bash
cd google_drive_test_project
```

### 2. 檢查套件安裝
```bash
python3.12 -c "import gdown; print('✅ 套件準備就緒')"
```

### 3. 啟動應用程式
```bash
python3.12 main.py
```

## 📱 界面說明

### 主界面
```
┌─────────────────────────────────────┐
│      Google Drive File Connector    │
│                                     │
│ Click the button below to fetch     │
│    data from Google Drive          │
│                                     │
│  ┌─────────────────────────────┐   │
│  │ Fetch Data From Google Drive │   │
│  └─────────────────────────────┘   │
│                                     │
│ Ready to connect to Google Drive    │
│        Google Drive Test v1.0       │
└─────────────────────────────────────┘
```

### 對話框界面
```
┌─────────────────────────────────────────────────────┐
│               Google Drive 檔案連接器                │
│                                                     │
│ 請輸入 Google Drive 檔案連結：                        │
│                                                     │
│ 支援的連結格式：                                      │
│ • https://drive.google.com/file/d/FILE_ID/view?...  │
│ • https://drive.google.com/open?id=FILE_ID          │
│                                                     │
│ Google Drive 檔案連結:                               │
│ ┌─────────────────────────────────────────────────┐ │
│ │ [預填測試連結]                                   │ │
│ └─────────────────────────────────────────────────┘ │
│                                                     │
│ 準備就緒                                            │
│ 下載位置: /path/to/temp                             │
│                                                     │
│ [ 下載並開啟檔案 ]  [ 取消 ]                         │
└─────────────────────────────────────────────────────┘
```

## 🔧 功能測試

### 測試步驟
1. **啟動應用程式**
   - 應該看到簡潔的主界面
   - 只有一個主要按鈕：`Fetch Data From Google Drive`

2. **點擊主按鈕**
   - 彈出 Google Drive 檔案連接器對話框
   - 預填測試連結
   - 顯示下載位置路徑

3. **測試下載功能**
   - 使用預填的連結或輸入新的連結
   - 點擊「下載並開啟檔案」
   - 檔案應下載到 `temp/` 目錄並自動開啟

### 預期結果
✅ 界面簡潔，只有核心功能  
✅ 使用系統預設顏色和字體  
✅ 快速響應，無複雜依賴  
✅ 錯誤處理完善，有明確的錯誤訊息  
✅ 檔案下載到專案 `temp/` 目錄  

## 🛠️ 開發優勢

### 相比主專案的優勢
1. **快速迭代**: 無需擔心影響主專案功能
2. **依賴最小化**: 只包含 Google Drive 必要套件
3. **界面簡化**: 易於測試和驗證功能
4. **獨立性**: 可以完全獨立運行和測試

### 適用場景
- 🧪 測試新的 Google Drive API 功能
- 🔍 驗證檔案下載和處理邏輯
- 🎨 測試 UI 改進（如顏色、佈局等）
- 🚀 快速原型開發

## 📂 檔案結構詳解

```
google_drive_test_project/
├── main.py                    # 主程式入口
│   ├── create_main_window()   # 建立主視窗
│   ├── create_ui()           # 建立簡化界面
│   └── main()                # 主函數
│
├── google_drive_utils.py      # Google Drive 核心功能
│   ├── extract_google_drive_file_id()    # 提取檔案ID
│   ├── download_google_drive_file()      # 下載檔案
│   ├── open_file_with_system()          # 開啟檔案
│   └── open_google_drive_dialog()       # 對話框界面
│
├── requirements.txt           # 最小化依賴套件
├── README.md                 # 基本說明文件
├── USAGE_GUIDE.md           # 本使用指南
└── temp/                    # 自動建立的下載目錄
```

## 🔄 回到主專案

### 如何將測試成果應用到主專案

1. **功能驗證後**
   ```bash
   # 回到主專案目錄
   cd ..
   
   # 啟動主專案
   python3.12 app/main.py
   ```

2. **測試主專案的 Google Drive 功能**
   - 點擊主界面的「Google Drive」按鈕
   - 驗證功能是否正常
   - 比較與測試專案的差異

3. **反饋改進**
   - 測試專案中驗證的功能可以反饋到主專案
   - UI 改進可以同步更新
   - 錯誤修正可以一併應用

## 💡 使用建議

### 開發流程
1. 在測試專案中快速驗證新功能
2. 確認功能穩定後再整合到主專案
3. 定期同步兩個專案的 Google Drive 相關代碼

### 注意事項
- 測試專案專注於 Google Drive 功能，不包含其他分析功能
- 使用相同的 Python 3.12 環境確保一致性
- 保持測試專案的簡潔性，避免功能過度膨脹

## 📞 技術支援

如果在測試過程中遇到問題：

1. **檢查 Python 環境**: `python3.12 --version`
2. **檢查套件安裝**: `python3.12 -c "import gdown, tkinter; print('OK')"`
3. **檢查檔案權限**: 確認 Google Drive 檔案設定為公開可檢視
4. **查看錯誤日誌**: 在終端機中查看詳細錯誤訊息

成功設置後，您就可以在這個乾淨的環境中專心測試 Google Drive 功能了！ 🎉 