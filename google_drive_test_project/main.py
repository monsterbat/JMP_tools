#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Google Drive 測試專案

簡化版的 Google Drive 檔案下載和開啟工具
功能：點擊按鈕開啟 Google Drive 檔案連接器

作者：Data Analysis Tools
"""

import tkinter as tk
from tkinter import ttk
import os
import sys

# 匯入我們的 Google Drive 工具
from google_drive_utils import open_google_drive_dialog

def create_main_window():
    """創建主視窗"""
    root = tk.Tk()
    root.title("Google Drive Test - Data Analysis Tools")
    root.geometry("400x300")
    root.resizable(True, True)
    
    # 設定視窗居中
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (400 // 2)
    y = (root.winfo_screenheight() // 2) - (300 // 2)
    root.geometry(f"400x300+{x}+{y}")
    
    return root

def create_ui(root):
    """創建使用者介面"""
    
    # 主框架
    main_frame = tk.Frame(root)
    main_frame.pack(expand=True, fill="both", padx=20, pady=20)
    
    # 標題
    title_label = tk.Label(main_frame, 
                          text="Google Drive File Connector", 
                          font=("Arial", 18, "bold"))
    title_label.pack(pady=(0, 30))
    
    # 說明文字
    info_label = tk.Label(main_frame, 
                         text="Click the button below to fetch data from Google Drive",
                         font=("Arial", 12))
    info_label.pack(pady=(0, 40))
    
    # 主要按鈕 - 使用預設顏色
    fetch_button = tk.Button(main_frame,
                           text="Fetch Data From Google Drive",
                           font=("Arial", 14, "bold"),
                           width=25,
                           height=2,
                           command=open_google_drive_dialog)
    fetch_button.pack(pady=20)
    
    # 狀態信息
    status_frame = tk.Frame(main_frame)
    status_frame.pack(side="bottom", fill="x", pady=(20, 0))
    
    status_label = tk.Label(status_frame, 
                           text="Ready to connect to Google Drive",
                           font=("Arial", 10),
                           fg="gray")
    status_label.pack()
    
    # 版本信息
    version_label = tk.Label(status_frame,
                           text="Google Drive Test v1.0",
                           font=("Arial", 8),
                           fg="lightgray")
    version_label.pack(side="bottom")

def main():
    """主函數"""
    print("=== Google Drive 測試專案 ===")
    print("功能：簡化版 Google Drive 檔案下載工具")
    print("支援格式：Excel, CSV, JMP")
    print("啟動中...")
    
    # 確保必要目錄存在
    os.makedirs("temp", exist_ok=True)
    
    # 創建GUI
    root = create_main_window()
    create_ui(root)
    
    print("✅ 應用程式已啟動")
    print("點擊 'Fetch Data From Google Drive' 按鈕開始使用")
    
    # 啟動主迴圈
    root.mainloop()

if __name__ == "__main__":
    main() 