#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
重置 Google Drive API 認證腳本

用於清除現有的認證 token 並重新進行 OAuth 流程
"""

import os

def reset_authentication():
    """重置認證設定"""
    print("=== Google Drive API 認證重置工具 ===")
    print()
    
    # 檢查並刪除 token.json
    if os.path.exists('token.json'):
        try:
            os.remove('token.json')
            print("✅ 已刪除舊的 token.json 檔案")
        except Exception as e:
            print(f"❌ 刪除 token.json 失敗: {e}")
    else:
        print("ℹ️  沒有找到 token.json 檔案")
    
    # 檢查 credentials.json
    if os.path.exists('credentials.json'):
        print("✅ 找到 credentials.json 檔案")
    else:
        print("❌ 找不到 credentials.json 檔案")
        print("請確認已從 Google Cloud Console 下載憑證檔案")
        return False
    
    print()
    print("🔄 認證已重置！")
    print()
    print("📋 接下來的步驟：")
    print("1. 執行 python3.12 main.py")
    print("2. 點擊企業版按鈕")
    print("3. 輸入檔案連結")
    print("4. 系統會自動開啟瀏覽器進行重新認證")
    print("5. 使用您的 Google 帳號登入並授權")
    print()
    print("⚠️  重要提醒：")
    print("• 請使用擁有該檔案的 Google 帳號登入")
    print("• 確認授權所有請求的權限")
    print("• 如果是企業帳號，可能需要管理員批准")
    
    return True

if __name__ == "__main__":
    reset_authentication() 