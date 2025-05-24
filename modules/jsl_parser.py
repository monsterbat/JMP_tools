import os
from tkinter import filedialog, Tk
from modules.path_helper import resource_path

def extract_process_variables(jsl_text):
    """從JSL文本中提取Process Variables部分"""
    keyword = "Process Variables("
    start_idx = jsl_text.find(keyword)
    if start_idx == -1:
        return "Process Variables(...) not found"

    # 開始位置是在 "(" 之後
    start_idx += len(keyword)
    depth = 1
    end_idx = start_idx

    while end_idx < len(jsl_text):
        char = jsl_text[end_idx]
        if char == "(":
            depth += 1
        elif char == ")":
            depth -= 1
            if depth == 0:
                break
        end_idx += 1

    if depth == 0:
        return jsl_text[start_idx:end_idx].strip()
    else:
        return "Unbalanced parentheses, cannot extract correctly"

def read_jsl_template():
    """讀取JSL模板檔案"""
    try:
        with open(resource_path("config/JMP_PC_report_generate_bestFit.jsl"), "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {str(e)}"

def save_jsl_with_vars(vars_text):
    """將變數保存到JSL檔案中"""
    try:
        # 讀取原始檔案
        template = read_jsl_template()
        
        # 找到 myVars 的位置
        start_idx = template.find("myVars = {")
        if start_idx == -1:
            return "myVars definition not found", None
            
        # 找到 myVars 的結束位置
        end_idx = template.find("};", start_idx)
        if end_idx == -1:
            return "Cannot find end of myVars", None
            
        # 構建新的檔案內容
        new_content = template[:start_idx + 10] + vars_text + template[end_idx:]
        
        # 讓使用者選擇保存位置和檔案名稱
        root = Tk()
        root.withdraw()  # 隱藏主視窗
        
        # 預設檔案名稱
        default_filename = "JMP_PC_report_generate_bestFit_new.jsl"
        
        # 開啟檔案儲存對話框
        file_path = filedialog.asksaveasfilename(
            title="Select Save Location",
            defaultextension=".jsl",
            initialfile=default_filename,
            filetypes=[("JSL Files", "*.jsl"), ("All Files", "*.*")]
        )
        
        if not file_path:  # 使用者取消
            return "Save cancelled", None
            
        # 保存新檔案
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
            
        return f"Successfully saved to {os.path.basename(file_path)}", file_path
    except Exception as e:
        return f"Error saving file: {str(e)}", None 