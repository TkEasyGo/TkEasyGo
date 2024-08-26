import sys
import os

# 添加项目根目录到sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from TkEasyGo.core import SimpleWindow

def test_separator():
    window = SimpleWindow(title="Separator Test", width=400, height=200)
    
    window.add_label("Above Separator", row=0, column=0)
    window.add_separator(orient="horizontal", row=1, column=0)  # 使用 "horizontal" 而不是 tk.HORIZONTAL
    window.add_label("Below Separator", row=2, column=0)
    
    window.run()

if __name__ == "__main__":
    test_separator()
