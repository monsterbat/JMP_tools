# Data Analysis Tools User Guide

## Introduction
Data Analysis Tools is a comprehensive data analysis application that provides process capability analysis, data preprocessing, and automated report generation. It integrates with JMP software for advanced statistical analysis and report generation.

## Main Features
The software is organized into four main sections:

### 1. Data Process
**Unified Workflow:**
- **Open Data**: Select and load your data file (CSV, Excel formats supported)
- **Exclude Duplicate**: Remove duplicate data items with interactive GUI
- **Setup Spec**: Configure specification limits for process variables
- **Exclude Outlier**: Remove abnormal values using statistical methods

**Workflow Process:**
1. Click "Open Data" to select your data file
2. The file name will be displayed in the status area
3. All processing buttons become enabled after file selection
4. Each function operates on the same selected file for consistency

### 2. Process Capability Report
- **Best Fit Analysis**: Advanced process capability analysis for non-normal distributions
- **Normal Distribution Analysis**: Standard normal distribution process capability analysis
- **Automated Report Generation**: Generate PDF/PNG reports automatically
- **JMP Integration**: Seamless integration with JMP JSL scripts

### 3. Analysis Tools
- **Box Plot Tool**: Generate box plots for data visualization
- **Correlation Analysis**: Analyze correlations between variables
- **Quick Report**: Generate summary reports

### 4. Application Information
- Version information and system status
- Help and documentation links

## Usage Instructions

### Data Processing Workflow
1. **Open Data File**
   - Click "Open Data" button
   - Select CSV or Excel file
   - File name will be displayed in status area

2. **Exclude Duplicate Data**
   - Click "Exclude Duplicate" button
   - Interactive GUI will open in JMP
   - Select SN and Judge columns
   - Click "Excluded!" to process duplicate data

3. **Setup Specifications**
   - Click "Setup Spec" button
   - Select limits file (CSV or Excel format)
   - Program will generate JSL script with specifications
   - Script will be saved with timestamp

4. **Exclude Outliers**
   - Click "Exclude Outlier" button
   - Select variables for outlier analysis
   - Program will generate JSL script for outlier detection

### Process Capability Analysis
1. **Best Fit Analysis**
   - Click "Best Fit Distribution" button
   - Select data file for analysis
   - Program will generate comprehensive report

2. **Normal Distribution Analysis**
   - Click "Normal Distribution" button
   - Select data file for analysis
   - Standard normal distribution analysis

### JMP Integration
- All generated JSL scripts use "Current Data Table()" logic
- Scripts include error checking and file information display
- Scripts are saved with timestamps for version control

## File Format Support
- **Input Files**: CSV, Excel (.xlsx, .xls)
- **Output Files**: PDF, PNG, JSL scripts
- **Note**: JMP files (.jmp) are not supported for direct reading

## Common Issues
- Ensure your data files are in supported formats (CSV, Excel)
- For large datasets, processing may take longer
- Make sure JMP software is properly installed for JSL script execution
- Check that all required columns are present in your data files

## System Requirements
- Python 3.10 or higher
- JMP software (for JSL script execution)
- Required Python packages: pandas, openpyxl, tkinter

## Contact Information
For any questions, please contact SC Hsiao

Version: V1.3  
Last Updated: 2025/07/05

---

# 數據分析工具 使用指南

## 軟件介紹
數據分析工具是一個綜合性的數據分析應用程式，提供製程能力分析、數據預處理和自動化報告生成。它與 JMP 軟件整合，提供進階統計分析和報告生成功能。

## 主要功能
軟件分為四個主要區塊：

### 1. 數據處理 (Data Process)
**統一工作流程：**
- **Open Data**: 選擇並載入數據檔案（支援 CSV、Excel 格式）
- **Exclude Duplicate**: 使用互動式 GUI 排除重複數據項
- **Setup Spec**: 設定製程變數的規格限制
- **Exclude Outlier**: 使用統計方法排除異常值

**工作流程：**
1. 點擊 "Open Data" 選擇數據檔案
2. 檔案名稱會顯示在狀態區域
3. 選擇檔案後所有處理按鈕會啟用
4. 每個功能都作用於同一個選定的檔案，確保一致性

### 2. 製程能力報告 (Process Capability Report)
- **Best Fit 分析**: 適用於非常態分布的進階製程能力分析
- **常態分布分析**: 標準常態分布製程能力分析
- **自動化報告生成**: 自動生成 PDF/PNG 報告
- **JMP 整合**: 與 JMP JSL 腳本無縫整合

### 3. 分析工具 (Analysis Tools)
- **Box Plot 工具**: 生成箱型圖進行數據視覺化
- **相關性分析**: 分析變數間的相關性
- **快速報告**: 生成摘要報告

### 4. 應用程式資訊 (Application Information)
- 版本資訊和系統狀態
- 幫助和文件連結

## 使用方法

### 數據處理工作流程
1. **開啟數據檔案**
   - 點擊 "Open Data" 按鈕
   - 選擇 CSV 或 Excel 檔案
   - 檔案名稱會顯示在狀態區域

2. **排除重複數據**
   - 點擊 "Exclude Duplicate" 按鈕
   - 互動式 GUI 會在 JMP 中開啟
   - 選擇 SN 和 Judge 欄位
   - 點擊 "Excluded!" 處理重複數據

3. **設定規格**
   - 點擊 "Setup Spec" 按鈕
   - 選擇限制檔案（CSV 或 Excel 格式）
   - 程式會生成包含規格的 JSL 腳本
   - 腳本會以時間戳記儲存

4. **排除異常值**
   - 點擊 "Exclude Outlier" 按鈕
   - 選擇要進行異常值分析的變數
   - 程式會生成異常值檢測的 JSL 腳本

### 製程能力分析
1. **Best Fit 分析**
   - 點擊 "Best Fit Distribution" 按鈕
   - 選擇要分析的數據檔案
   - 程式會生成綜合報告

2. **常態分布分析**
   - 點擊 "Normal Distribution" 按鈕
   - 選擇要分析的數據檔案
   - 標準常態分布分析

### JMP 整合
- 所有生成的 JSL 腳本都使用 "Current Data Table()" 邏輯
- 腳本包含錯誤檢查和檔案資訊顯示
- 腳本以時間戳記儲存，便於版本控制

## 檔案格式支援
- **輸入檔案**: CSV, Excel (.xlsx, .xls)
- **輸出檔案**: PDF, PNG, JSL 腳本
- **注意**: 不支援直接讀取 JMP 檔案 (.jmp)

## 常見問題
- 確保您的數據檔案是支援的格式（CSV, Excel）
- 大型數據集處理可能需要較長時間
- 確保 JMP 軟件已正確安裝以執行 JSL 腳本
- 檢查數據檔案中是否包含所有必要欄位

## 系統需求
- Python 3.10 或更高版本
- JMP 軟件（用於執行 JSL 腳本）
- 必要 Python 套件: pandas, openpyxl, tkinter

## 聯繫方式
如有任何問題，請聯繫 SC Hsiao

版本: V1.2  
更新日期: 2025/07/05 