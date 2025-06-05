# Data analysis tools

---

## Project Overview (English)

### 1. ProcessCapability_BestFit
- **Purpose:** Advanced process capability analysis using the "Best Fit" method, suitable for non-normal distributions and real-world manufacturing data.
- **Features:**
  - Batch processing of multiple data files.
  - Automatic report and chart generation (including PDF/PNG outputs).
  - Modular code structure: `app/` (main program & UI), `modules/` (utility functions), `scripts/jsl/` (JSL scripts), `docs/` (documentation).
  - Supports integration with JMP JSL scripts for further automation.
  - User-friendly interface for file selection and result visualization.
  - Customizable configuration for different analysis scenarios.
  - Easy packaging and deployment (PyInstaller spec included).
- **Typical Workflow:**
  1. User selects data file(s) via the GUI.
  2. The program performs best-fit process capability analysis.
  3. Results and charts are automatically saved to the output directory.
  4. Optionally, JSL scripts can be triggered for further JMP automation.

### 2. ProcessCapability_Normal
- Standard process capability analysis for normal distributions.
- Includes JSL scripts for automated report generation in JMP.

### 3. ExcludeDuplicateData
- Data cleaning tools for removing duplicates and outliers.
- JSL scripts for batch processing of JMP data tables.
- **Features:**
  - Interactive GUI for selecting key columns (e.g., SN, Judge).
  - Automatically marks and excludes duplicate or ambiguous records based on user-defined rules.
  - Supports multi-level duplicate logic (e.g., single, double, triple occurrence handling).
  - Batch processing for large datasets.
  - Easy integration with other JMP analysis workflows.
- **Typical Use Cases:**
  - Preprocessing test data to ensure only valid, unique records are analyzed.
  - Quickly filtering out ambiguous or failed test results before statistical analysis.
- **Included Scripts:**
  - `scripts/jsl/duplicate_process.jsl`: Main script for duplicate and ambiguity exclusion.
  - `scripts/jsl/exclude_fail.jsl`: Script for excluding failed or unwanted records.
- **Workflow:**
  1. User selects a JMP data table.
  2. Selects the SN and Judge columns via the GUI.
  3. Script automatically marks duplicates and ambiguous cases.
  4. Excluded rows are removed from analysis, and a summary is displayed.

### 4. JMP_boxplot_generate.jsl
- JSL script for batch generation of boxplots from selected columns.
- Saves images automatically to the desktop.

### 5. JMP_correlation_analysis.jsl
- JSL script for interactive correlation analysis between selected X and Y columns.
- Automatically saves correlation plots to the desktop.

---

## 各資料夾與腳本功能介紹（中文）

### 1. ProcessCapability_BestFit
- **用途：** 進階製程能力分析（Best Fit），適用於非常態分布與實際製造數據。
- **功能特色：**
  - 支援多檔案批次處理。
  - 自動產生報表與圖表（PDF/PNG）。
  - 模組化架構：`app/`（主程式與介面）、`modules/`（工具模組）、`scripts/jsl/`（JSL腳本）、`docs/`（文件）。
  - 可與JMP JSL腳本整合，進行自動化分析。
  - 友善的圖形化介面，方便選檔與結果瀏覽。
  - 設定檔可自訂不同分析情境。
  - 提供PyInstaller打包規格，方便部署。
- **典型流程：**
  1. 使用者透過介面選擇資料檔案。
  2. 程式自動執行Best Fit製程能力分析。
  3. 結果與圖表自動儲存於指定資料夾。
  4. 可選擇觸發JSL腳本，進行JMP自動化。

### 2. ProcessCapability_Normal
- 標準常態分布製程能力分析。
- 內含JSL腳本，自動產生JMP報表。

### 3. ExcludeDuplicateData
- 資料去重與異常值排除工具。
- JSL腳本可批次處理JMP資料表。
- **功能特色：**
  - 互動式GUI，讓使用者選擇關鍵欄位（如SN、Judge）。
  - 依據自訂規則，自動標記並排除重複或判斷不明的資料。
  - 支援多層級重複判斷（如出現一次、兩次、三次的不同處理邏輯）。
  - 適合大量資料的批次前處理。
  - 可與其他JMP分析流程無縫整合。
- **應用場景：**
  - 測試數據前處理，確保分析時只用到唯一且有效的資料。
  - 在統計分析前，快速過濾掉不明確或失敗的測試結果。
- **內含腳本：**
  - `scripts/jsl/duplicate_process.jsl`：主腳本，負責重複與不明資料的排除。
  - `scripts/jsl/exclude_fail.jsl`：輔助腳本，用於排除失敗或不需要的資料。
- **使用流程：**
  1. 使用者選擇JMP資料表。
  2. 透過GUI選擇SN與Judge欄位。
  3. 腳本自動標記重複與不明資料。
  4. 排除的資料會自動移除，並顯示排除摘要。

### 4. JMP_boxplot_generate.jsl
- JMP用的箱型圖自動產生腳本。
- 可選擇多個欄位批次產生箱型圖，圖檔自動儲存於桌面。

### 5. JMP_correlation_analysis.jsl
- JMP用的相關性分析腳本。
- 可互動式選擇X、Y欄位產生相關性圖，自動儲存於桌面。
