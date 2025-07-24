# 🏢 企業版 Google Drive API 設定指南

## 📋 概述

本指南說明如何設定企業版 Google Drive API 存取權限，以便存取公司內部共享檔案、私人檔案，以及其他受限制的 Google Drive 檔案。

## 🎯 支援的檔案類型

企業版 API 可以存取：

✅ **公司內部共享檔案** - 僅限公司成員檢視的檔案  
✅ **私人檔案** - 您擁有的私人檔案  
✅ **特定權限檔案** - 明確分享給您的檔案  
✅ **受限制檔案** - 需要特殊權限的檔案  

## 🚀 設定步驟

### 步驟 1: 建立 Google Cloud 專案

1. 前往 [Google Cloud Console](https://console.cloud.google.com)
2. 點擊專案選擇器，然後點擊「新增專案」
3. 輸入專案名稱（例如：`Company-GoogleDrive-Access`）
4. 選擇您的組織（如果有）
5. 點擊「建立」

### 步驟 2: 啟用 Google Drive API

1. 在左側選單中，前往「API 和服務」→「程式庫」
2. 搜尋「Google Drive API」
3. 點擊「Google Drive API」
4. 點擊「啟用」

### 步驟 3: 建立 OAuth 2.0 憑證

1. 前往「API 和服務」→「憑證」
2. 點擊「+ 建立憑證」→「OAuth 用戶端 ID」
3. 如果是第一次，需要設定「OAuth 同意畫面」：
   - 選擇「內部」（適用於 G Suite/Workspace 組織）
   - 填寫應用程式名稱：`Google Drive File Connector`
   - 填寫使用者支援電子郵件
   - 點擊「儲存並繼續」
4. 返回憑證頁面，再次點擊「+ 建立憑證」→「OAuth 用戶端 ID」
5. 選擇應用程式類型：「桌面應用程式」
6. 輸入名稱：`GoogleDrive-Desktop-Client`
7. 點擊「建立」

### 步驟 4: 下載憑證檔案

1. 在憑證清單中找到您剛建立的 OAuth 2.0 用戶端 ID
2. 點擊下載圖示（⬇️）
3. 將下載的 JSON 檔案重新命名為 `credentials.json`
4. 將檔案放置在程式目錄中：
   ```
   google_drive_test_project/
   ├── credentials.json  ← 放在這裡
   ├── main.py
   ├── google_drive_utils.py
   └── ...
   ```

## 🔧 安裝必要套件

執行以下命令安裝 Google Drive API 套件：

```bash
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

或者使用我們提供的 requirements.txt：

```bash
pip install -r requirements.txt
```

## 🎮 使用方法

### 首次使用

1. 啟動程式：`python main.py`
2. 點擊「🔐 Fetch Enterprise Data (OAuth)」按鈕
3. 輸入 Google Drive 檔案連結
4. 點擊「🔐 透過 API 下載檔案」
5. **首次使用會自動開啟瀏覽器進行授權**：
   - 選擇您的企業帳號
   - 點擊「允許」授權存取
   - 瀏覽器會顯示「認證流程已完成」
6. 返回程式，檔案會自動開始下載

### 後續使用

認證完成後，系統會自動儲存 `token.json` 檔案。之後使用時：

1. 不需要重新授權
2. Token 會自動更新
3. 可以直接存取企業檔案

## 📁 檔案結構

設定完成後，目錄結構應該如下：

```
google_drive_test_project/
├── credentials.json     ← Google Cloud 憑證
├── token.json          ← 自動生成的授權 Token
├── main.py
├── google_drive_utils.py
├── temp/               ← 下載檔案儲存位置
└── ...
```

## ⚠️  安全注意事項

### 🔒 憑證檔案安全

- **credentials.json** 包含敏感資訊，不要分享給他人
- **token.json** 包含您的授權資訊，同樣需要保密
- 建議將這些檔案加入 `.gitignore`

### 🏢 企業政策

- 確保您的操作符合公司的 IT 安全政策
- 如有疑問，請聯絡您的 IT 部門
- 某些企業可能限制第三方應用程式存取

## 🔧 故障排除

### 常見問題

#### 1. 找不到 credentials.json

**錯誤訊息**：`❌ 找不到 credentials.json 檔案！`

**解決方案**：
- 確認已從 Google Cloud Console 下載憑證檔案
- 確認檔案名稱為 `credentials.json`
- 確認檔案位於程式目錄中

#### 2. 授權失敗

**錯誤訊息**：`存取被拒絕` 或授權頁面錯誤

**解決方案**：
- 確認使用正確的企業帳號登入
- 檢查 OAuth 同意畫面設定
- 確認 Google Drive API 已啟用

#### 3. 缺少套件

**錯誤訊息**：`❌ 缺少必要套件！`

**解決方案**：
```bash
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

#### 4. Token 過期

**情況**：之前可以使用，現在無法存取

**解決方案**：
- 刪除 `token.json` 檔案
- 重新執行程式進行授權

## 📊 功能比較

| 功能 | 公開存取 | 企業版存取 |
|------|----------|------------|
| 設定複雜度 | ⭐ 簡單 | ⭐⭐⭐ 需要設定 |
| 存取範圍 | 僅公開檔案 | 所有有權限的檔案 |
| 安全性 | 基礎 | 🔐 OAuth 2.0 |
| 企業檔案 | ❌ 無法存取 | ✅ 完全支援 |
| 私人檔案 | ❌ 無法存取 | ✅ 完全支援 |

## 📞 技術支援

如果遇到問題：

1. 檢查本指南的故障排除章節
2. 確認所有設定步驟都已完成
3. 檢查 Google Cloud Console 中的 API 配額和使用情況
4. 聯絡您的 IT 部門了解企業政策

## 🎉 設定完成

設定完成後，您就可以：

✅ 存取公司內部共享的 Google Drive 檔案  
✅ 下載和分析企業資料  
✅ 整合到您的工作流程中  
✅ 享受安全的 OAuth 2.0 認證保護  

祝您使用愉快！🚀 