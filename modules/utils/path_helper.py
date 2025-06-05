import os
import sys

def resource_path(relative_path):
    """取得打包後或開發階段的資源實體路徑"""
    # 检查路径是否需要转换
    if relative_path.startswith("config/"):
        # 将config/路径映射到新的目录结构
        parts = relative_path.split("/", 1)
        if len(parts) > 1:
            file_path = parts[1]
            # 根据文件扩展名决定映射到哪个目录
            if file_path.endswith(".jsl"):
                relative_path = f"scripts/jsl/{file_path}"
            elif file_path.endswith(".md"):
                relative_path = f"docs/{file_path}"
    
    # 返回最终路径
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), relative_path)