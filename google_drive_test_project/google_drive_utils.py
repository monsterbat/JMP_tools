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

def open_enterprise_google_drive_dialog():
    """開啟企業版 Google Drive 檔案連接器對話框"""
    
    def show_auth_info():
        """顯示認證設定說明"""
        info_text = """
🏢 企業版 Google Drive 存取設定說明

📋 需要設定步驟：
1. 前往 Google Cloud Console (https://console.cloud.google.com)
2. 建立新專案或選擇現有專案
3. 啟用 Google Drive API
4. 建立憑證 (OAuth 2.0 用戶端 ID)
5. 下載憑證檔案並命名為 'credentials.json'
6. 將檔案放置在此程式目錄中

⚠️  首次使用需要完成瀏覽器授權流程
✅ 授權完成後會自動儲存 token.json

📁 可存取檔案類型：
• 企業內部共享檔案
• 您擁有的私人檔案  
• 明確分享給您的檔案
        """
        messagebox.showinfo("企業版設定說明", info_text)
    
    def fetch_enterprise_file():
        """取得企業版檔案"""
        url = url_entry.get().strip()
        if not url:
            messagebox.showerror("錯誤", "請輸入 Google Drive 檔案連結")
            return
        
        try:
            status_label.config(text="🔄 正在透過 API 下載檔案...")
            dialog.update()
            
            # 使用企業版 API 下載
            file_path = download_enterprise_google_drive_file(url)
            
            if file_path:
                status_label.config(text="✅ 檔案下載成功！正在開啟...")
                dialog.update()
                
                # 開啟檔案
                open_file_with_system(file_path)
                
                status_label.config(text="🎉 檔案已成功開啟！")
                
                # 顯示成功訊息
                success_msg = f"""
✅ 企業版 Google Drive 檔案已成功開啟！

📁 檔案位置: {file_path}
🔐 透過企業認證存取

您現在可以使用這個檔案進行分析。
                """
                messagebox.showinfo("成功", success_msg)
            else:
                status_label.config(text="❌ 下載失敗")
                
        except Exception as e:
            error_msg = f"企業版存取失敗: {str(e)}"
            status_label.config(text="❌ " + error_msg)
            messagebox.showerror("錯誤", error_msg)
    
    # 創建對話框
    dialog = tk.Toplevel()
    dialog.title("企業版 Google Drive 檔案連接器")
    dialog.geometry("600x500")
    dialog.resizable(True, True)
    
    # 設定對話框居中
    dialog.update_idletasks()
    x = (dialog.winfo_screenwidth() // 2) - (600 // 2)
    y = (dialog.winfo_screenheight() // 2) - (500 // 2)
    dialog.geometry(f"600x500+{x}+{y}")
    
    # 主框架
    main_frame = tk.Frame(dialog)
    main_frame.pack(expand=True, fill="both", padx=20, pady=20)
    
    # 標題
    title_label = tk.Label(main_frame, 
                          text="🏢 企業版 Google Drive 存取", 
                          font=("Arial", 16, "bold"))
    title_label.pack(pady=(0, 20))
    
    # 說明文字
    info_text = """
    透過 Google Drive API 存取企業內部檔案
    支援：企業共享檔案、私人檔案、特定權限檔案
    """
    info_label = tk.Label(main_frame, text=info_text, font=("Arial", 10))
    info_label.pack(pady=(0, 20))
    
    # URL 輸入區域
    url_frame = tk.Frame(main_frame)
    url_frame.pack(fill="x", pady=(0, 20))
    
    tk.Label(url_frame, text="Google Drive 檔案連結:", font=("Arial", 11, "bold")).pack(anchor="w")
    url_entry = tk.Entry(url_frame, font=("Arial", 10), width=70)
    url_entry.pack(fill="x", pady=(5, 0))
    url_entry.insert(0, "https://drive.google.com/file/d/YOUR_FILE_ID/view")
    
    # 按鈕區域
    button_frame = tk.Frame(main_frame)
    button_frame.pack(fill="x", pady=20)
    
    # 設定說明按鈕
    setup_button = tk.Button(button_frame, 
                           text="📋 設定說明", 
                           font=("Arial", 10),
                           command=show_auth_info)
    setup_button.pack(side="left", padx=(0, 10))
    
    # 下載按鈕
    download_button = tk.Button(button_frame, 
                              text="🔐 透過 API 下載檔案", 
                              font=("Arial", 11, "bold"),
                              command=fetch_enterprise_file)
    download_button.pack(side="left", padx=10)
    
    # 關閉按鈕
    close_button = tk.Button(button_frame, 
                           text="關閉", 
                           font=("Arial", 10),
                           command=dialog.destroy)
    close_button.pack(side="right")
    
    # 狀態顯示
    status_label = tk.Label(main_frame, 
                           text="🔐 準備透過企業認證存取檔案", 
                           font=("Arial", 10), 
                           fg="blue")
    status_label.pack(pady=(20, 0))
    
    # 詳細資訊
    details_text = """
📌 企業版功能特色：
• 🏢 存取企業內部共享檔案
• 🔐 支援私人和受限檔案
• 👥 透過您的企業帳號認證
• 🛡️  符合企業安全政策

⚙️  技術說明：
• 使用 Google Drive API v3
• OAuth 2.0 企業認證流程
• 自動 Token 管理和更新
• 支援所有檔案格式
    """
    
    details_label = tk.Label(main_frame, 
                           text=details_text, 
                           font=("Arial", 9),
                           fg="gray",
                           justify="left")
    details_label.pack(pady=(20, 0), anchor="w")

def download_enterprise_google_drive_file(url, target_dir=None):
    """使用 Google Drive API 下載檔案（支援企業版和私人檔案）"""
    # 檢查是否已安裝必要套件
    try:
        from google.auth.transport.requests import Request
        from google.oauth2.credentials import Credentials
        from google_auth_oauthlib.flow import InstalledAppFlow
        from googleapiclient.discovery import build
        from googleapiclient.errors import HttpError
        import io
        from googleapiclient.http import MediaIoBaseDownload
    except ImportError as e:
        error_msg = """
❌ 缺少必要套件！

請安裝 Google Drive API 套件：
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib

然後重新啟動程式。
        """
        raise Exception(error_msg)
    
    try:
        
        # OAuth 2.0 權限範圍 - 修正為更完整的權限
        SCOPES = [
            'https://www.googleapis.com/auth/drive.readonly',
            'https://www.googleapis.com/auth/drive.file',
            'https://www.googleapis.com/auth/drive'
        ]
        
        # 憑證檔案路徑
        credentials_file = 'credentials.json'
        token_file = 'token.json'
        
        # 檢查憑證檔案
        if not os.path.exists(credentials_file):
            error_msg = """
❌ 找不到 credentials.json 檔案！

請按照以下步驟設定：
1. 前往 Google Cloud Console
2. 建立專案並啟用 Google Drive API  
3. 建立 OAuth 2.0 憑證
4. 下載 credentials.json 到程式目錄

詳細設定說明請點擊「📋 設定說明」按鈕。
            """
            raise Exception(error_msg)
        
        creds = None
        
        # 載入現有 token
        if os.path.exists(token_file):
            creds = Credentials.from_authorized_user_file(token_file, SCOPES)
        
        # 如果沒有有效認證，執行 OAuth 流程
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                print("🔄 正在更新認證 token...")
                creds.refresh(Request())
            else:
                print("🔐 啟動 OAuth 認證流程...")
                flow = InstalledAppFlow.from_client_secrets_file(credentials_file, SCOPES)
                creds = flow.run_local_server(port=0)
            
            # 儲存認證資訊
            with open(token_file, 'w') as token:
                token.write(creds.to_json())
            print("✅ 認證資訊已儲存")
        
        # 建立 Google Drive API 服務
        service = build('drive', 'v3', credentials=creds)
        
        # 提取檔案 ID
        file_id = extract_google_drive_file_id(url)
        if not file_id:
            raise Exception("無法從 URL 中提取檔案 ID")
        
        print(f"📁 正在存取檔案 ID: {file_id}")
        
        # 取得檔案資訊和權限檢查
        try:
            file_metadata = service.files().get(fileId=file_id, fields='id,name,size,owners,permissions,shared').execute()
            file_name = file_metadata.get('name', f"downloaded_file_{file_id}")
            file_size = file_metadata.get('size', 'Unknown')
            
            print(f"📄 檔案名稱: {file_name}")
            print(f"📊 檔案大小: {file_size} bytes" if file_size != 'Unknown' else "📊 檔案大小: Unknown")
            print(f"🔍 檔案 ID: {file_id}")
            
        except HttpError as metadata_error:
            if metadata_error.resp.status == 403:
                error_msg = f"""
❌ 權限錯誤 (檔案資訊存取被拒絕)

可能的原因：
1. 檔案權限設定問題
2. OAuth 權限範圍不足
3. 檔案不存在或已被刪除

建議解決方案：
1. 刪除 token.json 檔案重新認證
2. 確認檔案 ID 正確: {file_id}
3. 檢查 Google Cloud Console 的 OAuth 設定
                """
                raise Exception(error_msg)
            else:
                raise metadata_error
        
        # 設定下載目錄
        if target_dir is None:
            target_dir = os.path.join(os.getcwd(), 'temp')
        os.makedirs(target_dir, exist_ok=True)
        
        # 設定檔案路徑
        file_path = os.path.join(target_dir, file_name)
        
        # 下載檔案
        print("⬇️  正在下載檔案...")
        request = service.files().get_media(fileId=file_id)
        
        with open(file_path, 'wb') as file_handle:
            downloader = MediaIoBaseDownload(file_handle, request)
            done = False
            while done is False:
                status, done = downloader.next_chunk()
                if status:
                    progress = int(status.progress() * 100)
                    print(f"⬇️  下載進度: {progress}%")
        
        print(f"✅ 檔案下載完成: {file_path}")
        return file_path
        
    except HttpError as error:
        if error.resp.status == 403:
            error_msg = "❌ 存取被拒絕：您沒有權限存取此檔案"
        elif error.resp.status == 404:
            error_msg = "❌ 檔案不存在：請檢查檔案 ID 是否正確"
        else:
            error_msg = f"❌ Google Drive API 錯誤: {error}"
        raise Exception(error_msg)
        
    except Exception as e:
        raise Exception(f"企業版下載失敗: {str(e)}")

if __name__ == "__main__":
    # 測試功能
    print("Google Drive 工具模組測試")
    
    # 創建簡單的測試視窗
    root = tk.Tk()
    root.withdraw()  # 隱藏主視窗
    
    open_google_drive_dialog()
    root.mainloop() 