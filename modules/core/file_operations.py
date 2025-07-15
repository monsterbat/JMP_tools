import os
import platform
import subprocess
import tkinter as tk
from tkinter import Tk, filedialog, messagebox
from modules.utils.path_helper import resource_path
from modules.core.jsl_parser import extract_process_variables, save_jsl_with_vars
from modules.utils.constants import (
    FILE_TYPE_JMP, FILE_TYPE_ALL, FILE_EXT_JMP, FILE_EXT_ALL,
    MSG_TITLE_SUCCESS, MSG_TITLE_ERROR, MSG_TITLE_NOTICE, MSG_TITLE_INFO,
    MSG_NO_SCRIPT_TEMPLATE
)

# 全域變數來追蹤當前打開的檔案路徑（Beta功能用）
current_file_path_beta = None

def open_file(filepath):
    """Open file at specified path"""
    system = platform.system()
    if system == "Windows":
        os.startfile(filepath)
    elif system == "Darwin":  # macOS
        subprocess.run(["open", filepath])
    elif system == "Linux":
        subprocess.run(["xdg-open", filepath])
    else:
        print("Unsupported operating system")

def open_with_jmp(filepath):
    """Open file specifically with JMP application"""
    system = platform.system()
    
    try:
        if system == "Darwin":  # macOS
            # 嘗試多種 JMP 應用程式名稱（常見的排在前面）
            jmp_app_names = ["JMP 18", "JMP 19", "JMP 17", "JMP Pro 18", "JMP Pro 19", "JMP Pro 17", "JMP", "JMP Pro"]
            
            jmp_opened = False
            for app_name in jmp_app_names:
                result = subprocess.run(["open", "-a", app_name, filepath], 
                                      capture_output=True, text=True)
                
                if result.returncode == 0:
                    jmp_opened = True
                    break
            
            if not jmp_opened:
                # 如果找不到 JMP，回到一般開啟方式
                open_file(filepath)
                    
        elif system == "Windows":
            # Windows 版本 - 可能需要調整 JMP 路徑
            jmp_paths = [
                r"C:\Program Files\SAS\JMP\19\jmp.exe",
                r"C:\Program Files\SAS\JMP\18\jmp.exe",
                r"C:\Program Files\SAS\JMP\17\jmp.exe",
                r"C:\Program Files\SAS\JMP\16\jmp.exe", 
                r"C:\Program Files\SAS\JMP\15\jmp.exe",
                r"C:\Program Files (x86)\SAS\JMP\19\jmp.exe",
                r"C:\Program Files (x86)\SAS\JMP\18\jmp.exe",
                r"C:\Program Files (x86)\SAS\JMP\17\jmp.exe",
                r"C:\Program Files (x86)\SAS\JMP\16\jmp.exe",
                r"C:\Program Files (x86)\SAS\JMP\15\jmp.exe"
            ]
            
            jmp_found = False
            for jmp_path in jmp_paths:
                if os.path.exists(jmp_path):
                    subprocess.run([jmp_path, filepath])
                    jmp_found = True
                    break
            
            if not jmp_found:
                print("JMP not found, using default application")
                open_file(filepath)
                
        else:
            # Linux 或其他系統，回到一般開啟方式
            print("JMP path not configured for this system, using default application")
            open_file(filepath)
            
    except Exception as e:
        print(f"Error opening with JMP: {e}")
        # 如果有錯誤，回到一般開啟方式
        open_file(filepath)

def ask_and_open_file(jmp_file_path=None):
    """Open file selection dialog and open selected file"""
    root = Tk()
    root.withdraw()  # Hide main window
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
    """Open analysis item file"""
    jsl_path = resource_path("config/best_fit_distribution.jsl")
    open_file(jsl_path)

def open_duplicate_process():
    """Open Exclude Duplicate JSL file"""
    jsl_path = resource_path("config/duplicate_process.jsl")
    open_file(jsl_path)

def open_box_plot_tool():
    """Open Box Plot analysis tool UI"""
    # Use launcher module to avoid circular import issues
    from modules.utils.ui_launcher import launch_box_plot_ui
    launch_box_plot_ui()

def open_correlation_tool():
    """Open Correlation analysis tool"""
    # Check if configuration file exists
    jsl_path = resource_path("config/correlation_tool.jsl")
    if os.path.exists(jsl_path):
        open_file(jsl_path)
    else:
        messagebox.showinfo(
            MSG_TITLE_INFO, 
            MSG_NO_SCRIPT_TEMPLATE.format("Correlation", "scripts/jsl/correlation_tool.jsl")
        )

def open_user_guide():
    """Open user guide document"""
    guide_path = resource_path("docs/Data Analysis Tools SOP.pdf")
    open_file(guide_path)

def open_box_plot_lite():
    """Open Box Plot Lite analysis tool JSL script"""
    jsl_path = resource_path("config/box_plot_tool.jsl")
    open_file(jsl_path)

def open_quick_report():
    """Open Quick Report function"""
    from modules.ui.quick_report_ui import open_quick_report_window
    open_quick_report_window()

def open_exclude_outliers():
    """Open Exclude Outliers JSL file"""
    jsl_path = resource_path("config/explore_outliers.jsl")
    if os.path.exists(jsl_path):
        open_file(jsl_path)
    else:
        messagebox.showinfo(
            MSG_TITLE_INFO, 
            MSG_NO_SCRIPT_TEMPLATE.format("Exclude Outliers", "scripts/jsl/explore_outliers.jsl")
        )

