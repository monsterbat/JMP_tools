#!/usr/bin/env python3
import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from modules.core.aicc_calculator import AICcCalculator

class AICcCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AICc 分布配適計算器 - 與 JMP 一致")
        self.root.geometry("800x600")
        
        self.data = None
        self.calculator = AICcCalculator()
        
        self.setup_ui()
    
    def setup_ui(self):
        # 標題
        title_label = tk.Label(self.root, text="AICc 分布配適計算器", 
                              font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
        
        subtitle_label = tk.Label(self.root, text="支援 9 個分布，與 JMP 邏輯一致", 
                                 font=("Arial", 10))
        subtitle_label.pack(pady=5)
        
        # 分布列表
        distributions_text = ("支援的分布:\n"
                             "• Normal, LogNormal, Exponential, Gamma, Weibull\n"
                             "• Johnson Sb, SHASH, Mixture of 2 Normals, Mixture of 3 Normals")
        dist_label = tk.Label(self.root, text=distributions_text, 
                             font=("Arial", 9), justify=tk.LEFT)
        dist_label.pack(pady=10)
        
        # 檔案選擇
        file_frame = tk.Frame(self.root)
        file_frame.pack(pady=10, fill=tk.X, padx=20)
        
        tk.Label(file_frame, text="選擇資料檔案:").pack(anchor=tk.W)
        
        file_select_frame = tk.Frame(file_frame)
        file_select_frame.pack(fill=tk.X, pady=5)
        
        self.file_path_var = tk.StringVar()
        file_entry = tk.Entry(file_select_frame, textvariable=self.file_path_var, 
                             state='readonly', width=60)
        file_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        browse_btn = tk.Button(file_select_frame, text="瀏覽", 
                              command=self.select_file)
        browse_btn.pack(side=tk.RIGHT, padx=(5, 0))
        
        # 欄位選擇
        column_frame = tk.Frame(self.root)
        column_frame.pack(pady=10, fill=tk.X, padx=20)
        
        tk.Label(column_frame, text="選擇要分析的欄位:").pack(anchor=tk.W)
        
        self.column_var = tk.StringVar()
        self.column_combo = ttk.Combobox(column_frame, textvariable=self.column_var,
                                        state='readonly', width=40)
        self.column_combo.pack(fill=tk.X, pady=5)
        
        # 計算按鈕
        calc_btn = tk.Button(self.root, text="計算 AICc 值", 
                            command=self.calculate_distributions,
                            bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
        calc_btn.pack(pady=20)
        
        # 結果顯示
        result_frame = tk.Frame(self.root)
        result_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        tk.Label(result_frame, text="計算結果:", font=("Arial", 12, "bold")).pack(anchor=tk.W)
        
        # 創建結果文字框
        self.result_text = tk.Text(result_frame, height=15, wrap=tk.WORD)
        scrollbar = tk.Scrollbar(result_frame)
        
        self.result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.result_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.result_text.yview)
        
    def select_file(self):
        """選擇檔案"""
        file_path = filedialog.askopenfilename(
            title="選擇資料檔案",
            filetypes=[
                ("Excel 檔案", "*.xlsx *.xls"),
                ("CSV 檔案", "*.csv"),
                ("所有檔案", "*.*")
            ]
        )
        
        if file_path:
            self.file_path_var.set(file_path)
            self.load_file(file_path)
    
    def load_file(self, file_path):
        """載入檔案並更新欄位列表"""
        try:
            if file_path.endswith(('.xlsx', '.xls')):
                self.data = pd.read_excel(file_path)
            elif file_path.endswith('.csv'):
                self.data = pd.read_csv(file_path)
            else:
                messagebox.showerror("錯誤", "不支援的檔案格式")
                return
            
            # 更新欄位列表 - 只顯示數值欄位
            numeric_columns = []
            for col in self.data.columns:
                if pd.api.types.is_numeric_dtype(self.data[col]):
                    numeric_columns.append(col)
            
            self.column_combo['values'] = numeric_columns
            
            if numeric_columns:
                self.column_combo.set(numeric_columns[0])
            
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, 
                f"成功載入檔案: {file_path}\n"
                f"資料形狀: {self.data.shape}\n"
                f"可用的數值欄位: {len(numeric_columns)} 個\n\n"
                "請選擇要分析的欄位，然後按下「計算 AICc 值」。")
            
        except Exception as e:
            messagebox.showerror("錯誤", f"載入檔案失敗: {str(e)}")
    
    def calculate_distributions(self):
        """計算所有分布的 AICc 值"""
        if self.data is None:
            messagebox.showerror("錯誤", "請先選擇資料檔案")
            return
        
        if not self.column_var.get():
            messagebox.showerror("錯誤", "請選擇要分析的欄位")
            return
        
        column_name = self.column_var.get()
        
        try:
            # 提取欄位數據
            column_data = self.data[column_name].dropna()
            
            if len(column_data) < 3:
                messagebox.showerror("錯誤", "數據點太少，無法進行分析")
                return
            
            # 顯示計算進度
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"正在計算 {column_name} 欄位的 AICc 值...\n\n")
            self.result_text.insert(tk.END, f"數據統計:\n")
            self.result_text.insert(tk.END, f"數據點數量: {len(column_data)}\n")
            self.result_text.insert(tk.END, f"平均值: {column_data.mean():.6f}\n")
            self.result_text.insert(tk.END, f"標準差: {column_data.std():.6f}\n")
            self.result_text.insert(tk.END, f"範圍: {column_data.min():.6f} 到 {column_data.max():.6f}\n\n")
            self.result_text.update()
            
            # 計算所有分布
            results = self.calculator.calculate_all_distributions(column_data, column_name)
            
            # 排序結果
            sorted_results = sorted([(name, aicc) for name, aicc in results.items() 
                                   if np.isfinite(aicc)], key=lambda x: x[1])
            
            # 顯示結果
            self.result_text.insert(tk.END, "="*50 + "\n")
            self.result_text.insert(tk.END, "AICc 計算結果 (按優劣排序):\n")
            self.result_text.insert(tk.END, "="*50 + "\n\n")
            
            for i, (name, aicc) in enumerate(sorted_results):
                rank_symbol = "🥇" if i == 0 else "🥈" if i == 1 else "🥉" if i == 2 else f"{i+1:2d}."
                self.result_text.insert(tk.END, f"{rank_symbol} {name:20s}: AICc = {aicc:10.3f}\n")
            
            if len(sorted_results) > 0:
                best_name, best_aicc = sorted_results[0]
                self.result_text.insert(tk.END, f"\n最佳分布: {best_name}\n")
                self.result_text.insert(tk.END, f"最佳 AICc 值: {best_aicc:.3f}\n")
                
                # 特殊提示
                if "GAMMA" in column_name.upper():
                    self.result_text.insert(tk.END, f"\n💡 注意: GAMMA 欄位已自動應用 JMP 修正邏輯\n")
                
                if column_data.std() < 0.001:
                    self.result_text.insert(tk.END, f"\n💡 注意: 數據變異很小，已使用穩健算法處理 Mixture 分布\n")
            
            # 顯示計算詳情按鈕
            details_frame = tk.Frame(self.root)
            details_frame.pack(pady=10)
            
            save_btn = tk.Button(details_frame, text="儲存結果", 
                               command=lambda: self.save_results(column_name, results))
            save_btn.pack(side=tk.LEFT, padx=5)
            
        except Exception as e:
            messagebox.showerror("錯誤", f"計算失敗: {str(e)}")
    
    def save_results(self, column_name, results):
        """儲存結果到檔案"""
        try:
            file_path = filedialog.asksaveasfilename(
                title="儲存結果",
                defaultextension=".txt",
                filetypes=[("文字檔案", "*.txt"), ("所有檔案", "*.*")]
            )
            
            if file_path:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(f"AICc 計算結果 - {column_name} 欄位\n")
                    f.write("="*50 + "\n\n")
                    
                    sorted_results = sorted([(name, aicc) for name, aicc in results.items() 
                                           if np.isfinite(aicc)], key=lambda x: x[1])
                    
                    for i, (name, aicc) in enumerate(sorted_results):
                        f.write(f"{i+1:2d}. {name:20s}: AICc = {aicc:10.3f}\n")
                    
                    if sorted_results:
                        best_name, best_aicc = sorted_results[0]
                        f.write(f"\n最佳分布: {best_name}\n")
                        f.write(f"最佳 AICc 值: {best_aicc:.3f}\n")
                
                messagebox.showinfo("成功", f"結果已儲存到: {file_path}")
                
        except Exception as e:
            messagebox.showerror("錯誤", f"儲存失敗: {str(e)}")

def main():
    """主程序"""
    print("=== AICc 分布配適計算器 ===")
    print("此工具將幫助您計算不同分布的AICc值，找出最佳配適分布")
    print("支援的分布:")
    print("• Normal, LogNormal, Exponential, Gamma, Weibull")
    print("• Johnson Sb, SHASH, Mixture of 2 Normals, Mixture of 3 Normals")
    print("共 9 個分布，與JMP內建功能一致")
    print()
    
    root = tk.Tk()
    app = AICcCalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main() 