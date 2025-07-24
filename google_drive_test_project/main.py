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
from google_drive_utils import open_google_drive_dialog, open_enterprise_google_drive_dialog

def create_main_window():
    """創建主視窗"""
    root = tk.Tk()
    root.title("Google Drive Test - Data Analysis Tools")
    root.geometry("500x400")
    root.resizable(True, True)
    
    # 設定視窗居中
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (500 // 2)
    y = (root.winfo_screenheight() // 2) - (400 // 2)
    root.geometry(f"500x400+{x}+{y}")
    
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
    title_label.pack(pady=(0, 20))
    
    # 說明文字
    info_label = tk.Label(main_frame, 
                         text="Choose the appropriate method to access your Google Drive files",
                         font=("Arial", 12))
    info_label.pack(pady=(0, 30))
    
    # 按鈕容器框架
    buttons_frame = tk.Frame(main_frame)
    buttons_frame.pack(expand=True, fill="both")
    
    # 公開檔案區域
    public_frame = tk.LabelFrame(buttons_frame, text="🌐 Public Files", font=("Arial", 11, "bold"))
    public_frame.pack(fill="x", pady=(0, 20))
    
    public_desc = tk.Label(public_frame, 
                          text="For files shared with 'Anyone with the link can view'",
                          font=("Arial", 10), fg="gray")
    public_desc.pack(pady=(10, 10))
    
    # 原有的公開檔案按鈕
    public_button = tk.Button(public_frame,
                             text="📁 Fetch Public Data From Google Drive",
                             font=("Arial", 12, "bold"),
                             width=35,
                             height=2,
                             command=open_google_drive_dialog)
    public_button.pack(pady=(0, 15))
    
    # 企業版檔案區域
    enterprise_frame = tk.LabelFrame(buttons_frame, text="🏢 Enterprise Files", font=("Arial", 11, "bold"))
    enterprise_frame.pack(fill="x", pady=(0, 20))
    
    enterprise_desc = tk.Label(enterprise_frame, 
                              text="For company internal files or restricted access files",
                              font=("Arial", 10), fg="gray")
    enterprise_desc.pack(pady=(10, 10))
    
    # 新的企業版按鈕
    enterprise_button = tk.Button(enterprise_frame,
                                 text="🔐 Fetch Enterprise Data (OAuth)",
                                 font=("Arial", 12, "bold"),
                                 width=35,
                                 height=2,
                                 bg="#E3F2FD",  # 淺藍色背景以區分
                                 command=open_enterprise_google_drive_dialog)
    enterprise_button.pack(pady=(0, 15))
    
    # 功能比較說明
    comparison_frame = tk.Frame(main_frame)
    comparison_frame.pack(fill="x", pady=(20, 0))
    
    comparison_text = """
📋 Feature Comparison:

🌐 Public Access:
• ✅ No authentication required
• ✅ Quick and simple
• ❌ Only public shared files

🏢 Enterprise Access:
• ✅ Access company internal files
• ✅ Support private files
• ✅ OAuth 2.0 security
• ⚠️  Requires initial setup
    """
    
    comparison_label = tk.Label(comparison_frame,
                               text=comparison_text,
                               font=("Arial", 9),
                               fg="gray",
                               justify="left")
    comparison_label.pack(anchor="w")
    
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
                           text="Google Drive Test v1.1 (Enterprise Support)",
                           font=("Arial", 8),
                           fg="lightgray")
    version_label.pack(side="bottom")

def main():
    """主函數"""
    print("=== Google Drive 測試專案 ===")
    print("功能：Google Drive 檔案下載工具（支援企業版）")
    print("支援格式：Excel, CSV, JMP")
    print("存取模式：公開檔案 + 企業版檔案")
    print("啟動中...")
    
    # 確保必要目錄存在
    os.makedirs("temp", exist_ok=True)
    
    # 創建GUI
    root = create_main_window()
    create_ui(root)
    
    print("✅ 應用程式已啟動")
    print("選擇適合的存取方式：")
    print("  📁 公開檔案：適用於公開分享的檔案")
    print("  🔐 企業版：適用於公司內部或受限檔案")
    
    # 啟動主迴圈
    root.mainloop()

if __name__ == "__main__":
    main() 