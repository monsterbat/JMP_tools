import os
import platform
import subprocess
import tkinter as tk
from tkinter import Tk, filedialog, messagebox
from modules.utils.path_helper import resource_path
from modules.core.jsl_parser import extract_process_variables, save_jsl_with_vars
from modules.utils.constants import (
    FILE_TYPE_JMP, FILE_TYPE_ALL, FILE_EXT_JMP, FILE_EXT_ALL,
    MSG_TITLE_SUCCESS, MSG_TITLE_ERROR, MSG_TITLE_NOTICE,
    MSG_NO_SCRIPT_TEMPLATE
)

def open_file(filepath):
    """開啟指定路徑的檔案"""
    system = platform.system()
    if system == "Windows":
        os.startfile(filepath)
    elif system == "Darwin":  # macOS
        subprocess.run(["open", filepath])
    elif system == "Linux":
        subprocess.run(["xdg-open", filepath])
    else:
        print("Unsupported operating system")

def ask_and_open_file(jmp_file_path=None):
    """開啟檔案選擇對話框並開啟選擇的檔案"""
    root = Tk()
    root.withdraw()  # 隱藏主視窗
    filepath = filedialog.askopenfilename(
        title="Select File to Open",
        filetypes=[(FILE_TYPE_JMP, FILE_EXT_JMP), (FILE_TYPE_ALL, FILE_EXT_ALL)]
    )
    if filepath:
        print("Selected file:", filepath)
        open_file(filepath)
        if jmp_file_path:
            jmp_file_path.set(filepath)
        return filepath
    else:
        print("No file selected")
        return None

def open_analysis_item(file_path=None):
    """開啟分析項目檔案"""
    jsl_path = resource_path("config/best_fit_distribution.jsl")
    open_file(jsl_path)

def open_duplicate_process():
    """開啟Exclude Duplicate功能的JSL檔案"""
    jsl_path = resource_path("config/duplicate_process.jsl")
    open_file(jsl_path)

def open_box_plot_tool():
    """開啟Box Plot分析工具UI界面"""
    # 使用啟動器模塊來避免循環導入問題
    from modules.utils.ui_launcher import launch_box_plot_ui
    launch_box_plot_ui()

def open_correlation_tool():
    """開啟Correlation分析工具"""
    # 檢查配置檔案是否存在
    jsl_path = resource_path("config/correlation_tool.jsl")
    if os.path.exists(jsl_path):
        open_file(jsl_path)
    else:
        messagebox.showinfo(
            MSG_TITLE_INFO, 
            MSG_NO_SCRIPT_TEMPLATE.format("Correlation", "scripts/jsl/correlation_tool.jsl")
        )

def open_user_guide():
    """開啟使用說明文件"""
    guide_path = resource_path("config/user_guide.md")
    open_file(guide_path)

def open_box_plot_lite():
    """開啟Box Plot Lite分析工具的JSL腳本"""
    jsl_path = resource_path("config/box_plot_tool.jsl")
    open_file(jsl_path)

def open_quick_report():
    """開啟Quick Report功能"""
    from modules.ui.quick_report_ui import open_quick_report_window
    open_quick_report_window()

def on_extract(text_input):
    """處理JSL程式碼提取並整合到JSL檔案中
    Args:
        text_input (tk.Text): 包含JSL程式碼的文字輸入框
    """
    input_text = text_input.get("1.0", tk.END)
    extracted = extract_process_variables(input_text)
    
    if extracted.startswith("Process Variables") or extracted.startswith("Unbalanced"):
        messagebox.showerror(MSG_TITLE_ERROR, extracted)
        return
        
    # 儲存到JSL檔案
    save_result, file_path = save_jsl_with_vars(extracted)
    
    # 顯示結果訊息
    if "Successfully saved" in save_result:
        messagebox.showinfo(MSG_TITLE_SUCCESS, save_result)
        # 自動開啟新建立的檔案
        if file_path:
            open_file(file_path)
    elif "Save cancelled" in save_result:
        messagebox.showinfo(MSG_TITLE_NOTICE, save_result)
    else:
        messagebox.showerror(MSG_TITLE_ERROR, save_result) 