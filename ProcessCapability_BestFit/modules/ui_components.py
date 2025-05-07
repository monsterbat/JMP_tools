import tkinter as tk
from tkinter import Label, Button, Text, StringVar, messagebox
from modules.path_helper import resource_path

def create_main_window():
    """建立主視窗"""
    root = tk.Tk()
    root.title("JMP Process Capability Report Generate (Best Fit) v1.0")
    root.geometry("800x660")
    return root

def create_file_selection_ui(root, jmp_file_path, on_select_file, on_open_analysis):
    """建立檔案選擇相關的UI元件"""
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
    """建立JSL解析器相關的UI元件"""
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