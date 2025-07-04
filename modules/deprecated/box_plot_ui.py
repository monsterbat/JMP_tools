import tkinter as tk
from tkinter import ttk, messagebox, StringVar
import os
from modules.utils.path_helper import resource_path
from modules.deprecated.file_operations import open_file, ask_and_open_file

class BoxPlotUI:
    def __init__(self, master=None):
        """初始化Box Plot UI界面"""
        if master is None:
            # 如果沒有傳入主窗口，創建一個新窗口
            self.root = tk.Toplevel()
            self.root.title("Box Plot Tool")
            self.root.geometry("700x500")
        else:
            self.root = master

        # 創建主要框架
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # 創建UI元素
        self._create_ui()

    def _create_ui(self):
        """創建所有UI元素"""
        # 創建標題
        title_label = tk.Label(
            self.main_frame, 
            text="Choose Analysis Data", 
            font=("Arial", 16, "bold")
        )
        title_label.pack(pady=(0, 10))

        # 創建選擇區域框架
        selection_frame = tk.LabelFrame(
            self.main_frame, 
            text="", 
            bd=2,
            relief="groove"
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
            text="Choose Analysis items",
            bd=2,
            relief="groove"
        )
        analysis_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        # 搜索框
        y_search_frame = tk.Frame(analysis_frame)
        y_search_frame.pack(fill="x", padx=5, pady=5)

        self.y_search_var = StringVar()
        y_search_entry = tk.Entry(
            y_search_frame, 
            textvariable=self.y_search_var,
            width=20
        )
        y_search_entry.pack(side="left", fill="x", expand=True)
        
        y_search_button = tk.Button(
            y_search_frame, 
            text="🔍", 
            command=lambda: self._filter_listbox(self.y_search_var, self.y_listbox)
        )
        y_search_button.pack(side="right")

        # 列表框
        y_listbox_frame = tk.Frame(analysis_frame)
        y_listbox_frame.pack(fill="both", expand=True, padx=5, pady=5)

        self.y_listbox = tk.Listbox(
            y_listbox_frame, 
            selectmode="multiple", 
            width=25, 
            height=10
        )
        self.y_listbox.pack(side="left", fill="both", expand=True)

        y_scrollbar = tk.Scrollbar(y_listbox_frame, orient="vertical")
        y_scrollbar.pack(side="right", fill="y")
        self.y_listbox.config(yscrollcommand=y_scrollbar.set)
        y_scrollbar.config(command=self.y_listbox.yview)

        # ===== 第二列：X Group item =====
        x_group_frame = tk.LabelFrame(
            columns_frame,
            text="Choose X Group item",
            bd=2,
            relief="groove"
        )
        x_group_frame.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

        # 搜索框
        x_group_search_frame = tk.Frame(x_group_frame)
        x_group_search_frame.pack(fill="x", padx=5, pady=5)

        self.x_group_search_var = StringVar()
        x_group_search_entry = tk.Entry(
            x_group_search_frame, 
            textvariable=self.x_group_search_var,
            width=20
        )
        x_group_search_entry.pack(side="left", fill="x", expand=True)
        
        x_group_search_button = tk.Button(
            x_group_search_frame, 
            text="🔍", 
            command=lambda: self._filter_listbox(self.x_group_search_var, self.x_group_listbox)
        )
        x_group_search_button.pack(side="right")

        # 列表框
        x_group_listbox_frame = tk.Frame(x_group_frame)
        x_group_listbox_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        self.x_group_listbox = tk.Listbox(
            x_group_listbox_frame, 
            selectmode="single", 
            width=25, 
            height=10
        )
        self.x_group_listbox.pack(side="left", fill="both", expand=True)

        x_group_scrollbar = tk.Scrollbar(x_group_listbox_frame, orient="vertical")
        x_group_scrollbar.pack(side="right", fill="y")
        self.x_group_listbox.config(yscrollcommand=x_group_scrollbar.set)
        x_group_scrollbar.config(command=self.x_group_listbox.yview)

        # ===== 第三列：X axis item =====
        x_axis_frame = tk.LabelFrame(
            columns_frame,
            text="Choose X axis item",
            bd=2,
            relief="groove"
        )
        x_axis_frame.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")

        # 搜索框
        x_axis_search_frame = tk.Frame(x_axis_frame)
        x_axis_search_frame.pack(fill="x", padx=5, pady=5)

        self.x_axis_search_var = StringVar()
        x_axis_search_entry = tk.Entry(
            x_axis_search_frame, 
            textvariable=self.x_axis_search_var,
            width=20
        )
        x_axis_search_entry.pack(side="left", fill="x", expand=True)
        
        x_axis_search_button = tk.Button(
            x_axis_search_frame, 
            text="🔍", 
            command=lambda: self._filter_listbox(self.x_axis_search_var, self.x_axis_listbox)
        )
        x_axis_search_button.pack(side="right")

        # 列表框
        x_axis_listbox_frame = tk.Frame(x_axis_frame)
        x_axis_listbox_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        self.x_axis_listbox = tk.Listbox(
            x_axis_listbox_frame, 
            selectmode="single", 
            width=25, 
            height=10
        )
        self.x_axis_listbox.pack(side="left", fill="both", expand=True)

        x_axis_scrollbar = tk.Scrollbar(x_axis_listbox_frame, orient="vertical")
        x_axis_scrollbar.pack(side="right", fill="y")
        self.x_axis_listbox.config(yscrollcommand=x_axis_scrollbar.set)
        x_axis_scrollbar.config(command=self.x_axis_listbox.yview)

        # 創建Display Options區域
        options_frame = tk.LabelFrame(
            self.main_frame, 
            text="Display Options", 
            bd=2,
            relief="groove"
        )
        options_frame.pack(fill="x", padx=5, pady=10)

        # 創建左右兩邊的選項
        left_options_frame = tk.Frame(options_frame)
        left_options_frame.pack(side="left", padx=20, pady=10)

        right_options_frame = tk.Frame(options_frame)
        right_options_frame.pack(side="right", padx=20, pady=10)

        # 左側選項 - Choose type
        type_label = tk.Label(
            left_options_frame, 
            text="Choose type", 
            font=("Arial", 10)
        )
        type_label.pack(anchor="w")

        self.plot_type = StringVar(value="contour")
        contour_radio = tk.Radiobutton(
            left_options_frame, 
            text="Contour", 
            variable=self.plot_type, 
            value="contour"
        )
        contour_radio.pack(anchor="w")

        dot_radio = tk.Radiobutton(
            left_options_frame, 
            text="Dot", 
            variable=self.plot_type, 
            value="dot"
        )
        dot_radio.pack(anchor="w")

        # 右側選項 - Show type
        show_label = tk.Label(
            right_options_frame, 
            text="Show type", 
            font=("Arial", 10)
        )
        show_label.pack(anchor="w")

        self.show_confidence = tk.BooleanVar(value=True)
        confidence_check = tk.Checkbutton(
            right_options_frame, 
            text="Show Confidence Diamond", 
            variable=self.show_confidence
        )
        confidence_check.pack(anchor="w")

        self.show_outliers = tk.BooleanVar(value=False)
        outliers_check = tk.Checkbutton(
            right_options_frame, 
            text="Show Outliers", 
            variable=self.show_outliers
        )
        outliers_check.pack(anchor="w")

        self.show_jitter = tk.BooleanVar(value=False)
        jitter_check = tk.Checkbutton(
            right_options_frame, 
            text="Show Jitter", 
            variable=self.show_jitter
        )
        jitter_check.pack(anchor="w")

        # 創建生成按鈕
        generate_frame = tk.Frame(self.main_frame)
        generate_frame.pack(pady=15)

        generate_button = tk.Button(
            generate_frame, 
            text="Generate Box Plot", 
            font=("Arial", 11),
            width=25, 
            height=1,
            command=self._generate_box_plot
        )
        generate_button.pack()

        # 初始化加載數據
        self._load_demo_data()

    def _load_demo_data(self):
        """加載示例數據到列表框"""
        demo_analysis_items = ["A001", "A002", "A003", "A004", "A005", "A006", "A007"]
        demo_x_group_items = ["B001", "B002", "B003", "B004", "B005", "B006", "B007"]
        demo_x_axis_items = ["A001", "A002", "A003", "A004", "A005", "A006", "A007"]

        for item in demo_analysis_items:
            self.y_listbox.insert(tk.END, item)

        for item in demo_x_group_items:
            self.x_group_listbox.insert(tk.END, item)

        for item in demo_x_axis_items:
            self.x_axis_listbox.insert(tk.END, item)

    def _filter_listbox(self, search_var, listbox):
        """根據搜索條件過濾列表框中的項目"""
        search_term = search_var.get().lower()
        listbox.delete(0, tk.END)

        # 這裡應該是從實際數據源獲取，暫時使用示例數據
        all_items = ["A001", "A002", "A003", "A004", "A005", "A006", "A007"]
        
        for item in all_items:
            if search_term in item.lower():
                listbox.insert(tk.END, item)

    def _generate_box_plot(self):
        """生成Box Plot圖"""
        # 獲取選擇的項目
        selected_y_indices = self.y_listbox.curselection()
        if not selected_y_indices:
            messagebox.showwarning("警告", "請至少選擇一個分析項目")
            return

        selected_y_items = [self.y_listbox.get(idx) for idx in selected_y_indices]
        
        # 獲取X Group項目
        selected_x_group_indices = self.x_group_listbox.curselection()
        selected_x_group = self.x_group_listbox.get(selected_x_group_indices[0]) if selected_x_group_indices else None
        
        # 獲取X Axis項目
        selected_x_axis_indices = self.x_axis_listbox.curselection()
        selected_x_axis = self.x_axis_listbox.get(selected_x_axis_indices[0]) if selected_x_axis_indices else None
        
        # 獲取顯示選項
        plot_type = self.plot_type.get()
        show_confidence = self.show_confidence.get()
        show_outliers = self.show_outliers.get()
        show_jitter = self.show_jitter.get()
        
        # 實際生成Box Plot的代碼
        # 這裡調用JMP腳本生成圖表
        messagebox.showinfo("成功", f"已生成Box Plot\n\n選擇的Y項目: {', '.join(selected_y_items)}\nX Group: {selected_x_group}\nX Axis: {selected_x_axis}")
        
        # 生成JSL腳本並執行
        self._generate_and_run_jsl(selected_y_items, selected_x_group, selected_x_axis, plot_type, show_confidence, show_outliers, show_jitter)

    def _generate_and_run_jsl(self, y_items, x_group, x_axis, plot_type, show_confidence, show_outliers, show_jitter):
        """生成JSL腳本並運行"""
        # 創建臨時JSL腳本
        jsl_path = resource_path("temp/box_plot_temp.jsl")
        os.makedirs(os.path.dirname(jsl_path), exist_ok=True)
        
        with open(jsl_path, 'w') as f:
            f.write(f"""// Temporary Box Plot JSL Script
// Generated by Box Plot Tool

// Choose File
filePath = Pick File("Choose JMP file", {{"JMP Files|jmp"}});
dt = Open(filePath);

// 設置參數
show_confidence = {1 if show_confidence else 0};
show_outliers = {1 if show_outliers else 0};
show_jitter = {1 if show_jitter else 0};

// 創建Box Plot
""")
            
            # 根據不同情況添加不同的代碼
            if x_group:
                f.write(f"""
// 使用X Group模式
gb = dt << Graph Builder(
    Show Control Panel(0),
    Variables(
        Group X(:{x_group}),
""")
            else:
                f.write("""
// 不使用X Group模式
gb = dt << Graph Builder(
    Show Control Panel(0),
    Variables(
""")
            
            # 添加Y變量
            for i, y_item in enumerate(y_items):
                if i == 0:
                    f.write(f"        Y(:{y_item})")
                else:
                    f.write(f",\n        Y(:{y_item}, Position(1))")
            
            f.write("\n    ),\n    Elements(\n")
            
            # 添加元素
            if plot_type == "contour":
                f.write("        Contour(Y, Legend(10)),\n")
            
            if x_group:
                f.write("""        Box Plot(
            X, Y,
            Legend(11),
""")
            else:
                f.write("""        Box Plot(
            Y,
            Legend(11),
""")
            
            # 添加選項
            f.write(f"            Jitter({1 if show_jitter else 0}),\n")
            f.write(f"            Outliers({1 if show_outliers else 0}),\n")
            f.write(f"            Confidence Diamond({1 if show_confidence else 0})\n")
            f.write("""        ),
        Caption Box(
            Y, 
            Legend(12), 
            Summary Statistic("Mean"),
            Summary Statistic2("N")
        )
    )
);

// 保存圖片
save_path = "$DESKTOP/BoxPlot_Custom.png";
Report(gb) << Save Picture(save_path);
Show("Box plot saved: " || save_path);
""")
        
        # 運行生成的JSL腳本
        open_file(jsl_path)

def open_box_plot_ui():
    """打開Box Plot UI界面"""
    root = tk.Tk()
    root.withdraw()  # 隱藏主窗口
    
    ui = BoxPlotUI()
    
    # 等待窗口關閉
    ui.root.wait_window()
    
    # 關閉主窗口
    root.destroy()

if __name__ == "__main__":
    open_box_plot_ui() 