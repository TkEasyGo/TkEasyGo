import sys
import os

# 添加项目根目录到sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from TkEasyGo.core import SimpleWindow, SimpleVariable

def create_tab_content(window, frame, label_text, button_text, button_command):
    window.add_label(label_text, row=0, column=0, frame=frame)
    window.add_button(button_text, button_command, row=1, column=0, frame=frame)

def tab1_content(window, frame):
    create_tab_content(window, frame, "This is Tab 1", "Click Me in Tab 1", lambda: print("Button in Tab 1 clicked"))

def tab2_content(window, frame):
    create_tab_content(window, frame, "This is Tab 2", "Click Me in Tab 2", lambda: print("Button in Tab 2 clicked"))

def tabbed_app():
    window = SimpleWindow(title="Tabbed TkEasyGo App", width=600, height=500)
    window.add_label("Welcome to TkEasyGo with Tabs!", row=0, column=0, columnspan=2)
    
    # 使用选项卡
    window.add_notebook({"Tab 1": tab1_content, "Tab 2": tab2_content}, row=1, column=0, columnspan=2)
    
    window.run()

if __name__ == "__main__":
    tabbed_app()
