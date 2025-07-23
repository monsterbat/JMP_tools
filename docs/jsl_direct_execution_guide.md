# JSL 直接執行功能使用指南

## 📋 概述

本指南說明如何使用創建的 JSL 測試檔案來直接執行 GUI 按鈕的功能，而不需要顯示圖形介面。

## 📁 檔案說明

### 1. `test_direct_execution.jsl`
- **功能**: 提供簡單的選擇對話框
- **適用**: 需要手動選擇執行功能的情況
- **特點**: 
  - 有基本的GUI選擇介面
  - 可以設定路徑
  - 支援測試功能

### 2. `auto_execute_mtp.jsl`  
- **功能**: 完全自動化執行
- **適用**: 完全無人值守的自動化執行
- **特點**:
  - 無任何GUI介面
  - 自動批次執行
  - 詳細的執行記錄

## 🚀 使用方法

### 方法1: 使用選擇對話框版本

1. **開啟檔案**:
   ```
   在 JMP 中開啟 scripts/jsl/test_direct_execution.jsl
   ```

2. **設定路徑** (如果需要):
   - 點擊「設定路徑」按鈕
   - 選擇 JSL 檔案所在目錄

3. **執行功能**:
   - 點擊「SHP MTP」執行 SHP MTP 功能
   - 點擊「BOE MTP」執行 BOE MTP 功能

### 方法2: 使用完全自動化版本

1. **編輯設定**:
   ```jsl
   // 在 auto_execute_mtp.jsl 中修改路徑
   folderPath = "/your/actual/path/to/jsl/files";
   ```

2. **選擇執行模式**:
   ```jsl
   // 取消註解想要執行的功能
   
   // 只執行 SHP MTP
   ExecuteSHPMTP();
   
   // 只執行 BOE MTP  
   ExecuteBOEMTP();
   
   // 批次執行所有功能 (預設)
   ExecuteAllMTP();
   ```

3. **執行**:
   - 在 JMP 中開啟並執行 `auto_execute_mtp.jsl`

## ⚙️ 路徑設定選項

### 選項1: 完整絕對路徑
```jsl
folderPath = "/Users/yourname/Documents/JSL_Files";
```

### 選項2: 相對路徑
```jsl
folderPath = File Directory(Get Default Directory()) || "../templates";
```

### 選項3: 自動偵測 (如果檔案在同一目錄)
```jsl
folderPath = File Directory($PROGRAM);
```

### 選項4: 空路徑 (使用預設路徑)
```jsl
folderPath = "";  // 會嘗試使用檔案的絕對路徑
```

## 🔧 自訂功能

### 新增其他按鈕功能

如果您的 GUI 有其他按鈕，可以按照以下模式新增：

```jsl
// 新增執行函數
ExecuteYourFunction = Function({},
    Try(
        Show("正在執行您的功能...");
        Include(folderPath || "/Your_JSL_File.jsl");
        Show("✅ 執行完成");
    ,
        Show("❌ 執行失敗: " || exception_msg);
    );
);

// 在執行區域呼叫
ExecuteYourFunction();
```

### 條件執行

```jsl
// 例如：只在特定日期執行
If(Day Of Week(Today()) == 1,  // 星期一
    ExecuteSHPMTP();
);

// 例如：根據時間執行不同功能
currentHour = Hour(Today());
If(currentHour < 12,
    ExecuteSHPMTP();
,
    ExecuteBOEMTP();
);
```

### 迴圈執行

```jsl
// 重複執行多次
For(i = 1, i <= 3, i++,
    Show("第 " || Char(i) || " 次執行");
    ExecuteSHPMTP();
    Wait(5);  // 等待5秒
);
```

## 📊 執行記錄

### 自動記錄功能

```jsl
// 記錄到檔案
logFile = "mtp_execution_log.txt";
logContent = "執行時間: " || Format(Today(), "yyyy/mm/dd h:m:s") || 
              " - 功能: SHP MTP - 狀態: 成功\n";
Save Text File(logFile, logContent, "append");
```

### 執行統計

```jsl
// 統計執行時間
startTime = Today();
ExecuteSHPMTP();
endTime = Today();
duration = (endTime - startTime) * 24 * 60 * 60;  // 秒
Show("執行耗時: " || Round(duration, 2) || " 秒");
```

## ❗ 常見問題

### Q1: 執行失敗，提示找不到檔案
**解決方案**:
1. 檢查 `folderPath` 設定是否正確
2. 確認 JSL 檔案確實存在於指定路徑
3. 檢查檔案名稱是否正確

### Q2: 想要完全靜默執行
**解決方案**:
將所有 `Show()` 語句註解掉或刪除：
```jsl
// Show("正在執行...");  // 註解掉這行
Include(filePath);
```

### Q3: 需要傳遞參數給被執行的 JSL
**解決方案**:
在執行前設定全域變數：
```jsl
// 設定參數
globalParam1 = "value1";
globalParam2 = 123;

// 然後執行
Include(filePath);
```

## 🎯 最佳實踐

1. **測試執行**: 先在小範圍測試，確認功能正常
2. **錯誤處理**: 始終使用 `Try()` 包裝執行程式碼
3. **記錄輸出**: 保留執行記錄便於除錯
4. **路徑檢查**: 執行前驗證檔案路徑
5. **備份原檔**: 執行前備份重要檔案

## 📝 範例腳本

完整的使用範例請參考：
- `scripts/jsl/test_direct_execution.jsl`
- `scripts/jsl/auto_execute_mtp.jsl`

---

**作者**: Data Analysis Tools  
**更新日期**: 2024年7月  
**版本**: 1.0 