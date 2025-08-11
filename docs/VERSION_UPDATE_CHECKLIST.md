# 版本更新檢查清單

> 此檔案用於確保版本更新時所有相關檔案都得到正確更新

## 📋 版本更新步驟

### 1. 主要版本檔案 ✅
- [ ] `modules/utils/version.py` - 更新 `APP_VERSION`、`APP_UPDATE_DATE`

### 2. 文檔檔案 ✅
- [ ] `docs/user_guide.md` - 更新版本號和日期
- [ ] `README.md` - 檢查是否有版本號需要更新

### 3. 已棄用檔案 ✅
- [ ] `modules/deprecated/ui_components.py` - 更新 `APP_VERSION`

### 4. 規格檔案 (如果存在)
- [ ] `*.spec` 檔案 - 檢查 PyInstaller 規格檔案中的版本號
- [ ] `requirements.txt` - 檢查相依套件版本

### 5. 腳本檔案 (JSL)
- [ ] `scripts/jsl/` 目錄下的 JSL 檔案 - 檢查檔案頭部註解中的版本號

## 🔍 版本號搜尋指令

使用以下指令搜尋專案中所有可能的版本號：

```bash
# 搜尋所有版本相關字串
grep -r "1\.[0-9]" . --exclude-dir=.git --exclude-dir=__pycache__

# 搜尋版本變數
grep -r "VERSION\|version" . --exclude-dir=.git --exclude-dir=__pycache__

# 搜尋特定版本號 (例如搜尋 1.2)
grep -r "1\.2" . --exclude-dir=.git --exclude-dir=__pycache__
```

## 📝 版本更新記錄

### v1.3 (2025/01/27)
- ✅ 主版本檔案更新完成
- ✅ 文檔版本號更新完成  
- ✅ 已棄用檔案版本號更新完成
- ✅ UI改進：視窗置中、滾輪功能、點擊範圍優化

### v1.2 (2025/07/09)
- 前一版本

## 🚨 注意事項

1. **集中管理**：主要版本號統一在 `modules/utils/version.py` 管理
2. **日期格式**：使用 `YYYY/MM/DD` 格式
3. **向後相容**：確保版本更新不會破壞現有功能
4. **測試**：版本更新後務必進行功能測試

## 🎯 未來改進建議

1. 考慮使用 Git tags 來管理版本發布
2. 建立自動化版本更新腳本
3. 整合 CI/CD 流程進行版本驗證
