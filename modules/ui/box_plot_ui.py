import tkinter as tk
from tkinter import ttk, messagebox, StringVar
import os
from modules.utils.path_helper import resource_path
from modules.utils.version import get_app_title
from modules.core.file_operations import open_file, ask_and_open_file
from modules.utils.constants import (
    DEFAULT_WINDOW_WIDTH, DEFAULT_WINDOW_HEIGHT, DEFAULT_PADDING,
    DEFAULT_LISTBOX_WIDTH, DEFAULT_LISTBOX_HEIGHT, DEFAULT_ENTRY_WIDTH,
    TITLE_CHOOSE_ANALYSIS_DATA, LABEL_CHOOSE_ANALYSIS_ITEMS,
    LABEL_CHOOSE_X_GROUP_ITEM, LABEL_CHOOSE_X_AXIS_ITEM,
    LABEL_DISPLAY_OPTIONS, LABEL_SEARCH_ICON, RELIEF_GROOVE,
    DEFAULT_BORDER_WIDTH, BTN_GENERATE, MSG_TITLE_SUCCESS,
    MSG_TITLE_ERROR, MSG_TITLE_INFO
)

class BoxPlotUI:
    def __init__(self, master=None):
        """初始化Box Plot UI界面"""
        if master is None:
            # 如果沒有傳入主窗口，創建一個新窗口
            self.root = tk.Toplevel()
            self.root.title("Box Plot Tool - " + get_app_title())
            self.root.geometry(f"{DEFAULT_WINDOW_WIDTH}x{DEFAULT_WINDOW_HEIGHT}")
        else:
            self.root = master

        # 創建主要框架
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True, padx=DEFAULT_PADDING, pady=DEFAULT_PADDING)

        # 創建UI元素
        self._create_ui()

    def _create_ui(self):
        """創建所有UI元素"""
        # 創建標題
        title_label = tk.Label(
            self.main_frame, 
            text=TITLE_CHOOSE_ANALYSIS_DATA, 
            font=("Arial", 16, "bold")
        )
        title_label.pack(pady=(0, DEFAULT_PADDING))

        # 創建選擇區域框架
        selection_frame = tk.LabelFrame(
            self.main_frame, 
            text="", 
            bd=DEFAULT_BORDER_WIDTH,
            relief=RELIEF_GROOVE
        )
        selection_frame.pack(fill="x", padx=5, pady=5)

        # 創建三個區域的容器
        columns_frame = tk.Frame(selection_frame)
        columns_frame.pack(fill="x", padx=5, pady=5)

        # 設置三個列的權重
        columns_frame.columnconfigure(0, weight=1)
        columns_frame.columnconfigure(1, weight=1)
        columns_frame.columnconfigure(2, weight=1)

        # ===== 第一列：Analysis items =====
        analysis_frame = tk.LabelFrame(
            columns_frame,
            text=LABEL_CHOOSE_ANALYSIS_ITEMS,
            bd=DEFAULT_BORDER_WIDTH,
            relief=RELIEF_GROOVE
        )
        analysis_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        # 搜索框
        y_search_frame = tk.Frame(analysis_frame)
        y_search_frame.pack(fill="x", padx=5, pady=5)

        self.y_search_var = StringVar()
        y_search_entry = tk.Entry(
            y_search_frame, 
            textvariable=self.y_search_var,
            width=DEFAULT_ENTRY_WIDTH
        )
        y_search_entry.pack(side="left", fill="x", expand=True)
        
        y_search_button = tk.Button(
            y_search_frame, 
            text=LABEL_SEARCH_ICON, 
            command=lambda: self._filter_listbox(self.y_search_var, self.y_listbox)
        )
        y_search_button.pack(side="right")

        # 列表框
        y_listbox_frame = tk.Frame(analysis_frame)
        y_listbox_frame.pack(fill="both", expand=True, padx=5, pady=5)

        self.y_listbox = tk.Listbox(
            y_listbox_frame, 
            selectmode="multiple", 
            width=DEFAULT_LISTBOX_WIDTH, 
            height=DEFAULT_LISTBOX_HEIGHT
        )
        self.y_listbox.pack(side="left", fill="both", expand=True)

        y_scrollbar = tk.Scrollbar(y_listbox_frame, orient="vertical")
        y_scrollbar.pack(side="right", fill="y")
        self.y_listbox.config(yscrollcommand=y_scrollbar.set)
        y_scrollbar.config(command=self.y_listbox.yview)

        # ===== 第二列：X Group item =====
        x_group_frame = tk.LabelFrame(
            columns_frame,
            text=LABEL_CHOOSE_X_GROUP_ITEM,
            bd=DEFAULT_BORDER_WIDTH,
            relief=RELIEF_GROOVE
        )
        x_group_frame.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

        # 搜索框
        x_group_search_frame = tk.Frame(x_group_frame)
        x_group_search_frame.pack(fill="x", padx=5, pady=5)

        self.x_group_search_var = StringVar()
        x_group_search_entry = tk.Entry(
            x_group_search_frame, 
            textvariable=self.x_group_search_var,
            width=DEFAULT_ENTRY_WIDTH
        )
        x_group_search_entry.pack(side="left", fill="x", expand=True)
        
        x_group_search_button = tk.Button(
            x_group_search_frame, 
            text=LABEL_SEARCH_ICON, 
            command=lambda: self._filter_listbox(self.x_group_search_var, self.x_group_listbox)
        )
        x_group_search_button.pack(side="right")

        # 列表框
        x_group_listbox_frame = tk.Frame(x_group_frame)
        x_group_listbox_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        self.x_group_listbox = tk.Listbox(
            x_group_listbox_frame, 
            selectmode="single", 
            width=DEFAULT_LISTBOX_WIDTH, 
            height=DEFAULT_LISTBOX_HEIGHT
        )
        self.x_group_listbox.pack(side="left", fill="both", expand=True)

        x_group_scrollbar = tk.Scrollbar(x_group_listbox_frame, orient="vertical")
        x_group_scrollbar.pack(side="right", fill="y")
        self.x_group_listbox.config(yscrollcommand=x_group_scrollbar.set)
        x_group_scrollbar.config(command=self.x_group_listbox.yview)

        # ===== 第三列：X axis item =====
        x_axis_frame = tk.LabelFrame(
            columns_frame,
            text=LABEL_CHOOSE_X_AXIS_ITEM,
            bd=DEFAULT_BORDER_WIDTH,
            relief=RELIEF_GROOVE
        )
        x_axis_frame.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")

        # 搜索框
        x_axis_search_frame = tk.Frame(x_axis_frame)
        x_axis_search_frame.pack(fill="x", padx=5, pady=5)

        self.x_axis_search_var = StringVar()
        x_axis_search_entry = tk.Entry(
            x_axis_search_frame, 
            textvariable=self.x_axis_search_var,
            width=DEFAULT_ENTRY_WIDTH
        )
        x_axis_search_entry.pack(side="left", fill="x", expand=True)
        
        x_axis_search_button = tk.Button(
            x_axis_search_frame, 
            text=LABEL_SEARCH_ICON, 
            command=lambda: self._filter_listbox(self.x_axis_search_var, self.x_axis_listbox)
        )
        x_axis_search_button.pack(side="right")

        # 列表框
        x_axis_listbox_frame = tk.Frame(x_axis_frame)
        x_axis_listbox_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        self.x_axis_listbox = tk.Listbox(
            x_axis_listbox_frame, 
            selectmode="single", 
            width=DEFAULT_LISTBOX_WIDTH, 
            height=DEFAULT_LISTBOX_HEIGHT
        )
        self.x_axis_listbox.pack(side="left", fill="both", expand=True)

        x_axis_scrollbar = tk.Scrollbar(x_axis_listbox_frame, orient="vertical")
        x_axis_scrollbar.pack(side="right", fill="y")
        self.x_axis_listbox.config(yscrollcommand=x_axis_scrollbar.set)
        x_axis_scrollbar.config(command=self.x_axis_listbox.yview)

        # 創建Display Options區域
        options_frame = tk.LabelFrame(
            self.main_frame, 
            text=LABEL_DISPLAY_OPTIONS, 
            bd=DEFAULT_BORDER_WIDTH,
            relief=RELIEF_GROOVE
        )
        options_frame.pack(fill="x", padx=5, pady=10)

        # 創建左右兩邊的選項
        left_options_frame = tk.Frame(options_frame)
        left_options_frame.pack(side="left", padx=20, pady=10)

        # 圖形類型選項
        plot_type_frame = tk.Frame(left_options_frame)
        plot_type_frame.pack(anchor="w", pady=2)
        tk.Label(plot_type_frame, text="Plot Type:").pack(side="left")
        
        self.plot_type_var = StringVar(value="Box Plot")
        plot_types = ["Box Plot", "Violin Plot"]
        self.plot_type_combo = ttk.Combobox(
            plot_type_frame, 
            textvariable=self.plot_type_var,
            values=plot_types,
            width=15,
            state="readonly"
        )
        self.plot_type_combo.pack(side="left", padx=5)

        # 右邊的選項框架
        right_options_frame = tk.Frame(options_frame)
        right_options_frame.pack(side="right", padx=20, pady=10)

        # 顯示Confidence Int
        self.show_confidence_var = tk.BooleanVar(value=True)
        tk.Checkbutton(
            right_options_frame, 
            text="Show Confidence Int", 
            variable=self.show_confidence_var
        ).pack(anchor="w")

        # 顯示Outliers
        self.show_outliers_var = tk.BooleanVar(value=True)
        tk.Checkbutton(
            right_options_frame, 
            text="Show Outliers", 
            variable=self.show_outliers_var
        ).pack(anchor="w")

        # 顯示Jitter
        self.show_jitter_var = tk.BooleanVar(value=False)
        tk.Checkbutton(
            right_options_frame, 
            text="Show Jitter", 
            variable=self.show_jitter_var
        ).pack(anchor="w")

        # 創建File Selection區域
        file_frame = tk.LabelFrame(
            self.main_frame, 
            text="File Selection", 
            bd=2,
            relief="groove"
        )
        file_frame.pack(fill="x", padx=5, pady=5)

        file_buttons_frame = tk.Frame(file_frame)
        file_buttons_frame.pack(fill="x", padx=5, pady=10)

        # 設置JMP檔案按鈕
        self.select_jmp_button = tk.Button(
            file_buttons_frame, 
            text="Select JMP File", 
            command=self._select_jmp_file,
            width=15,
            font=("Arial", 11)
        )
        self.select_jmp_button.pack(side="left", padx=10)

        # 加載測試數據
        self.load_demo_button = tk.Button(
            file_buttons_frame, 
            text="Load Demo Data", 
            command=self._load_demo_data,
            width=15,
            font=("Arial", 11)
        )
        self.load_demo_button.pack(side="left", padx=10)

        # 檔案路徑顯示
        self.file_path_var = StringVar()
        self.file_path_label = tk.Label(
            file_frame, 
            textvariable=self.file_path_var,
            anchor="w",
            wraplength=650
        )
        self.file_path_label.pack(fill="x", padx=10, pady=5)

        # 創建底部按鈕區域
        button_frame = tk.Frame(self.main_frame)
        button_frame.pack(pady=10)

        # 生成圖表按鈕
        self.generate_button = tk.Button(
            button_frame, 
            text="Generate Box Plot", 
            command=self._generate_box_plot,
            width=20,
            font=("Arial", 12, "bold")
        )
        self.generate_button.pack(pady=5)
        
        # 創建狀態欄
        status_frame = tk.Frame(self.main_frame)
        status_frame.pack(fill="x", side="bottom")
        
        self.status_var = StringVar(value="Ready")
        status_label = tk.Label(
            status_frame, 
            textvariable=self.status_var, 
            bd=1, 
            relief="sunken", 
            anchor="w"
        )
        status_label.pack(fill="x")

    def _load_demo_data(self):
        """載入示範資料"""
        # 清空所有列表
        self.y_listbox.delete(0, tk.END)
        self.x_group_listbox.delete(0, tk.END)
        self.x_axis_listbox.delete(0, tk.END)
        
        # 加入示範資料
        for item in ["Height", "Weight", "BMI", "Age", "Blood Pressure", "Cholesterol"]:
            self.y_listbox.insert(tk.END, item)
            
        for item in ["Gender", "Region", "Age Group", "Smoking Status"]:
            self.x_group_listbox.insert(tk.END, item)
            self.x_axis_listbox.insert(tk.END, item)
            
        self.file_path_var.set("Demo data loaded")
        self.status_var.set("Demo data loaded successfully")

    def _filter_listbox(self, search_var, listbox):
        """根據搜索條件過濾列表框項目"""
        search_text = search_var.get().lower()
        items = listbox.get(0, tk.END)
        
        listbox.delete(0, tk.END)
        
        for item in items:
            if search_text in item.lower():
                listbox.insert(tk.END, item)

    def _select_jmp_file(self):
        """選擇JMP檔案"""
        filepath = ask_and_open_file()
        if filepath:
            self.file_path_var.set(filepath)
            self.status_var.set(f"JMP file loaded: {os.path.basename(filepath)}")
            
            # TODO: 這裡可以新增讀取JMP檔案並填充列表框的代碼
            # 暫時使用測試數據
            self._load_demo_data()

    def _generate_box_plot(self):
        """生成Box Plot圖表"""
        # 獲取選擇的Y項目（可多選）
        y_indices = self.y_listbox.curselection()
        if not y_indices:
            messagebox.showwarning(MSG_TITLE_INFO, "Please select at least one Analysis item")
            return
            
        y_items = [self.y_listbox.get(idx) for idx in y_indices]
        
        # 獲取選擇的X Group項目（單選）
        x_group_index = self.x_group_listbox.curselection()
        if not x_group_index:
            messagebox.showwarning(MSG_TITLE_INFO, "Please select one X Group item")
            return
            
        x_group = self.x_group_listbox.get(x_group_index[0])
        
        # 獲取選擇的X Axis項目（單選）
        x_axis_index = self.x_axis_listbox.curselection()
        if not x_axis_index:
            messagebox.showwarning(MSG_TITLE_INFO, "Please select one X axis item")
            return
            
        x_axis = self.x_axis_listbox.get(x_axis_index[0])
        
        # 獲取其他選項
        plot_type = self.plot_type_var.get()
        show_confidence = self.show_confidence_var.get()
        show_outliers = self.show_outliers_var.get()
        show_jitter = self.show_jitter_var.get()
        
        # 生成JSL並運行
        self._generate_and_run_jsl(
            y_items, 
            x_group, 
            x_axis, 
            plot_type, 
            show_confidence, 
            show_outliers, 
            show_jitter
        )
        
    def _generate_and_run_jsl(self, y_items, x_group, x_axis, plot_type, show_confidence, show_outliers, show_jitter):
        """生成JSL代碼並運行"""
        # 這裡生成JSL代碼並儲存到檔案
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        jsl_path = os.path.join(desktop_path, "box_plot_generated.jsl")

        # 生成JSL代碼
        jsl_code = """
// Box Plot生成器 - 自動生成的JSL代碼
// Generated by Data Analysis Tools

// 打開數據表
dt = Current Data Table();
If( !IsDefined( dt ), 
    dt = Open( "$FILE_PATH$" )
);

// 檢查是否成功打開數據表
If( !IsDefined( dt ),
    ::ThrowError( "無法打開數據表，請先確保已經在JMP中打開了一個數據表。" )
);

// 創建Box Plot
"""

        # 根據不同的plot_type添加不同的代碼
        if plot_type == "Box Plot":
            jsl_code += "bp = dt << Box Plot(\n"
        else:
            jsl_code += "bp = dt << Violin Plot(\n"
        
        # Y項目處理
        y_vars_str = ", ".join([f'"{item}"' for item in y_items])
        jsl_code += f"    Y( {y_vars_str} ),\n"
        
        # X項目處理
        jsl_code += f'    X( "{x_axis}" ),\n'
        jsl_code += f'    Group By( "{x_group}" ),\n'
        
        # 選項設置
        if show_confidence:
            jsl_code += "    Show Box CI( 1 ),\n"
        else:
            jsl_code += "    Show Box CI( 0 ),\n"
            
        if show_outliers:
            jsl_code += "    Points Outliers( 1 ),\n"
        else:
            jsl_code += "    Points Outliers( 0 ),\n"
            
        if show_jitter:
            jsl_code += "    Points Jitter( 1 ),\n"
        else:
            jsl_code += "    Points Jitter( 0 ),\n"
        
        # 結束Box Plot定義
        jsl_code += ");\n\n"
        
        # 新增儲存圖像的代碼
        jsl_code += """
// 獲取當前時間作為檔案名的一部分
timestamp = Format( Today(), "mmddyyyy" ) || "_" || Format( Hour( Now() ), "00" ) || Format( Minute( Now() ), "00" );

// 儲存為PNG檔案
save_path = "~/Desktop/BoxPlot_" || timestamp || ".png";
bp << Save Picture( save_path, PNG );

// 顯示完成訊息
New Window( "Box Plot Created",
    V List Box(
        Text Box( "Box Plot has been created and saved to desktop." ),
        Text Box( "File: BoxPlot_" || timestamp || ".png" ),
        Button Box( "OK", New Window( "Box Plot Details",
            bp << Report
        ))
    )
);
"""

        # 儲存JSL檔案
        try:
            with open(jsl_path, "w", encoding="utf-8") as f:
                f.write(jsl_code)
                
            # 更新狀態
            self.status_var.set(f"JSL script generated and saved to desktop")
            
            # 打開JSL檔案
            open_file(jsl_path)
            
            # 顯示成功訊息
            messagebox.showinfo(
                MSG_TITLE_SUCCESS, 
                "JSL script has been generated and opened.\n\n"
                "Click Run Script in JMP to generate the Box Plot."
            )
                
        except Exception as e:
            messagebox.showerror(MSG_TITLE_ERROR, f"Error saving JSL file: {str(e)}")
            self.status_var.set("Error generating JSL script")

def open_box_plot_ui():
    """打開Box Plot UI界面"""
    # 創建一個新的Toplevel窗口
    root = tk.Toplevel()
    root.title("Box Plot Tool - " + get_app_title())
    root.geometry(f"{DEFAULT_WINDOW_WIDTH}x750")
    
    # 創建Box Plot UI
    app = BoxPlotUI(root)
    
    return app 