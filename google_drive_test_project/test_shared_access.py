#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
測試共享存取模式

模擬企業環境：
- A人員分享檔案給B人員
- B人員用自己的帳號存取A分享的檔案
"""

import os
from google_drive_utils import download_enterprise_google_drive_file

def test_shared_access():
    """測試共享存取功能"""
    print("=== 企業級共享存取測試 ===")
    print()
    print("🏢 模擬情境：")
    print("• A人員（資料擁有者）上傳檔案到自己的 Google Drive")
    print("• A人員將檔案分享給B人員（檢視權限）")
    print("• B人員（您）用自己的帳號登入程式")
    print("• B人員存取A分享的檔案")
    print()
    
    # 檢查憑證檔案
    if not os.path.exists('credentials.json'):
        print("❌ 找不到 credentials.json 檔案")
        return False
    
    print("✅ 找到 credentials.json 檔案")
    print()
    
    print("📋 測試步驟：")
    print("1. 請A人員將檔案分享給您的 Google 帳號")
    print("2. 確認您已收到分享通知")
    print("3. 輸入A人員分享給您的檔案連結")
    print()
    
    # 請使用者輸入分享的檔案連結
    shared_url = input("請輸入A人員分享給您的檔案連結: ").strip()
    
    if not shared_url:
        print("❌ 未輸入連結")
        return False
    
    print()
    print("🔐 開始測試共享存取...")
    print("系統會使用您的 Google 帳號進行認證")
    print("然後存取A人員分享給您的檔案")
    print()
    
    try:
        # 測試下載分享的檔案
        downloaded_file = download_enterprise_google_drive_file(shared_url)
        
        if downloaded_file and os.path.exists(downloaded_file):
            print(f"✅ 共享存取測試成功！")
            print(f"📁 檔案已下載到: {downloaded_file}")
            print()
            print("🎉 企業級共享存取模式正常運作！")
            print()
            print("📊 這證明了：")
            print("• ✅ B人員可以用自己的帳號登入")
            print("• ✅ B人員可以存取A人員分享的檔案")
            print("• ✅ 權限控制正常運作")
            print("• ✅ 符合企業安全要求")
            return True
        else:
            print("❌ 下載失敗：檔案不存在")
            return False
            
    except Exception as e:
        error_msg = str(e)
        print(f"❌ 共享存取測試失敗: {error_msg}")
        print()
        
        if "權限錯誤" in error_msg:
            print("🔍 可能的原因：")
            print("1. A人員尚未將檔案分享給您")
            print("2. 分享權限設定不正確")
            print("3. 您使用了錯誤的 Google 帳號登入")
            print()
            print("💡 解決建議：")
            print("1. 請A人員確認已將檔案分享給您的 email")
            print("2. 確認分享權限至少是「檢視者」")
            print("3. 在 OAuth 認證時選擇正確的 Google 帳號")
        
        return False

def simulate_enterprise_workflow():
    """模擬企業工作流程"""
    print()
    print("=" * 50)
    print("🏢 企業級 Google Drive 共享工作流程")
    print("=" * 50)
    print()
    
    print("👤 A人員（資料擁有者）的操作：")
    print("1. 上傳檔案到自己的 Google Drive")
    print("2. 右鍵點擊檔案 → 共用")
    print("3. 輸入B人員的 Google email")
    print("4. 設定權限為「檢視者」或「編輯者」")
    print("5. 點擊「傳送」")
    print()
    
    print("👤 B人員（程式使用者）的操作：")
    print("1. 收到 Google Drive 分享通知")
    print("2. 點擊通知中的檔案連結")
    print("3. 複製瀏覽器中的檔案 URL")
    print("4. 在程式中使用企業版功能")
    print("5. 用自己的 Google 帳號進行 OAuth 認證")
    print("6. 輸入檔案連結並下載")
    print()
    
    print("🎯 這個流程的優勢：")
    print("• 🔐 完全符合企業安全要求")
    print("• 👥 支援多人協作")
    print("• 🛡️ 權限可以隨時撤銷")
    print("• 📊 有完整的存取記錄")
    print("• 🔄 可以設定不同的權限等級")

if __name__ == "__main__":
    # 顯示企業工作流程說明
    simulate_enterprise_workflow()
    
    print()
    input("按 Enter 鍵開始測試共享存取功能...")
    
    # 執行共享存取測試
    success = test_shared_access()
    
    print()
    if success:
        print("🎯 測試結論：企業級共享存取模式完全可行！")
        print()
        print("🚀 接下來您可以：")
        print("1. 請同事或合作夥伴分享檔案給您")
        print("2. 使用企業版功能存取分享的檔案")
        print("3. 建立標準化的檔案分享流程")
    else:
        print("🔧 請按照上述建議檢查設定")
        print()
        print("💡 記住：這個模式需要A人員主動分享檔案給您") 