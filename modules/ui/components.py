import tkinter as tk
from tkinter import Label, Button, Text, StringVar, messagebox
from modules.utils.path_helper import resource_path
from modules.utils.version import get_app_title, get_version_info
from modules.core.file_operations import open_duplicate_process, open_user_guide, open_box_plot_tool, open_correlation_tool, open_box_plot_lite, open_quick_report, open_exclude_outliers, open_data_file_and_update_ui, process_duplicate_with_file, process_spec_setup_with_file, process_outliers_with_file
from modules.core.spec_setup import open_spec_setup

def create_main_window():
    """Create the main window"""
    root = tk.Tk()
    root.title(get_app_title())
    root.geometry("850x850")  # 調整高度以適應新的分析工具區塊
    return root


def create_quick_analysis_ui(root):
    """創建Quick analysis區塊，包含Quick report按鈕"""
    frame = tk.LabelFrame(root, bd=2, relief="groove", padx=10, pady=10)
    frame.pack(fill="x", padx=10, pady=10)

    # 置中標題
    title = tk.Label(frame, text="Quick analysis", font=("Arial", 18, "bold"), anchor="center", justify="center")
    title.pack(fill="x", pady=(0, 10))

    # 按鈕框架
    btn_frame = tk.Frame(frame)
    btn_frame.pack()

    # 創建Quick report按鈕
    quick_report_btn = Button(
        btn_frame, 
        text="Quick report", 
        width=16, 
        font=("Arial", 12), 
        command=open_quick_report
    )
    quick_report_btn.pack(pady=5)


def create_data_process_ui(root):
    """Create the Data Process block and four function buttons"""
    frame = tk.LabelFrame(root, bd=2, relief="groove", padx=10, pady=10)
    frame.pack(fill="x", padx=10, pady=10)

    # Center title
    title = tk.Label(frame, text="Data Process", font=("Arial", 18, "bold"), anchor="center", justify="center")
    title.pack(fill="x", pady=(0, 10))

    # 檔案狀態顯示
    file_path_var = StringVar()
    status_label = tk.Label(frame, text="Choose Process data", font=("Arial", 12), anchor="center", justify="center", fg="gray")
    status_label.pack(fill="x", pady=(0, 10))

    # 按鈕框架
    btn_frame = tk.Frame(frame)
    btn_frame.pack()

    # Open Data 按鈕
    open_data_btn = Button(btn_frame, text="Open Data", width=16, font=("Arial", 12))
    open_data_btn.pack(side="left", padx=8)

    # 處理按鈕們（初始時禁用）
    exclude_duplicate_btn = Button(btn_frame, text="Exclude Duplicate", width=16, font=("Arial", 12), state="disabled")
    exclude_duplicate_btn.pack(side="left", padx=8)

    setup_spec_btn = Button(btn_frame, text="Setup Spec", width=16, font=("Arial", 12), state="disabled")
    setup_spec_btn.pack(side="left", padx=8)

    exclude_outlier_btn = Button(btn_frame, text="Exclude Outlier", width=16, font=("Arial", 12), state="disabled")
    exclude_outlier_btn.pack(side="left", padx=8)

    # 處理按鈕清單
    process_buttons = [exclude_duplicate_btn, setup_spec_btn, exclude_outlier_btn]

    # 設定按鈕命令
    open_data_btn.config(command=lambda: open_data_file_and_update_ui(file_path_var, status_label, process_buttons))
    exclude_duplicate_btn.config(command=lambda: process_duplicate_with_file(file_path_var))
    setup_spec_btn.config(command=lambda: process_spec_setup_with_file(file_path_var))
    exclude_outlier_btn.config(command=lambda: process_outliers_with_file(file_path_var))

    return frame 

def create_process_capability_report_ui(root, jmp_file_path, on_select_file, on_open_analysis, on_extract):
    """建立Process Capability Report區塊，包含分析選擇、JSL輸入與提取按鈕"""
    frame = tk.LabelFrame(root, bd=2, relief="groove", padx=10, pady=10)
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    # 置中標題
    title = tk.Label(frame, text="Process Capability Report", font=("Arial", 18, "bold"), anchor="center", justify="center")
    title.pack(fill="x", pady=(0, 10))

    # 按鈕
    btn_open_analysis = Button(frame, text="Select Analysis Items", font=("Arial", 12), command=on_open_analysis, width=30)
    btn_open_analysis.pack(pady=(0, 5))

    # JMP檔案路徑顯示
    lbl_jmp_path = Label(frame, textvariable=jmp_file_path, anchor="center", justify="center", font=("Arial", 11))
    lbl_jmp_path.pack(pady=(0, 5))

    # JSL輸入框
    Label(frame, text="Please paste JSL code:", font=("Arial", 11)).pack(anchor="center", pady=(5, 2))
    text_input = Text(frame, height=10, width=80, font=("Consolas", 12))
    text_input.pack(pady=(0, 10))

    # 提取按鈕
    btn_extract = Button(frame, text="Extract Process Variables Data", font=("Arial", 12), command=on_extract, width=30)
    btn_extract.pack(pady=(0, 5))

    return text_input

def create_analysis_tools_ui(root):
    """創建分析工具區塊，包含BoxPlot和Correlation按鈕"""
    frame = tk.LabelFrame(root, bd=2, relief="groove", padx=10, pady=10)
    frame.pack(fill="x", padx=10, pady=10)

    # 置中標題
    title = tk.Label(frame, text="Analysis Tools", font=("Arial", 18, "bold"), anchor="center", justify="center")
    title.pack(fill="x", pady=(0, 10))

    # 按鈕框架
    btn_frame = tk.Frame(frame)
    btn_frame.pack()

    # 創建Box Plot按鈕
    box_plot_btn = Button(
        btn_frame, 
        text="Box Plot", 
        width=16, 
        font=("Arial", 12), 
        command=open_box_plot_tool
    )
    box_plot_btn.pack(side="left", padx=8)

    # 創建Box Plot Lite按鈕
    box_plot_lite_btn = Button(
        btn_frame, 
        text="Box Plot Lite", 
        width=16, 
        font=("Arial", 12), 
        command=open_box_plot_lite
    )
    box_plot_lite_btn.pack(side="left", padx=8)

    # 創建Correlation按鈕
    correlation_btn = Button(
        btn_frame, 
        text="Correlation", 
        width=16, 
        font=("Arial", 12), 
        command=open_correlation_tool
    )
    correlation_btn.pack(side="left", padx=8)

def create_app_info_ui(root):
    """創建應用程式資訊區塊，包含版本、作者資訊和使用說明按鈕"""
    # 創建資訊框架
    frame = tk.Frame(root)
    frame.pack(fill="x", padx=10, pady=5)
    
    # 中央按鈕框架
    center_frame = tk.Frame(frame)
    center_frame.pack(anchor="center", pady=5)
    
    # 使用說明按鈕 (放在中間)
    help_btn = Button(center_frame, text="Instruction for use", command=open_user_guide, font=("Arial", 12), width=20)
    help_btn.pack(pady=5)
    
    # 版本與作者資訊 (放在底部中央)
    version_label = Label(frame, text=get_version_info(), font=("Arial", 10), anchor="center")
    version_label.pack(fill="x", pady=5)
    
    return frame 