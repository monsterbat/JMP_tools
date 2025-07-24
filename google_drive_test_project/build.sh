#!/bin/bash

# ===========================================
# Google Drive Test 專案建置腳本
# 版本：2.0 (2025-07-24)
# ===========================================

set -e  # 遇到錯誤立即停止

# 顏色定義
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 輔助函數
print_header() {
    echo -e "${BLUE}===========================================${NC}"
    echo -e "${BLUE}$1${NC}"
    echo -e "${BLUE}===========================================${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

# 檢查 Python 版本
check_python() {
    print_header "檢查 Python 環境"
    
    if ! command -v python3.12 &> /dev/null; then
        print_error "Python 3.12 未安裝，請先安裝 Python 3.12"
        exit 1
    fi
    
    PYTHON_VERSION=$(python3.12 --version)
    print_success "Python 版本: $PYTHON_VERSION"
}

# 檢查必要檔案
check_files() {
    print_header "檢查專案檔案"
    
    required_files=("main.py" "google_drive_utils.py" "requirements.txt" "google_drive_test_project.spec")
    
    for file in "${required_files[@]}"; do
        if [[ ! -f "$file" ]]; then
            print_error "找不到必要檔案: $file"
            exit 1
        else
            print_success "檔案存在: $file"
        fi
    done
}

# 安裝相依套件
install_dependencies() {
    print_header "安裝相依套件"
    
    print_info "使用 Python 3.12 安裝套件..."
    python3.12 -m pip install --upgrade pip
    python3.12 -m pip install -r requirements.txt
    
    print_success "套件安裝完成"
}

# 清理舊的建置檔案
clean_build() {
    print_header "清理舊的建置檔案"
    
    # 清理目錄
    dirs_to_clean=("build" "dist" "__pycache__" "*.egg-info")
    
    for dir in "${dirs_to_clean[@]}"; do
        if [[ -d "$dir" ]] || ls $dir 1> /dev/null 2>&1; then
            print_info "清理: $dir"
            rm -rf $dir
        fi
    done
    
    # 清理檔案
    files_to_clean=("*.pyc" "*.pyo" "*.spec~")
    
    for pattern in "${files_to_clean[@]}"; do
        if ls $pattern 1> /dev/null 2>&1; then
            print_info "清理: $pattern"
            rm -f $pattern
        fi
    done
    
    print_success "清理完成"
}

# 執行 PyInstaller
run_pyinstaller() {
    print_header "執行 PyInstaller 打包"
    
    print_info "開始打包程式..."
    python3.12 -m PyInstaller google_drive_test_project.spec --clean --noconfirm
    
    if [[ $? -eq 0 ]]; then
        print_success "打包完成！"
    else
        print_error "打包失敗"
        exit 1
    fi
}

# 檢查建置結果
check_build_result() {
    print_header "檢查建置結果"
    
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        app_path="dist/Google Drive Test.app"
        if [[ -d "$app_path" ]]; then
            print_success "macOS 應用程式包建立成功: $app_path"
            
            # 檢查執行檔
            exe_path="$app_path/Contents/MacOS/GoogleDriveTest"
            if [[ -f "$exe_path" ]]; then
                print_success "執行檔存在: $exe_path"
                
                # 檢查檔案大小
                size=$(du -h "$app_path" | cut -f1)
                print_info "應用程式大小: $size"
            else
                print_error "執行檔不存在: $exe_path"
                exit 1
            fi
        else
            print_error "應用程式包不存在: $app_path"
            exit 1
        fi
    else
        # Linux/Windows
        exe_path="dist/GoogleDriveTest"
        if [[ -f "$exe_path" ]]; then
            print_success "執行檔建立成功: $exe_path"
            
            # 檢查檔案大小
            size=$(du -h "$exe_path" | cut -f1)
            print_info "執行檔大小: $size"
        else
            print_error "執行檔不存在: $exe_path"
            exit 1
        fi
    fi
}

# 建立使用說明
create_usage_info() {
    print_header "建立使用說明"
    
    cat > dist/使用說明.txt << EOF
Google Drive Test 專案 - 使用說明
====================================

建置日期: $(date)
Python 版本: $(python3.12 --version)

檔案說明:
---------
$(if [[ "$OSTYPE" == "darwin"* ]]; then
    echo "• Google Drive Test.app - macOS 應用程式包"
    echo "• 雙擊即可執行"
else
    echo "• GoogleDriveTest - 執行檔"
    echo "• 在終端機中執行: ./GoogleDriveTest"
fi)

功能說明:
---------
• 公開檔案下載：支援 Google Drive 公開分享檔案
• 企業版存取：支援 OAuth 2.0 認證存取私人檔案
• 支援格式：CSV, Excel (.xlsx, .xls), JMP (.jmp)

首次使用企業版功能:
------------------
1. 需要準備 credentials.json 檔案 (從 Google Cloud Console 下載)
2. 將 credentials.json 放在執行檔同一目錄
3. 首次使用會開啟瀏覽器進行 Google 帳號認證
4. 認證成功後會自動生成 token.json

注意事項:
---------
• credentials.json 和 token.json 包含敏感資訊，請妥善保管
• 企業版功能需要網路連線
• 下載的檔案會儲存在 temp/ 目錄中

技術支援:
---------
如有問題請參考專案文件或聯繫開發團隊。

EOF
    
    print_success "使用說明已建立: dist/使用說明.txt"
}

# 主函數
main() {
    print_header "Google Drive Test 專案建置開始"
    
    # 檢查環境
    check_python
    check_files
    
    # 安裝相依套件
    install_dependencies
    
    # 清理舊檔案
    clean_build
    
    # 執行打包
    run_pyinstaller
    
    # 檢查結果
    check_build_result
    
    # 建立說明
    create_usage_info
    
    print_header "建置完成！"
    print_success "執行檔已建立在 dist/ 目錄中"
    
    if [[ "$OSTYPE" == "darwin"* ]]; then
        print_info "執行方式: 雙擊 'dist/Google Drive Test.app'"
    else
        print_info "執行方式: ./dist/GoogleDriveTest"
    fi
    
    print_warning "記得將 credentials.json 複製到 dist/ 目錄中才能使用企業版功能"
}

# 執行主函數
main "$@" 