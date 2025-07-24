# 🔧 OAuth 認證故障排除指南

## 🚨 常見錯誤解決方案

### 錯誤：「封鎖存取權」或「access_denied」

這通常是 OAuth 同意畫面設定問題。

#### 解決步驟：

### 1. 檢查 OAuth 同意畫面設定

1. 前往 [Google Cloud Console](https://console.cloud.google.com)
2. 選擇您的專案
3. 前往「API 和服務」→「OAuth 同意畫面」

#### 重要設定檢查：

| 設定項目 | 正確設定 | 說明 |
|----------|----------|------|
| **使用者類型** | 外部 | 適用於個人 Google 帳號 |
| **發布狀態** | 測試中 | 允許測試使用者使用 |
| **測試使用者** | 已添加您的 email | 必須包含您的 Google 帳號 |

### 2. 添加測試使用者

1. 在 OAuth 同意畫面頁面
2. 滾動到「測試使用者」區域
3. 點擊「+ 新增使用者」
4. 輸入您的 Google 帳號 email
5. 點擊「儲存」

### 3. 檢查 OAuth 權限範圍

確認您的應用程式請求的權限範圍：

```
https://www.googleapis.com/auth/drive.readonly
https://www.googleapis.com/auth/drive.file  
https://www.googleapis.com/auth/drive
```

### 4. 檢查憑證設定

1. 前往「API 和服務」→「憑證」
2. 確認 OAuth 2.0 用戶端 ID 存在
3. 檢查「授權的重新導向 URI」包含：
   - `http://localhost`
   - `http://localhost:8080`

## 🔄 重新認證流程

### 步驟 1: 重置認證

```bash
python3.12 reset_auth.py
```

### 步驟 2: 重新測試

```bash
python3.12 main.py
```

### 步驟 3: 認證注意事項

當瀏覽器開啟時：

1. **選擇正確的帳號**：使用擁有檔案的 Google 帳號
2. **確認應用程式**：看到「test_program」或您的專案名稱
3. **授權所有權限**：點擊「允許」所有請求的權限
4. **完成認證**：看到「認證流程已完成」訊息

## 🛠️ 進階故障排除

### 檢查檔案權限

您的檔案連結：
```
https://drive.google.com/file/d/1Zfb7haZ5uDoYCkxyxcGXJ2UCiNtbbhmK/view?usp=drive_link
```

檔案 ID：`1Zfb7haZ5uDoYCkxyxcGXJ2UCiNtbbhmK`

#### 權限檢查方法：

1. **直接存取**：在瀏覽器中開啟檔案連結
2. **檢查擁有者**：確認您是檔案擁有者
3. **檢查分享設定**：右鍵 → 共用 → 檢查權限

### 常見問題與解決方案

#### Q1: 仍然出現「存取被拒絕」
**解決方案**：
1. 確認使用正確的 Google 帳號登入
2. 檢查檔案是否仍然存在
3. 嘗試用不同的檔案測試

#### Q2: OAuth 流程沒有開啟瀏覽器
**解決方案**：
1. 檢查防火牆設定
2. 確認 `localhost` 連接正常
3. 手動複製 URL 到瀏覽器

#### Q3: 「應用程式未經驗證」警告
**解決方案**：
1. 點擊「進階」
2. 點擊「前往 [您的專案名稱] (不安全)」
3. 這是正常的，因為應用程式在測試階段

## 📋 完整檢查清單

在重新測試前，請確認：

- [ ] OAuth 同意畫面設定為「外部」
- [ ] 您的 email 已添加為測試使用者
- [ ] Google Drive API 已啟用
- [ ] OAuth 2.0 憑證已建立
- [ ] credentials.json 檔案在正確位置
- [ ] token.json 已刪除（重新認證）
- [ ] 使用正確的 Google 帳號測試

## 🆘 仍然無法解決？

### 除錯資訊收集

執行除錯測試：
```bash
python3.12 test_enterprise.py
```

提供以下資訊：
1. 完整錯誤訊息
2. Google Cloud Console 專案設定截圖
3. OAuth 同意畫面設定截圖
4. 使用的 Google 帳號類型（個人/企業）

### 替代解決方案

如果 OAuth 持續有問題，可以：

1. **使用公開存取模式**：
   - 將檔案設定為「任何人都可以檢視」
   - 使用公開存取按鈕

2. **重新建立專案**：
   - 在 Google Cloud Console 建立新專案
   - 重新設定 OAuth 同意畫面
   - 下載新的 credentials.json

3. **聯絡技術支援**：
   - 提供詳細的錯誤日誌
   - 包含 Google Cloud Console 設定資訊 