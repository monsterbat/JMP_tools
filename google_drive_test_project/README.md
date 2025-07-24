# Google Drive Test 專案

> **簡化版 Google Drive 檔案下載和開啟工具**  
> 版本：2.0 | 更新日期：2025-07-24 | Python 3.12+

## 📋 **專案概述**

這是一個輕量級的 Google Drive 檔案存取工具，支援兩種存取模式：

- **🌐 公開檔案下載**：無需認證，直接下載公開分享的檔案
- **🔐 企業版存取**：透過 OAuth 2.0 認證，存取有權限的私人檔案

## ✨ **主要功能**

### 🎯 **核心功能**
- 支援 Google Drive 公開和私人檔案存取
- 自動檔案格式識別（CSV, Excel, JMP）
- 一鍵下載並開啟檔案
- 現代化 GUI 介面

### 🔒 **企業級安全**
- OAuth 2.0 認證流程
- 安全的憑證管理
- 自動 token 刷新
- 權限範圍控制

### 📦 **部署選項**
- 直接執行 Python 腳本
- 打包為獨立執行檔
- 跨平台支援（macOS, Windows, Linux）

## 🚀 **快速開始**

### **方法 1：直接執行**
```bash
# 快速啟動（推薦）
./run.sh

# 或手動執行
python3.12 main.py
```

### **方法 2：打包執行檔**
```bash
# 一鍵打包
./build.sh

# 執行打包後的程式
# macOS: 雙擊 'dist/Google Drive Test.app'
# 其他: ./dist/GoogleDriveTest
```

## 📁 **專案結構**

```
google_drive_test_project/
├── 📄 main.py                     # 主程式入口
├── 📄 google_drive_utils.py       # 核心功能模組
├── 📄 requirements.txt            # 套件依賴
├── 📄 google_drive_test_project.spec # PyInstaller 配置
├── 🔧 run.sh                      # 快速啟動腳本
├── 🔧 build.sh                    # 打包建置腳本
├── 📚 README.md                   # 專案說明（本檔案）
├── 📚 USAGE_GUIDE.md             # 詳細使用指南
├── 📚 ENTERPRISE_SETUP.md        # 企業版設定說明
├── 📚 OAUTH_TROUBLESHOOTING.md   # OAuth 疑難排解
├── 📚 PRACTICAL_SOLUTIONS.md     # 實用解決方案
├── 🧪 test_enterprise.py         # 企業版測試腳本
├── 🧪 test_shared_access.py      # 共享存取測試
├── 🧪 quick_verify.py            # 快速驗證腳本
├── 🔧 reset_auth.py              # 認證重置工具
├── 📁 temp/                      # 下載檔案暫存目錄
├── 🔒 credentials.json           # Google API 憑證（需自行準備）
└── 🔒 token.json                 # OAuth token（自動生成）
```

## 🎯 **使用方式**

### **公開檔案下載**
1. 啟動程式
2. 點擊「📁 Fetch Public Data From Google Drive」
3. 輸入 Google Drive 公開分享連結
4. 點擊下載

### **企業版存取**
1. **首次設定**：
   - 參考 `ENTERPRISE_SETUP.md` 設定 Google Cloud Console
   - 下載 `credentials.json` 到專案目錄
   
2. **使用步驟**：
   - 點擊「🔐 Fetch Enterprise Data (OAuth)」
   - 輸入檔案連結
   - 完成瀏覽器認證
   - 自動下載檔案

## 📋 **系統需求**

### **基本需求**
- **Python**：3.12 或更高版本
- **作業系統**：macOS 10.15+, Windows 10+, Linux (Ubuntu 18.04+)
- **網路**：需要網際網路連線

### **套件依賴**
```txt
# 核心功能套件
gdown==5.2.0
requests==2.32.3
google-api-python-client==2.144.0
google-auth-httplib2==0.2.0
google-auth-oauthlib==1.2.1

# 資料處理套件
pandas==2.2.3
openpyxl==3.1.5

# 打包工具
pyinstaller==6.9.0
```

## 🔧 **安裝說明**

### **1. 克隆專案**
```bash
git clone <repository-url>
cd google_drive_test_project
```

### **2. 安裝依賴**
```bash
# 自動安裝（推薦）
./run.sh

# 手動安裝
python3.12 -m pip install -r requirements.txt
```

### **3. 企業版設定（可選）**
如需使用企業版功能，請參考 `ENTERPRISE_SETUP.md` 進行 Google Cloud Console 設定。

## 📖 **詳細文件**

| 文件 | 說明 |
|------|------|
| `USAGE_GUIDE.md` | 詳細使用指南和功能說明 |
| `ENTERPRISE_SETUP.md` | Google Cloud Console 設定步驟 |
| `OAUTH_TROUBLESHOOTING.md` | OAuth 認證問題排解 |
| `PRACTICAL_SOLUTIONS.md` | 實用的檔案分享解決方案 |

## 🧪 **測試工具**

| 腳本 | 功能 |
|------|------|
| `test_enterprise.py` | 測試企業版下載功能 |
| `test_shared_access.py` | 測試共享檔案存取 |
| `quick_verify.py` | 快速驗證分享邏輯 |
| `reset_auth.py` | 重置 OAuth 認證 |

## 🚀 **打包部署**

### **建置獨立執行檔**
```bash
# 一鍵建置
./build.sh

# 手動建置
python3.12 -m PyInstaller google_drive_test_project.spec --clean --noconfirm
```

### **分發說明**
- **執行檔位置**：`dist/` 目錄
- **依賴檔案**：需要將 `credentials.json` 複製到執行檔同一目錄
- **首次執行**：會自動開啟瀏覽器進行 OAuth 認證

## 🔒 **安全注意事項**

### **敏感檔案**
- `credentials.json`：Google API 憑證，**絕對不能公開**
- `token.json`：OAuth 存取權杖，包含敏感資訊
- 這些檔案已加入 `.gitignore`，不會被版本控制

### **權限管理**
- 企業版功能需要適當的 Google Drive API 權限
- 建議定期檢查和更新 OAuth 權限範圍
- 如有安全疑慮，可使用 `reset_auth.py` 重置認證

## 🤝 **企業級共享模式**

本專案支援企業級的檔案共享模式：

1. **A 人員**上傳檔案到自己的 Google Drive
2. **A 人員**分享檔案權限給 **B 人員**
3. **B 人員**使用自己的帳號登入並存取檔案

這種模式等效於企業版 Google Workspace 的運作邏輯，確保檔案安全性和存取控制。

## 📞 **技術支援**

如遇到問題，請按以下順序排查：

1. 查看相關文件（`TROUBLESHOOTING.md` 等）
2. 檢查系統需求和依賴套件
3. 使用測試腳本驗證功能
4. 聯繫開發團隊

## 📄 **授權資訊**

本專案為內部工具，版權歸 Data Analysis Tools 團隊所有。

---

**🎉 享受使用 Google Drive Test 專案！** 