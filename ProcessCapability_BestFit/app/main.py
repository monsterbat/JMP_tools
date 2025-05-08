import tkinter as tk
from tkinter import StringVar, messagebox
import subprocess
import platform

import sys
import os

# 把 A_project 加入 sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules.file_operations import ask_and_open_file, open_analysis_item
from modules.jsl_parser import extract_process_variables, save_jsl_with_vars
from modules.ui_components import create_main_window, create_file_selection_ui, create_jsl_parser_ui
from modules.path_helper import resource_path

def open_file(filepath):
    """開啟指定路徑的檔案"""
    system = platform.system()
    if system == "Windows":
        subprocess.run(f'start "" "{filepath}"', shell=True)
    elif system == "Darwin":  # macOS
        subprocess.run(["open", filepath])
    elif system == "Linux":
        subprocess.run(["xdg-open", filepath])
    else:
        print("Unsupported operating system")

def on_extract():
    """處理JSL程式碼提取並整合到JSL檔案中"""
    input_text = text_input.get("1.0", tk.END)
    extracted = extract_process_variables(input_text)
    
    if extracted.startswith("Process Variables") or extracted.startswith("Unbalanced"):
        messagebox.showerror("Error", extracted)
        return
        
    # 保存到JSL檔案
    save_result, file_path = save_jsl_with_vars(extracted)
    
    # 顯示結果訊息
    if "Successfully saved" in save_result:
        messagebox.showinfo("Success", save_result)
        # 自動開啟新建立的檔案
        if file_path:
            open_file(file_path)
    elif "Save cancelled" in save_result:
        messagebox.showinfo("Notice", save_result)
    else:
        messagebox.showerror("Error", save_result)

def main():
    # 初始化主視窗
    root = create_main_window()
    
    # 用於顯示選取的JMP檔案路徑
    jmp_file_path = StringVar()
    
    # 建立檔案選擇UI
    create_file_selection_ui(root, jmp_file_path, ask_and_open_file, open_analysis_item)
    
    # 建立JSL解析器UI
    global text_input
    text_input = create_jsl_parser_ui(root, on_extract)
    
   
    root.mainloop()

if __name__ == "__main__":
    main()