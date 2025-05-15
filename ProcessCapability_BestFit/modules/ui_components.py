import tkinter as tk
from tkinter import Label, Button, Text, StringVar, messagebox
from modules.path_helper import resource_path
from modules.file_operations import open_duplicate_process, open_user_guide

# 常數定義
APP_VERSION = "V1.0"
APP_AUTHOR = "SC Hsiao"
APP_UPDATE_DATE = "2024/05/15"

def create_main_window():
    """Create the main window"""
    root = tk.Tk()
    root.title("JMP Process Capability Report Generate (Best Fit) v1.0")
    root.geometry("800x660")
    return root


def create_data_process_ui(root):
    """Create the Data Process block and four function buttons"""
    frame = tk.LabelFrame(root, bd=2, relief="groove", padx=10, pady=10)
    frame.pack(fill="x", padx=10, pady=10)

    # Center title
    title = tk.Label(frame, text="Data Process", font=("Arial", 18, "bold"), anchor="center", justify="center")
    title.pack(fill="x", pady=(0, 10))

    btn_frame = tk.Frame(frame)
    btn_frame.pack()

    Button(btn_frame, text="Combine Data", width=16, font=("Arial", 12), command=lambda: messagebox.showinfo("Notice", "Combine Data function is under development")).pack(side="left", padx=8)
    Button(btn_frame, text="Exclude Duplicate", width=16, font=("Arial", 12), command=open_duplicate_process).pack(side="left", padx=8)
    Button(btn_frame, text="Setup Spec", width=16, font=("Arial", 12), command=lambda: messagebox.showinfo("Notice", "Setup Spec function is under development")).pack(side="left", padx=8)
    Button(btn_frame, text="Exclude Outlier", width=16, font=("Arial", 12), command=lambda: messagebox.showinfo("Notice", "Exclude Outlier function is under development")).pack(side="left", padx=8) 

def create_process_capability_report_ui(root, jmp_file_path, on_select_file, on_open_analysis, on_extract):
    """建立Process Capability Report區塊，包含分析選擇、JSL輸入與提取按鈕"""
    frame = tk.LabelFrame(root, bd=2, relief="groove", padx=10, pady=10)
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    # 置中標題
    title = tk.Label(frame, text="Process Capability Report", font=("Arial", 18, "bold"), anchor="center", justify="center")
    title.pack(fill="x", pady=(0, 10))

    # Step 2 按鈕
    btn_open_analysis = Button(frame, text="Step 2: Select Analysis Items", font=("Arial", 12), command=on_open_analysis, width=30)
    btn_open_analysis.pack(pady=(0, 5))

    # JMP檔案路徑顯示
    lbl_jmp_path = Label(frame, textvariable=jmp_file_path, anchor="center", justify="center", font=("Arial", 11))
    lbl_jmp_path.pack(pady=(0, 5))

    # JSL輸入框
    Label(frame, text="Please paste JSL code:", font=("Arial", 11)).pack(anchor="center", pady=(5, 2))
    text_input = Text(frame, height=10, width=80, font=("Consolas", 12))
    text_input.pack(pady=(0, 10))

    # 提取按鈕
    btn_extract = Button(frame, text="Extract Process Variables Data", font=("Arial", 12), command=on_extract, width=30)
    btn_extract.pack(pady=(0, 5))

    return text_input

def create_app_info_ui(root):
    """創建應用程序信息區塊，包含版本、作者信息和使用說明按鈕"""
    # 創建信息框架
    frame = tk.Frame(root)
    frame.pack(fill="x", padx=10, pady=5)
    
    # 中央按鈕框架
    center_frame = tk.Frame(frame)
    center_frame.pack(anchor="center", pady=5)
    
    # 使用說明按鈕 (放在中間)
    help_btn = Button(center_frame, text="Instruction for use", command=open_user_guide, font=("Arial", 12), width=20)
    help_btn.pack(pady=5)
    
    # 版本與作者信息 (放在底部中央)
    info_text = f"Version: {APP_VERSION}        Author: {APP_AUTHOR}"
    version_label = Label(frame, text=info_text, font=("Arial", 10), anchor="center")
    version_label.pack(fill="x", pady=5)
    
    return frame

# 為了向後兼容保留下面兩個函數，但它們已被上面的函數取代，所以可以刪除
def create_file_selection_ui(root, jmp_file_path, on_select_file, on_open_analysis):
    """建立檔案選擇相關的UI元件 (已被create_process_capability_report_ui取代)"""
    # 建立一個框架來容納所有元件
    frame = tk.Frame(root)
    frame.pack(fill="both", expand=True, padx=10, pady=5)
    
    # JMP檔案選擇區域
    jmp_frame = tk.Frame(frame)
    jmp_frame.pack(fill="x", pady=(10, 20))
    
    btn_select_jmp = Button(jmp_frame, text="Step 1: Select JMP File", command=on_select_file, width=25)
    btn_select_jmp.pack(pady=(0, 2))
    
    lbl_jmp_path = Label(jmp_frame, textvariable=jmp_file_path, anchor="w", wraplength=500)
    lbl_jmp_path.pack(pady=(0, 2))
    
    # JMP檔案備註區域（程式撰寫者使用）
    jmp_note = Label(jmp_frame, text="Please select the JMP file to analyze", anchor="w", justify="left")
    jmp_note.pack(pady=(0, 0))
    
    # 分析項目選擇區域
    analysis_frame = tk.Frame(frame)
    analysis_frame.pack(fill="x", pady=(0, 2))
    
    btn_open_analysis = Button(analysis_frame, text="Step 2: Select Analysis Items", command=on_open_analysis, width=25)
    btn_open_analysis.pack(pady=(0, 2))
    
    # 分析項目備註區域（程式撰寫者使用）
    analysis_note = Label(analysis_frame, text=
                          """
1. When best_fit_distribution appears, click Run script button
2. Select items to process, choose Best Fit Distribution, click OK
3. Click the red triangle 🔻 at top left -> Save Script -> To Script Window
4. Select all code in Script window, Ctrl+A to select all then Ctrl+C to copy
5. Paste to the Script window below""", 
                          anchor="w", justify="left")
    analysis_note.pack(pady=(0, 0))

def create_jsl_parser_ui(root, on_extract):
    """建立JSL解析器相關的UI元件 (已被create_process_capability_report_ui取代)"""
    # 建立一個框架來容納所有元件
    frame = tk.Frame(root)
    frame.pack(fill="both", expand=True, padx=10, pady=5)
    
    # 輸入區域
    Label(frame, text="Please paste JSL code:").pack(anchor="w", pady=(0, 2))
    text_input = Text(frame, height=15, width=100)
    text_input.pack(pady=(0, 2))
    
    # 按鈕區域
    button_frame = tk.Frame(frame)
    button_frame.pack(pady=(0, 2))
    
    Button(button_frame, text="Extract Process Variables Data", command=on_extract).pack(side="left", padx=5)
    
    # 抽取 Process Variables 資料的說明，附在程式裡面
    process_variables_note = Label(frame, text=
                            """
1. Click Run Script button
2. Select save location
3. Generate Process Capability Report and save to specified location
""", anchor="w", justify="left")
    process_variables_note.pack(pady=(0, 0))
    
    # 新增文字，顯示文件創作者
    author_note = Label(frame, text="""
                        Version: 1.0
                        If you have any questions, please contact SC Hsiao
                        """, anchor="w", justify="left")
    author_note.pack(pady=(0, 0))
    
    return text_input 
