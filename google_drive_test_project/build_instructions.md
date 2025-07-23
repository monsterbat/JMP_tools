# Google Drive 測試專案打包指南

## 🎯 打包目標

將 Google Drive 測試專案打包為獨立執行檔，無需安裝 Python 環境即可運行。

## 📋 打包前準備

### 1. 安裝 PyInstaller

```bash
python3.12 -m pip install pyinstaller
```

### 2. 確認依賴套件

```bash
python3.12 -m pip install -r requirements.txt
```

### 3. 測試程式正常運行

```bash
python3.12 main.py
```

## 🚀 打包步驟

### 方法 1：使用 spec 檔案（推薦）

```bash
# 進入專案目錄
cd google_drive_test_project

# 使用 spec 檔案打包
python3.12 -m PyInstaller google_drive_test_project.spec
```

### 方法 2：自動生成 spec 檔案

```bash
# 自動分析並生成 spec 檔案
python3.12 -m PyInstaller --onefile --windowed --name "Google_Drive_Test" main.py
```

## 📁 打包結果

打包完成後，會在 `dist/` 目錄中生成：

### macOS
- `Google Drive Test.app` - macOS 應用程式
- `Google_Drive_Test` - 可執行檔案

### Windows
- `Google_Drive_Test.exe` - Windows 執行檔

### Linux
- `Google_Drive_Test` - Linux 執行檔

## ⚙️ Spec 檔案配置說明

### 主要設定

| 設定項目 | 說明 |
|----------|------|
| `console=False` | 隱藏控制台視窗 |
| `name='Google_Drive_Test'` | 執行檔名稱 |
| `datas` | 包含的額外檔案 |
| `hiddenimports` | 隱藏的導入模組 |
| `excludes` | 排除的模組（減少檔案大小） |

### 包含的檔案
- ✅ `main.py` - 主程式
- ✅ `google_drive_utils.py` - Google Drive 工具
- ✅ `README.md` - 說明文件
- ✅ `USAGE_GUIDE.md` - 使用指南

### 排除的模組
- ❌ `matplotlib`, `numpy`, `pandas` - 大型科學計算套件
- ❌ `torch`, `tensorflow` - 機器學習套件
- ❌ `jupyter`, `IPython` - 開發工具

## 🔧 自訂配置

### 添加圖示

1. 準備圖示檔案：
   - Windows: `icon.ico`
   - macOS: `icon.icns`

2. 取消註解 spec 檔案中的圖示設定：
   ```python
   icon=os.path.join(current_dir, 'icon.icns'),  # macOS
   ```

### 修改應用程式資訊

編輯 spec 檔案中的 `info_plist` 部分：
```python
'CFBundleName': 'Google Drive Test',
'CFBundleVersion': '1.0.0',
'CFBundleIdentifier': 'com.dataanalysis.google-drive-test',
```

## 🧪 測試打包結果

### 1. 檢查檔案大小
```bash
ls -lh dist/
```

### 2. 測試執行
```bash
# macOS
open "dist/Google Drive Test.app"

# 或直接執行
./dist/Google_Drive_Test
```

### 3. 功能測試
- ✅ 啟動應用程式
- ✅ 點擊 "Fetch Data From Google Drive" 按鈕
- ✅ 輸入 Google Drive 連結
- ✅ 下載並開啟檔案

## 🛠️ 故障排除

### 常見問題

#### 1. 打包失敗
```bash
# 清理舊的打包檔案
rm -rf build/ dist/ __pycache__/

# 重新打包
python3.12 -m PyInstaller google_drive_test_project.spec
```

#### 2. 執行檔無法啟動
```bash
# 檢查依賴
python3.12 -c "import gdown, tkinter; print('OK')"

# 重新安裝套件
python3.12 -m pip install --force-reinstall gdown requests
```

#### 3. 檔案太大
- 檢查 `excludes` 清單是否包含不需要的模組
- 使用 `--onefile` 選項減少檔案數量

### 除錯模式

如果需要除錯，可以修改 spec 檔案：
```python
console=True,  # 顯示控制台視窗
debug=True,    # 啟用除錯模式
```

## 📦 分發準備

### 1. 測試在不同環境
- ✅ 乾淨的 macOS 系統
- ✅ 不同版本的 macOS
- ✅ 確認所有功能正常

### 2. 準備分發檔案
```bash
# 創建分發目錄
mkdir -p release/

# 複製執行檔
cp -r dist/ release/

# 複製說明文件
cp README.md USAGE_GUIDE.md release/

# 創建壓縮檔
cd release && zip -r Google_Drive_Test_v1.0.zip *
```

### 3. 版本管理
- 更新 `CFBundleVersion` 和 `CFBundleShortVersionString`
- 記錄變更日誌
- 標記 Git 標籤

## 🎉 完成！

打包完成後，您就有了：
- ✅ 獨立的執行檔，無需 Python 環境
- ✅ 完整的 Google Drive 功能
- ✅ 簡潔的使用者介面
- ✅ 跨平台支援

現在可以分發給其他使用者了！🚀 