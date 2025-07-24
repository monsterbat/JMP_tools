#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
企業版 Google Drive 功能測試腳本

用於測試企業版 Google Drive API 是否正常運作
"""

import os
from google_drive_utils import download_enterprise_google_drive_file

def test_enterprise_function():
    """測試企業版下載功能"""
    print("=== 企業版 Google Drive 功能測試 ===")
    print()
    
    # 檢查憑證檔案
    if not os.path.exists('credentials.json'):
        print("❌ 找不到 credentials.json 檔案")
        print("請確認檔案已正確放置在專案目錄中")
        return False
    
    print("✅ 找到 credentials.json 檔案")
    
    # 請使用者輸入測試連結
    print()
    print("請輸入您的 Google Drive 檔案連結進行測試：")
    print("(可以是您個人 Google Drive 中的任何檔案)")
    print()
    
    test_url = input("Google Drive 連結: ").strip()
    
    if not test_url:
        print("❌ 未輸入連結")
        return False
    
    print()
    print("🔐 開始測試企業版下載功能...")
    print("首次使用會開啟瀏覽器進行 OAuth 認證")
    print()
    
    try:
        # 測試下載
        downloaded_file = download_enterprise_google_drive_file(test_url)
        
        if downloaded_file and os.path.exists(downloaded_file):
            print(f"✅ 測試成功！")
            print(f"📁 檔案已下載到: {downloaded_file}")
            print()
            print("🎉 企業版 Google Drive 功能正常運作！")
            return True
        else:
            print("❌ 下載失敗：檔案不存在")
            return False
            
    except Exception as e:
        print(f"❌ 測試失敗: {str(e)}")
        print()
        print("📋 可能的原因：")
        print("1. 憑證設定問題")
        print("2. 網路連線問題")  
        print("3. 檔案權限問題")
        print("4. Google Drive API 配額限制")
        return False

if __name__ == "__main__":
    success = test_enterprise_function()
    
    print()
    if success:
        print("🎯 測試結論：企業版功能正常，可以正常使用！")
    else:
        print("🔧 測試結論：需要檢查設定或網路連線")
        print()
        print("🆘 如需協助，請檢查：")
        print("1. ENTERPRISE_SETUP.md 設定指南")
        print("2. Google Cloud Console 的 API 設定")
        print("3. 檔案權限和分享設定") 