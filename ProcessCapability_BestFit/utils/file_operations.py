import os
import platform
import subprocess
from tkinter import Tk, filedialog

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

def ask_and_open_file():
    """開啟檔案選擇對話框並開啟選擇的檔案"""
    root = Tk()
    root.withdraw()  # 隱藏主視窗
    filepath = filedialog.askopenfilename(
        title="Select File to Open",
        filetypes=[("JMP Files", "*.jmp"), ("All Files", "*.*")]
    )
    if filepath:
        print("Selected file:", filepath)
        open_file(filepath)
        return filepath
    else:
        print("No file selected")
        return None

def open_analysis_item():
    """開啟分析項目檔案"""
    open_file("best_fit_distribution.jsl") 