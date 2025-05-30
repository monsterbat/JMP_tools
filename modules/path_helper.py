import os
import sys

def resource_path(relative_path):
    """取得打包後或開發階段的資源實體路徑"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), relative_path)