#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Google Drive 工具模組

提供 Google Drive 檔案下載和處理功能

作者：Data Analysis Tools
"""

import os
import re
import platform
import subprocess
import tkinter as tk
from tkinter import messagebox
import tempfile

def extract_google_drive_file_id(url):
    """從 Google Drive URL 中提取檔案 ID"""
    patterns = [
        r'/file/d/([a-zA-Z0-9-_]+)',  # https://drive.google.com/file/d/FILE_ID/view
        r'id=([a-zA-Z0-9-_]+)',       # https://drive.google.com/open?id=FILE_ID
        r'/d/([a-zA-Z0-9-_]+)/'       # 其他格式
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    
    return None

def download_google_drive_file(url, target_dir=None):
    """下載 Google Drive 檔案到本地"""
    try:
        import gdown
        
        # 提取檔案 ID
        file_id = extract_google_drive_file_id(url)
        if not file_id:
            raise Exception("無法從 URL 中提取 Google Drive 檔案 ID")
        
        # 設定下載目錄 - 優先使用專案的 temp 目錄
        if target_dir is None:
            target_dir = os.path.join(os.getcwd(), 'temp')
        
        # 確保目錄存在
        os.makedirs(target_dir, exist_ok=True)
        
        # 創建下載 URL
        download_url = f"https://drive.google.com/uc?id={file_id}"
        
        # 指定完整的輸出檔案路徑
        output_filename = f"google_drive_{file_id}.csv"
        output_path = os.path.join(target_dir, output_filename)
        
        # 下載檔案
        print(f"正在下載 Google Drive 檔案 (ID: {file_id})...")
        print(f"下載位置: {output_path}")
        
        downloaded_file = gdown.download(download_url, output=output_path, quiet=False)
        
        if downloaded_file and os.path.exists(output_path):
            print(f"✅ 檔案下載成功: {output_path}")
            return output_path
        else:
            raise Exception("檔案下載失敗或檔案不存在")
            
    except ImportError:
        raise Exception("請先安裝 gdown 套件: pip install gdown")
    except Exception as e:
        raise Exception(f"下載 Google Drive 檔案失敗: {str(e)}")

def open_file_with_system(filepath):
    """用系統預設應用程式開啟檔案"""
    system = platform.system()
    try:
        if system == "Windows":
            os.startfile(filepath)
        elif system == "Darwin":  # macOS
            subprocess.run(["open", filepath])
        elif system == "Linux":
            subprocess.run(["xdg-open", filepath])
        else:
            print("不支援的作業系統")
            return False
        return True
    except Exception as e:
        print(f"開啟檔案失敗: {e}")
        return False

def open_google_drive_dialog():
    """開啟 Google Drive 檔案下載對話框"""
    try:
        # 創建對話框視窗
        dialog = tk.Toplevel()
        dialog.title("Google Drive 檔案連接器")
        dialog.geometry("700x500")
        dialog.grab_set()  # 設為模態視窗
        
        # 居中顯示
        dialog.update_idletasks()
        x = (dialog.winfo_screenwidth() // 2) - (700 // 2)
        y = (dialog.winfo_screenheight() // 2) - (500 // 2)
        dialog.geometry(f"700x500+{x}+{y}")
        
        # 主框架
        main_frame = tk.Frame(dialog)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # 標題
        title_label = tk.Label(main_frame, 
                              text="Google Drive 檔案連接器", 
                              font=("Arial", 18, "bold"))
        title_label.pack(pady=(0, 20))
        
        # 說明文字
        info_text = """請輸入 Google Drive 檔案連結：

支援的連結格式：
• https://drive.google.com/file/d/FILE_ID/view?usp=sharing
• https://drive.google.com/file/d/FILE_ID/view?usp=drive_link
• https://drive.google.com/open?id=FILE_ID

