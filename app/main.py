import tkinter as tk
from tkinter import StringVar
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules.core.file_operations import ask_and_open_file, open_analysis_item, on_extract
from modules.ui.components import create_main_window, create_data_process_ui, create_process_capability_report_ui, create_analysis_tools_ui, create_app_info_ui, create_quick_analysis_ui

def main():
    # Initialize the main window
    root = create_main_window()
    
    # Create Quick analysis UI at the top
    #create_quick_analysis_ui(root)
    
    create_data_process_ui(root)  
    # 用於顯示選取的JMP檔案路徑
    jmp_file_path = StringVar()
    
    # Create the Process Capability Report UI
    global text_input
    text_input = create_process_capability_report_ui(
        root, jmp_file_path, ask_and_open_file, open_analysis_item, lambda: on_extract(text_input)
    )
    
    # Create the Analysis Tools UI
    create_analysis_tools_ui(root)
    
    # Create the application info UI at the bottom
    create_app_info_ui(root)
    
    root.mainloop()

if __name__ == "__main__":
    main()