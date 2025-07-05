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
    root.geometry("850x850")  # Adjust height to fit new analysis tools section
    return root


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


def create_data_process_ui(root):
    """Create the Data Process block and four function buttons"""
    frame = tk.LabelFrame(root, bd=2, relief="groove", padx=10, pady=10)
    frame.pack(fill="x", padx=10, pady=10)

    # Center title
    title = tk.Label(frame, text="Data Process", font=("Arial", 18, "bold"), anchor="center", justify="center")
    title.pack(fill="x", pady=(0, 10))

    # File status display
    file_path_var = StringVar()
    status_label = tk.Label(frame, text="Choose Process data", font=("Arial", 12), anchor="center", justify="center", fg="gray")
    status_label.pack(fill="x", pady=(0, 10))

    # Button frame
    btn_frame = tk.Frame(frame)
    btn_frame.pack()

    # Open Data button
    open_data_btn = Button(btn_frame, text="Open Data", width=16, font=("Arial", 12))
    open_data_btn.pack(side="left", padx=8)

    # Process buttons (initially disabled)
    exclude_duplicate_btn = Button(btn_frame, text="Exclude Duplicate", width=16, font=("Arial", 12), state="disabled")
    exclude_duplicate_btn.pack(side="left", padx=8)

    setup_spec_btn = Button(btn_frame, text="Setup Spec", width=16, font=("Arial", 12), state="disabled")
    setup_spec_btn.pack(side="left", padx=8)

    exclude_outlier_btn = Button(btn_frame, text="Exclude Outlier", width=16, font=("Arial", 12), state="disabled")
    exclude_outlier_btn.pack(side="left", padx=8)

    # Process button list
    process_buttons = [exclude_duplicate_btn, setup_spec_btn, exclude_outlier_btn]

    # Set button commands
    open_data_btn.config(command=lambda: open_data_file_and_update_ui(file_path_var, status_label, process_buttons))
    exclude_duplicate_btn.config(command=lambda: process_duplicate_with_file(file_path_var))
    setup_spec_btn.config(command=lambda: process_spec_setup_with_file(file_path_var))
    exclude_outlier_btn.config(command=lambda: process_outliers_with_file(file_path_var))

    return frame 

def create_process_capability_report_ui(root, jmp_file_path, on_select_file, on_open_analysis, on_extract):
    """Create Process Capability Report section with analysis selection, JSL input and extract button"""
    frame = tk.LabelFrame(root, bd=2, relief="groove", padx=10, pady=10)
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    # Center title
    title = tk.Label(frame, text="Process Capability Report", font=("Arial", 18, "bold"), anchor="center", justify="center")
    title.pack(fill="x", pady=(0, 10))

    # Button
    btn_open_analysis = Button(frame, text="Select Analysis Items", font=("Arial", 12), command=on_open_analysis, width=30)
    btn_open_analysis.pack(pady=(0, 5))

    # JMP file path display
    lbl_jmp_path = Label(frame, textvariable=jmp_file_path, anchor="center", justify="center", font=("Arial", 11))
    lbl_jmp_path.pack(pady=(0, 5))

    # JSL input box
    Label(frame, text="Please paste JSL code:", font=("Arial", 11)).pack(anchor="center", pady=(5, 2))
    text_input = Text(frame, height=10, width=80, font=("Consolas", 12))
    text_input.pack(pady=(0, 10))

    # Extract button
    btn_extract = Button(frame, text="Extract Process Variables Data", font=("Arial", 12), command=on_extract, width=30)
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
    help_btn = Button(center_frame, text="Instruction for use", command=open_user_guide, font=("Arial", 12), width=20)
    help_btn.pack(pady=5)
    
    # Version and author info (placed at bottom center)
    version_label = Label(frame, text=get_version_info(), font=("Arial", 10), anchor="center")
    version_label.pack(fill="x", pady=5)
    
    return frame 