注意事項：
• 請確保檔案已設定為「任何人都可以檢視」
• 支援的檔案格式：Excel (.xlsx, .xls), CSV (.csv), JMP (.jmp)
• 檔案將會下載到專案的 temp/ 目錄"""
        
        info_label = tk.Label(main_frame, text=info_text, 
                             font=("Arial", 11), justify=tk.LEFT,
                             anchor="w")
        info_label.pack(fill="x", pady=(0, 20))
        
        # URL 輸入區域
        url_frame = tk.Frame(main_frame)
        url_frame.pack(fill="x", pady=(0, 10))
        
        url_label = tk.Label(url_frame, text="Google Drive 檔案連結:", 
                            font=("Arial", 12, "bold"))
        url_label.pack(anchor="w")
        
        url_entry = tk.Entry(url_frame, width=80, font=("Arial", 11))
        url_entry.pack(fill="x", pady=(5, 0))
        
        # 預填測試連結
        sample_url = ""
        url_entry.insert(0, sample_url)
        
        # 狀態顯示
        status_label = tk.Label(main_frame, text="準備就緒", font=("Arial", 11))
        status_label.pack(pady=(10, 0))
        
        # 下載位置顯示
        download_dir = os.path.join(os.getcwd(), 'temp')
        location_label = tk.Label(main_frame, 
                                 text=f"下載位置: {download_dir}",
                                 font=("Arial", 9), fg="gray")
        location_label.pack(pady=(5, 20))
        
        # 處理函數
        def process_download():
            url = url_entry.get().strip()
            if not url:
                messagebox.showerror("錯誤", "請輸入 Google Drive 檔案連結")
                return
            
            try:
                # 更新狀態
                status_label.config(text="🔄 正在下載檔案...", fg="blue")
                dialog.update()
                
                # 下載檔案
                downloaded_path = download_google_drive_file(url)
                
                # 更新狀態
                status_label.config(text="📂 檔案下載完成，正在開啟...", fg="green")
                dialog.update()
                
                # 開啟檔案
                if open_file_with_system(downloaded_path):
                    # 顯示成功訊息
                    rel_path = os.path.relpath(downloaded_path, os.getcwd())
                    success_msg = f"✅ Google Drive 檔案已成功下載並開啟！\n\n"
                    success_msg += f"檔案位置: {rel_path}\n"
                    success_msg += f"完整路徑: {downloaded_path}\n\n"
                    success_msg += "您現在可以在相應的應用程式中使用這個檔案。"
                    
                    messagebox.showinfo("成功", success_msg)
                    dialog.destroy()
                else:
                    status_label.config(text="❌ 檔案開啟失敗", fg="red")
                    messagebox.showwarning("警告", f"檔案下載成功但開啟失敗\n檔案位置: {downloaded_path}")
                
            except Exception as e:
                status_label.config(text="❌ 下載失敗", fg="red")
                error_msg = f"處理 Google Drive 檔案時發生錯誤:\n{str(e)}\n\n"
                error_msg += "常見解決方法:\n"
                error_msg += "• 確認檔案權限設定為「任何人都可以檢視」\n"
                error_msg += "• 檢查網路連線\n"
                error_msg += "• 確認已安裝 gdown 套件: pip install gdown"
                messagebox.showerror("錯誤", error_msg)
        
        # 按鈕區域
        button_frame = tk.Frame(main_frame)
        button_frame.pack(pady=(20, 0))
        
        # 下載按鈕
        download_btn = tk.Button(button_frame, text="下載並開啟檔案", 
                               command=process_download,
                               font=("Arial", 12, "bold"),
                               width=20)
        download_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        # 取消按鈕
        cancel_btn = tk.Button(button_frame, text="取消", 
                              command=dialog.destroy,
                              font=("Arial", 12),
                              width=10)
        cancel_btn.pack(side=tk.LEFT)
        
        # 設定焦點
        url_entry.focus()
        url_entry.select_range(0, tk.END)
        
    except Exception as e:
        messagebox.showerror("錯誤", f"開啟對話框失敗: {str(e)}")

if __name__ == "__main__":
    # 測試功能
    print("Google Drive 工具模組測試")
    
    # 創建簡單的測試視窗
    root = tk.Tk()
    root.withdraw()  # 隱藏主視窗
    
    open_google_drive_dialog()
    root.mainloop() 