import sys
import os

# 添加项目根目录到sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from TkEasyGo.core import SimpleWindow

def test_notebook_and_slider():
    # 创建 SimpleWindow 实例
    window = SimpleWindow(title="Notebook & Slider Test", width=600, height=400)
    
    # 定义标签页内容
    def tab1_content(win, frame):
        win.add_label("Slider Example", row=0, column=0, frame=frame)
        win.add_slider(from_=0, to=100, value=50, row=1, column=0, frame=frame)
    
    def tab2_content(win, frame):
        win.add_label("This is tab 2", row=0, column=0, frame=frame)
    
    # 添加 Notebook
    window.add_notebook(tabs={"Tab 1": tab1_content, "Tab 2": tab2_content}, row=0, column=0, columnspan=2)
    
    # 运行窗口
    window.run()

if __name__ == "__main__":
    test_notebook_and_slider()
