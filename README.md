# Data Analysis Tools

A comprehensive suite of data analysis tools with integrated JMP automation capabilities, designed for manufacturing and quality control applications.

---

## Project Overview (English)

### Main Application
**Entry Point:** `python app/main.py`

The main application provides a unified interface with the following modules:

### 1. Data Process Workflow
- **Purpose:** Streamlined data preprocessing workflow with consistent file handling.
- **Features:**
  - **Open Data:** Select and open data files (JMP format supported).
  - **Exclude Duplicate:** Remove duplicate records based on configurable criteria.
  - **Setup Spec:** Configure specification limits from CSV/Excel files.
  - **Exclude Outlier:** Dynamic outlier detection and removal.
- **Workflow:**
  1. Click "Open Data" to select and open a JMP data file.
  2. Process buttons become enabled after file selection.
  3. All processing operations work on the selected data file.
  4. Results are automatically saved with timestamps.

### 2. Process Capability Reports
- **Best Fit Report:** Advanced process capability analysis using best-fit distributions.
- **Normal Report:** Standard process capability analysis for normal distributions.
- **Features:**
  - Automatic report generation with PDF/PNG outputs.
  - Batch processing capabilities.
  - Integration with JMP JSL scripts.

### 3. Analysis Tools
- **Box Plot Tool:** Interactive box plot generation with customizable parameters.
- **Correlation Tool:** Correlation analysis between selected variables.
- **Explore Outliers:** Dynamic outlier analysis with user-selectable variables.

### 4. Key JSL Scripts
- **`duplicate_process.jsl`:** Removes duplicate records, works with current data table.
- **`explore_outliers.jsl`:** Dynamic outlier detection with variable selection dialog.
- **`spec_setup.jsl`:** Template-based specification limit setup with success/failure reporting.
- **`best_fit_distribution.jsl`:** Best-fit distribution analysis.
- **`box_plot_tool.jsl`:** Box plot generation tool.
- **`correlation_tool.jsl`:** Correlation analysis tool.

### 5. Specification Setup
- **Purpose:** Set specification limits for multiple variables from external files.
- **Supported Formats:** CSV, Excel (.xlsx, .xls) - JMP files not supported.
- **Features:**
  - Template-based JSL generation.
  - Automatic success/failure counting.
  - Timestamped output files.
  - User-friendly error messages.
- **File Format:** Requires columns: Variable, LSL, USL, Target, Show Limits.

---

## 功能介紹（繁體中文）

### 主程式
**執行方式：** `python app/main.py`

主程式提供統一介面，包含以下模組：

### 1. 資料處理工作流程
- **用途：** 簡化的資料前處理工作流程，統一檔案處理方式。
- **功能特色：**
  - **開啟資料：** 選擇並開啟資料檔案（支援JMP格式）。
  - **排除重複：** 根據可設定條件移除重複記錄。
  - **設定規格：** 從CSV/Excel檔案設定規格限制。
  - **排除異常值：** 動態異常值偵測與移除。
- **工作流程：**
  1. 點選「開啟資料」選擇並開啟JMP資料檔案。
  2. 選擇檔案後，處理按鈕會啟用。
  3. 所有處理操作都作用於選定的資料檔案。
  4. 結果會自動儲存並加上時間戳記。

### 2. 製程能力報告
- **Best Fit報告：** 使用最佳配適分布的進階製程能力分析。
- **常態報告：** 標準常態分布製程能力分析。
- **功能特色：**
  - 自動產生PDF/PNG格式報告。
  - 批次處理能力。
  - 整合JMP JSL腳本。

### 3. 分析工具
- **箱型圖工具：** 互動式箱型圖產生，可自訂參數。
- **相關性工具：** 選定變數間的相關性分析。
- **探索異常值：** 動態異常值分析，可選擇變數。

### 4. 主要JSL腳本
- **`duplicate_process.jsl`：** 移除重複記錄，作用於目前資料表。
- **`explore_outliers.jsl`：** 動態異常值偵測，含變數選擇對話框。
- **`spec_setup.jsl`：** 基於範本的規格限制設定，含成功/失敗報告。
- **`best_fit_distribution.jsl`：** 最佳配適分布分析。
- **`box_plot_tool.jsl`：** 箱型圖產生工具。
- **`correlation_tool.jsl`：** 相關性分析工具。

### 5. 規格設定功能
- **用途：** 從外部檔案為多個變數設定規格限制。
- **支援格式：** CSV、Excel (.xlsx, .xls) - 不支援JMP檔案。
- **功能特色：**
  - 基於範本的JSL產生。
  - 自動成功/失敗計數。
  - 時間戳記輸出檔案。
  - 友善的錯誤訊息。
- **檔案格式：** 需要欄位：Variable、LSL、USL、Target、Show Limits。

### 6. 專案架構
- **`app/`：** 主程式與使用者介面
- **`modules/`：** 核心功能模組
  - `core/`：檔案操作、JSL解析器
  - `ui/`：使用者介面元件
  - `utils/`：工具函數與常數
- **`scripts/jsl/`：** JMP JSL腳本
- **`docs/`：** 使用者文件
- **`output/`：** 輸出檔案資料夾
- **`test_data/`：** 測試資料

### 7. 系統需求
- Python 3.7+
- 相依套件：pandas, tkinter, openpyxl
- JMP軟體（用於執行JSL腳本）
- 支援Windows、macOS、Linux
