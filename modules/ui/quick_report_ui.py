import tkinter as tk
from tkinter import Label, Button, StringVar, filedialog, messagebox
from tkinter import ttk
import os

class QuickReportWindow:
    def __init__(self, parent=None):
        self.window = tk.Toplevel(parent) if parent else tk.Tk()
        self.window.title("Quick report")
        self.window.geometry("600x300")
        self.window.resizable(False, False)
        
        # 變數來儲存選擇的檔案路徑
        self.data_file_path = StringVar(self.window)
        self.setting_file_path = StringVar(self.window)
        
        # 設定預設顯示文字
        self.data_file_display = StringVar(self.window, value="未選擇檔案")
        self.setting_file_display = StringVar(self.window, value="未選擇檔案")
        
        self.setup_ui()
        
        # 讓視窗置中
        self.center_window()
    
    def setup_ui(self):
        """設置界面元素"""
        # 主框架
        main_frame = tk.Frame(self.window, relief='raised', bd=2)
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # 標題
        title_label = tk.Label(
            main_frame, 
            text="Quick report", 
            font=("Arial", 16, "bold")
        )
        title_label.pack(pady=(10, 20))
        
        # 檔案選擇區域
        file_frame = tk.Frame(main_frame)
        file_frame.pack(pady=10)
        
        # Data File 行
        data_row = tk.Frame(file_frame)
        data_row.pack(fill='x', pady=5)
        
        data_btn = tk.Button(
            data_row,
            text="1. Data File",
            width=15,
            font=("Arial", 11),
            command=self.select_data_file
        )
        data_btn.pack(side='left', padx=(0, 20))
        
        self.data_label = tk.Label(
            data_row,
            textvariable=self.data_file_display,
            font=("Arial", 11),
            anchor='w'
        )
        self.data_label.pack(side='left', fill='x', expand=True)
        
        # Setting File 行
        setting_row = tk.Frame(file_frame)
        setting_row.pack(fill='x', pady=5)
        
        setting_btn = tk.Button(
            setting_row,
            text="2. Setting File",
            width=15,
            font=("Arial", 11),
            command=self.select_setting_file
        )
        setting_btn.pack(side='left', padx=(0, 20))
        
        self.setting_label = tk.Label(
            setting_row,
            textvariable=self.setting_file_display,
            font=("Arial", 11),
            anchor='w'
        )
        self.setting_label.pack(side='left', fill='x', expand=True)
        
        # Generate 按鈕
        generate_btn = tk.Button(
            main_frame,
            text="Generate",
            width=15,
            font=("Arial", 12),
            command=self.generate_report
        )
        generate_btn.pack(pady=(30, 10))
    
    def center_window(self):
        """讓視窗在螢幕中央顯示"""
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f'{width}x{height}+{x}+{y}')
    
    def select_data_file(self):
        """選擇數據檔案"""
        file_path = filedialog.askopenfilename(
            title="選擇數據檔案",
            filetypes=[
                ("Excel files", "*.xlsx *.xls"),
                ("CSV files", "*.csv"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            print(f"選擇的數據檔案路徑: {file_path}")  # 調試資訊
            self.data_file_path.set(file_path)
            # 只顯示檔案名稱，不包含路徑
            filename = os.path.basename(file_path)
            print(f"提取的檔案名稱: {filename}")  # 調試資訊
            self.data_file_display.set(filename)
            print(f"設定後的顯示值: {self.data_file_display.get()}")  # 調試資訊
            # 強制更新界面
            self.window.update_idletasks()
    
    def select_setting_file(self):
        """選擇設定檔案"""
        file_path = filedialog.askopenfilename(
            title="選擇設定檔案",
            filetypes=[
                ("JSON files", "*.json"),
                ("XML files", "*.xml"),
                ("Config files", "*.cfg *.ini"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            print(f"選擇的設定檔案路徑: {file_path}")  # 調試資訊
            self.setting_file_path.set(file_path)
            # 只顯示檔案名稱，不包含路徑
            filename = os.path.basename(file_path)
            print(f"提取的檔案名稱: {filename}")  # 調試資訊
            self.setting_file_display.set(filename)
            print(f"設定後的顯示值: {self.setting_file_display.get()}")  # 調試資訊
            # 強制更新界面
            self.window.update_idletasks()
    
    def generate_report(self):
        """生成報告（目前為預留功能）"""
        data_file = self.data_file_path.get()
        setting_file = self.setting_file_path.get()
        
        if not data_file:
            messagebox.showwarning("警告", "請選擇數據檔案")
            return
        
        if not setting_file:
            messagebox.showwarning("警告", "請選擇設定檔案")
            return
        
        # 目前顯示選擇的檔案資訊，之後可以替換為實際的報告生成邏輯
        messagebox.showinfo(
            "檔案資訊", 
            f"數據檔案: {data_file}\n設定檔案: {setting_file}\n\nGenerate 功能開發中..."
        )

def open_quick_report_window(parent=None):
    """開啟 Quick report 視窗"""
    quick_report = QuickReportWindow(parent)
    return quick_report 