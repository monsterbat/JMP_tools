"""
UI啟動器模塊
用於集中管理UI界面的啟動，避免循環導入問題
"""

def launch_box_plot_ui():
    """
    啟動Box Plot UI界面
    這個函數通過延遲導入來避免循環依賴問題
    """
    from modules.ui.box_plot_ui import open_box_plot_ui
    open_box_plot_ui() 