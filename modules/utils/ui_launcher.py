"""
UI Launcher Module
Used for centralized management of UI interface launching, avoiding circular import issues
"""

def launch_box_plot_ui():
    """
    Launch Box Plot UI interface
    This function uses delayed import to avoid circular dependency issues
    """
    from modules.ui.box_plot_ui import open_box_plot_ui
    open_box_plot_ui() 