def select_data_file():
    """Select data file but don't open it"""
    root = Tk()
    root.withdraw()  # Hide main window
    filepath = filedialog.askopenfilename(
        title="Select Data File",
        filetypes=[(FILE_TYPE_JMP, FILE_EXT_JMP), (FILE_TYPE_ALL, FILE_EXT_ALL)]
    )
    root.destroy()
    return filepath

def open_data_file_and_update_ui(file_path_var, status_label, process_buttons):
    """Open data file and update UI status"""
    filepath = select_data_file()
    if filepath:
        # Open file
        open_file(filepath)
        # Update UI
        import os
        filename = os.path.basename(filepath)
        file_path_var.set(filepath)
        status_label.config(text=filename)
        # Enable process buttons
        for btn in process_buttons:
            btn.config(state="normal")
        print(f"Selected and opened file: {filepath}")
        return filepath
    else:
        print("No file selected")
        return None

def process_duplicate_with_file(file_path_var):
    """Execute Exclude Duplicate with specified file"""
    filepath = file_path_var.get()
    if not filepath:
        messagebox.showwarning("Warning", "Please select a data file first")
        return
    
    # Here we can pass file path to JSL script
    # Currently just open JSL file for manual operation
    jsl_path = resource_path("config/duplicate_process.jsl")
    open_file(jsl_path)

def process_spec_setup_with_file(file_path_var):
    """Execute Setup Spec with specified file"""
    filepath = file_path_var.get()
    if not filepath:
        messagebox.showwarning("Warning", "Please select a data file first")
        return
    
    # Call spec_setup function
    from modules.core.spec_setup import open_spec_setup
    open_spec_setup()

def process_outliers_with_file(file_path_var):
    """Execute Exclude Outlier with specified file"""
    filepath = file_path_var.get()
    if not filepath:
        messagebox.showwarning("Warning", "Please select a data file first")
        return
    
    # Open outliers JSL file
    jsl_path = resource_path("config/explore_outliers.jsl")
    if os.path.exists(jsl_path):
        open_file(jsl_path)
    else:
        messagebox.showinfo(
            MSG_TITLE_INFO, 
            MSG_NO_SCRIPT_TEMPLATE.format("Exclude Outliers", "scripts/jsl/explore_outliers.jsl")
        )

def on_extract(text_input):
    """Process JSL code extraction and integrate into JSL file
    Args:
        text_input (tk.Text): Text input box containing JSL code
    """
    input_text = text_input.get("1.0", tk.END)
    extracted = extract_process_variables(input_text)
    
    if extracted.startswith("Process Variables") or extracted.startswith("Unbalanced"):
        messagebox.showerror(MSG_TITLE_ERROR, extracted)
        return
        
    # Save to JSL file (use Beta path if available)
    save_result, file_path = save_jsl_with_vars(extracted, current_file_path_beta)
    
    # Display result message
    if "Successfully saved" in save_result:
        messagebox.showinfo(MSG_TITLE_SUCCESS, save_result)
        # Automatically open newly created file
        if file_path:
            open_file(file_path)
    elif "Save cancelled" in save_result:
        messagebox.showinfo(MSG_TITLE_NOTICE, save_result)
    else:
        messagebox.showerror(MSG_TITLE_ERROR, save_result) 

def open_normal_distribution():
    """Open Normal distribution JSL file"""
    jsl_path = resource_path("config/jmp_pc_report_generate_normal.jsl")
    if os.path.exists(jsl_path):
        open_file(jsl_path)
    else:
        messagebox.showinfo(
            MSG_TITLE_INFO, 
            MSG_NO_SCRIPT_TEMPLATE.format("Normal distribution", "scripts/jsl/jmp_pc_report_generate_normal.jsl")
        ) 

def open_file_jsl():
    """Open file selection JSL script"""
    jsl_path = resource_path("scripts/jsl/open_file.jsl")
    if os.path.exists(jsl_path):
        open_file(jsl_path)
    else:
        messagebox.showinfo(
            MSG_TITLE_INFO, 
            MSG_NO_SCRIPT_TEMPLATE.format("Open File", "scripts/jsl/open_file.jsl")
        )

def open_file_jsl_beta():
    """Open file selection dialog and track file path (Beta)"""
    global current_file_path_beta
    
    root = Tk()
    root.withdraw()  # 隱藏主視窗
    
    # 打開檔案選擇對話框（支援 CSV 和 JMP）
    file_path = filedialog.askopenfilename(
        title="Choose data file (Beta)",
        filetypes=[("CSV Files", "*.csv"), ("JMP Files", "*.jmp"), ("All Files", "*.*")]
    )
    
    if file_path:
        # 保存當前檔案路徑
        current_file_path_beta = file_path
        
        # 根據檔案類型決定開啟方式
        file_extension = os.path.splitext(file_path)[1].lower()
        
        if file_extension == '.jmp':
            # .jmp 檔案用系統預設方式開啟（通常已設定為 JMP）
            open_file(file_path)
        else:
            # 其他檔案（如 CSV）強制用 JMP 開啟
            open_with_jmp(file_path) 