import tkinter as tk
from tkinter import Label, Button, Text, StringVar, messagebox
from modules.utils.path_helper import resource_path
from modules.utils.version import get_app_title, get_version_info
from modules.core.file_operations import open_duplicate_process, open_user_guide, open_box_plot_tool, open_correlation_tool, open_box_plot_lite, open_quick_report, open_exclude_outliers, open_data_file_and_update_ui, process_duplicate_with_file, process_spec_setup_with_file, process_outliers_with_file, open_normal_distribution, open_file_jsl, open_file_jsl_beta, open_best_fit_beta, open_google_drive_file
from modules.core.spec_setup import open_spec_setup

def create_main_window():
    """Create the main window"""
    root = tk.Tk()
    root.title(get_app_title())
    root.geometry("850x800")  # Adjust height to fit new analysis tools section
    return root

def create_header_ui(root):
    """Create header section with description and instruction link"""
    frame = tk.Frame(root)
    frame.pack(fill="x", padx=10, pady=10)

    # Description text
    desc_text = tk.Label(frame, text="This is the toolbox for processing, analyzing, and visualizing optical data.", 
                         font=("Arial", 11), anchor="center", justify="center")
    desc_text.pack(fill="x", pady=(0, 5))

    # Instruction link
    link_text = tk.Label(frame, text="➡️ Click here to view the instructions.", 
                         font=("Arial", 14, "bold"), anchor="center", justify="center", 
                         cursor="hand2")
    link_text.pack(fill="x")
    
    # Bind click event to open user guide
    link_text.bind("<Button-1>", lambda e: open_user_guide())
    
    return frame


def create_quick_analysis_ui(root):
    """Create Quick analysis section with Quick report button"""
    frame = tk.LabelFrame(root, bd=2, relief="groove", padx=10, pady=10)
    frame.pack(fill="x", padx=10, pady=10)

    # Center title
    title = tk.Label(frame, text="Quick analysis", font=("Arial", 18, "bold"), anchor="center", justify="center")
    title.pack(fill="x", pady=(0, 10))

    # Button frame
    btn_frame = tk.Frame(frame)
    btn_frame.pack()

    # Create Quick report button
    quick_report_btn = Button(
        btn_frame, 
        text="Quick report", 
        width=16, 
        font=("Arial", 12), 
        command=open_quick_report
    )
    quick_report_btn.pack(pady=5)


def create_open_data_ui(root):
    """Create independent Open Data section without border"""
    frame = tk.Frame(root)
    frame.pack(fill="x", padx=10, pady=10)

    # Center button frame
    btn_frame = tk.Frame(frame)
    btn_frame.pack()

    # Open Data(jsl) button (隱藏但保留，未來可能使用)
    open_data_jsl_btn = Button(btn_frame, text="Open Data(jsl)", width=16, font=("Arial", 12, "bold"))
    # open_data_jsl_btn.pack(side="left", padx=8, pady=5)  # 註解掉不顯示

    # Open Data button (原本的 Beta 版本，現在是主要版本)
    open_data_btn = Button(btn_frame, text="Open Data", width=16, font=("Arial", 12, "bold"))
    open_data_btn.pack(side="left", padx=8, pady=5)

    # Google Drive button (新增)
    google_drive_btn = Button(btn_frame, text="Google Drive", width=16, font=("Arial", 12, "bold"))
    google_drive_btn.pack(side="left", padx=8, pady=5)

    # Set button commands
    open_data_jsl_btn.config(command=open_file_jsl)
    open_data_btn.config(command=open_file_jsl_beta)
    google_drive_btn.config(command=open_google_drive_file)

    return frame

def create_data_process_ui(root):
    """Create the Data Process block with three function buttons"""
    frame = tk.LabelFrame(root, bd=2, relief="groove", padx=10, pady=10)
    frame.pack(fill="x", padx=10, pady=10)

    # Center title
    title = tk.Label(frame, text="Data Process", font=("Arial", 18, "bold"), anchor="center", justify="center")
    title.pack(fill="x", pady=(0, 10))

    # Button frame
    btn_frame = tk.Frame(frame)
    btn_frame.pack()

    # Process buttons (now always enabled)
    exclude_duplicate_btn = Button(btn_frame, text="Exclude Duplicate", width=16, font=("Arial", 12))
    exclude_duplicate_btn.pack(side="left", padx=8)

    setup_spec_btn = Button(btn_frame, text="Setup Spec", width=16, font=("Arial", 12))
    setup_spec_btn.pack(side="left", padx=8)

    exclude_outlier_btn = Button(btn_frame, text="Exclude Outlier", width=16, font=("Arial", 12))
    exclude_outlier_btn.pack(side="left", padx=8)

    # Set button commands
    exclude_duplicate_btn.config(command=open_duplicate_process)
    setup_spec_btn.config(command=open_spec_setup)
    exclude_outlier_btn.config(command=open_exclude_outliers)

    return frame

