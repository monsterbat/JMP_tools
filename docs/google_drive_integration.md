# Google Drive 檔案整合指南

## 🎯 概述

本專案已成功整合 Google Drive 檔案存取功能，您可以直接從 Google Drive 連結下載和分析檔案，無需手動下載到本地。

## 🐍 Python 解決方案

### 功能特色

✅ **自動檔案下載**: 從 Google Drive URL 自動下載檔案  
✅ **多格式支援**: 支援 Excel (.xlsx, .xls), CSV (.csv), JMP (.jmp)  
✅ **智慧檔案開啟**: 自動判斷檔案類型並用合適的應用程式開啟  
✅ **整合分析功能**: 可直接進行 Best Fit AICc 多欄位分析  
✅ **用戶友善介面**: 圖形化操作介面，無需程式設計經驗  

### 安裝需求

```bash
# 安裝新增的套件
pip install gdown requests

# 或使用專案的 requirements.txt
pip install -r requirements.txt
```

### 使用方法

#### 方法 1: 從主應用程式使用

1. 啟動主應用程式
2. 點擊 **"Google Drive"** 按鈕 (藍色按鈕)
3. 在彈出視窗中輸入 Google Drive 檔案連結
4. 選擇功能：
   - **下載並開啟檔案**: 僅下載和開啟檔案
   - **直接進行 Best Fit 分析**: 下載後立即進行統計分析

#### 方法 2: 獨立測試腳本

```bash
python test_google_drive.py
```

### 支援的連結格式

✅ `https://drive.google.com/file/d/FILE_ID/view?usp=sharing`  
✅ `https://drive.google.com/file/d/FILE_ID/view?usp=drive_link`  
✅ `https://drive.google.com/open?id=FILE_ID`  

### 檔案權限要求

⚠️ **重要**: Google Drive 檔案必須設定為 **「任何人都可以檢視」**

#### 設定方法：
1. 在 Google Drive 中右鍵點擊檔案
2. 選擇「共用」
3. 將權限改為「任何人都可以檢視」
4. 複製連結

## 📄 JSL 解決方案

### 功能特色

✅ **原生 JMP 整合**: 直接在 JMP 環境中執行  
✅ **圖形化介面**: 提供完整的對話框操作  
✅ **錯誤處理**: 完善的錯誤提示和手動下載選項  
✅ **多格式支援**: 自動判斷檔案格式並設定副檔名  

### 使用方法

#### 方法 1: 執行 JSL 腳本

1. 在 JMP 中開啟 `scripts/jsl/google_drive_connector.jsl`
2. 執行腳本
3. 在彈出對話框中輸入 Google Drive 連結
4. 點擊「下載並開啟檔案」

#### 方法 2: 直接呼叫函數

```jsl
// 開啟通用對話框
Open_Google_Drive_File();

// 處理特定檔案
Process_Specific_Google_Drive_File();
```

### JSL 版本限制

⚠️ **注意**: JSL 的 HTTP 功能可能因 JMP 版本而異

- **JMP 15+**: 完全支援 HTTP Get 功能
- **較舊版本**: 可能需要手動下載

## 🔧 故障排除

### 常見問題

#### 1. 下載失敗
- **檢查檔案權限**: 確保設定為「任何人都可以檢視」
- **檢查網路連線**: 確保可以存取 Google Drive
- **檢查連結格式**: 使用支援的連結格式

#### 2. 套件安裝問題
```bash
# 手動安裝
pip install gdown==5.2.0
pip install requests==2.32.3
```

#### 3. JMP 檔案讀取問題
- **建議轉換**: 將 JMP 檔案匯出為 Excel 或 CSV 格式
- **版本相容性**: 使用 JMP 11 或更新版本的檔案格式

### 手動下載選項

如果自動下載失敗，系統會提供手動下載說明：

1. 複製提供的直接下載連結
2. 在瀏覽器中開啟連結
3. 手動下載檔案
4. 使用「Open Data」功能開啟下載的檔案

## 📊 整合的分析功能

### Best Fit AICc 分析

Google Drive 功能完全整合了多欄位 AICc 分析：

1. **自動欄位檢測**: 識別檔案中的數值欄位
2. **多選欄位分析**: 可同時分析多個欄位
3. **分布配適**: 測試多種機率分布
4. **結果排序**: 按 AICc 值排序最佳分布
5. **JSL 生成**: 自動生成 JMP 分析腳本

### 支援的分布類型

- Normal (常態分布)
- LogNormal (對數常態分布)
- Exponential (指數分布)
- Gamma (伽瑪分布)
- Weibull (威布爾分布)
- Johnson Sb
- SHASH

## 🚀 使用範例

### 您的測試檔案

您提供的 Google Drive 連結已預設在系統中：
```
https://drive.google.com/file/d/119sslkCIIlacTa1gucenrweXI8EFJobZ/view?usp=drive_link
```

### 完整工作流程

1. **啟動應用程式**
2. **點擊 Google Drive 按鈕**
3. **貼上您的連結** (已預設)
4. **選擇「直接進行 Best Fit 分析」**
5. **選擇要分析的欄位**
6. **查看 AICc 分析結果**
7. **生成 JSL 檔案** (可選)

## 📝 技術細節

### Python 實作

- **gdown**: Google Drive 檔案下載
- **pandas**: 資料處理和分析
- **tkinter**: 圖形化使用者介面
- **正規表示式**: URL 檔案 ID 提取

### JSL 實作

- **HTTP Get**: 檔案下載功能
- **Regex**: 檔案 ID 提取
- **New Window**: 對話框建立
- **File I/O**: 檔案讀寫操作

## 🎉 總結

現在您有兩種方式來處理 Google Drive 檔案：

1. **🐍 Python 方式**: 功能完整、整合度高、適合資料分析
2. **📄 JSL 方式**: JMP 原生支援、適合 JMP 工作流程

兩種方式都支援您提供的連結格式，並且可以無縫整合到現有的分析工具中。 