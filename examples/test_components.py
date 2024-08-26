import sys
import os

# 添加项目根目录到 sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from TkEasyGo.core import SimpleWindow

def test_components():
    # 创建 SimpleWindow 实例
    window = SimpleWindow(title="Components Test", width=600, height=400)
    
    # 文件对话框测试
    def open_file():
        file_path = window.open_file_dialog(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            window.show_messagebox("Selected File", file_path)
    
    # 颜色选择器测试
    def choose_color():
        color = window.open_color_dialog()
        if color:
            window.show_messagebox("Selected Color", color)
    
    # 提示框测试
    def show_message():
        window.show_messagebox("Information", "This is a message box.")
    
    # 添加按钮以触发对话框、颜色选择器和消息框
    window.add_button("Open File Dialog", open_file, row=0, column=0)
    window.add_button("Choose Color", choose_color, row=1, column=0)
    window.add_button("Show Message Box", show_message, row=2, column=0)
    
    # # 日历控件测试
    # window.add_label("Select a date:", row=3, column=0)
    # calendar = window.add_calendar(row=4, column=0)
    
    # 工具提示测试
    window.add_tooltip("Open File Dialog", "Click to open a file")
    window.add_tooltip("Choose Color", "Click to choose a color")
    window.add_tooltip("Show Message Box", "Click to show a message box")
    
    # 右键菜单测试
    def menu_action():
        window.show_messagebox("Menu Action", "Right-click menu item selected.")
    
    context_menu_items = {"Menu Item 1": menu_action, "Menu Item 2": menu_action}
    window.add_context_menu("Show Message Box", context_menu_items)
    
    # 运行窗口
    window.run()

if __name__ == "__main__":
    test_components()