def create_process_capability_ui(root, on_open_analysis):
    """Create Process Capability section with Best Fit and Normal distribution buttons"""
    frame = tk.LabelFrame(root, bd=2, relief="groove", padx=10, pady=10)
    frame.pack(fill="x", padx=10, pady=10)

    # Center title
    title = tk.Label(frame, text="Process Capability", font=("Arial", 18, "bold"), anchor="center", justify="center")
    title.pack(fill="x", pady=(0, 10))

    # Button frame
    btn_frame = tk.Frame(frame)
    btn_frame.pack()

    # Normal distribution button
    normal_dist_btn = Button(
        btn_frame, 
        text="Normal distribution", 
        width=16, 
        font=("Arial", 12), 
        command=open_normal_distribution
    )
    normal_dist_btn.pack(side="left", padx=8)

    # Best Fit button (renamed from Select Analysis Items)
    best_fit_btn = Button(
        btn_frame, 
        text="Best Fit", 
        width=16, 
        font=("Arial", 12), 
        command=on_open_analysis
    )
    best_fit_btn.pack(side="left", padx=8)

    # Best Fit(beta) button - 新增的按鈕
    best_fit_beta_btn = Button(
        btn_frame, 
        text="Best Fit(beta)", 
        width=16, 
        font=("Arial", 12), 
        command=open_best_fit_beta
    )
    best_fit_beta_btn.pack(side="left", padx=8)
    
    return frame

def create_report_generate_ui(root, jmp_file_path, on_extract):
    """Create Report Generate section with JSL input and extract button"""
    frame = tk.LabelFrame(root, bd=2, relief="groove", padx=10, pady=10)
    frame.pack(fill="x", padx=10, pady=10)

    # Center title
    title = tk.Label(frame, text="Report Generate", font=("Arial", 18, "bold"), anchor="center", justify="center")
    title.pack(fill="x", pady=(0, 10))

    # JSL input box
    Label(frame, text="Please paste JSL code:", font=("Arial", 11)).pack(anchor="center", pady=(5, 2))
    text_input = Text(frame, height=6, width=80, font=("Consolas", 12))
    text_input.pack(pady=(0, 10))

    # Extract button
    btn_extract = Button(frame, text="Generate in report format", font=("Arial", 12), command=on_extract, width=30)
    btn_extract.pack(pady=(0, 5))

    return text_input

def create_analysis_tools_ui(root):
    """Create analysis tools section with BoxPlot and Correlation buttons"""
    frame = tk.LabelFrame(root, bd=2, relief="groove", padx=10, pady=10)
    frame.pack(fill="x", padx=10, pady=10)

    # Center title
    title = tk.Label(frame, text="Analysis Tools", font=("Arial", 18, "bold"), anchor="center", justify="center")
    title.pack(fill="x", pady=(0, 10))

    # Button frame
    btn_frame = tk.Frame(frame)
    btn_frame.pack()

    # Create Box Plot button
    """
    box_plot_btn = Button(
        btn_frame, 
        text="Box Plot", 
        width=16, 
        font=("Arial", 12), 
        command=open_box_plot_tool
    )
    box_plot_btn.pack(side="left", padx=8)
    

    # Create Box Plot Lite button
    box_plot_lite_btn = Button(
        btn_frame, 
        text="Box Plot Lite", 
        width=16, 
        font=("Arial", 12), 
        command=open_box_plot_lite
    )
    box_plot_lite_btn.pack(side="left", padx=8)
    """
    # Create Correlation button
    correlation_btn = Button(
        btn_frame, 
        text="Correlation", 
        width=16, 
        font=("Arial", 12), 
        command=open_correlation_tool
    )
    correlation_btn.pack(side="left", padx=8)

def create_app_info_ui(root):
    """Create application info section with version, author info and instruction button"""
    # Create info frame
    frame = tk.Frame(root)
    frame.pack(fill="x", padx=10, pady=5)
    
    # Center button frame
    center_frame = tk.Frame(frame)
    center_frame.pack(anchor="center", pady=5)
    
    # Instruction button (placed in center)
    # help_btn = Button(center_frame, text="How to use", command=open_user_guide, font=("Arial", 12), width=20)
    # help_btn.pack(pady=5)
    
    # Version and author info (placed at bottom center)
    # version_label = Label(frame, text=get_version_info(), font=("Arial", 10), anchor="center")
    # version_label.pack(fill="x", pady=5)
    
    return frame 