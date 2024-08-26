import sys
import os

# 添加项目根目录到sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from TkEasyGo.core import SimpleWindow

def test_scrollbar():
    window = SimpleWindow(title="Scrollbar Test", width=400, height=300)
    
    items = [f"Item {i}" for i in range(1, 101)]
    
    listbox = window.add_listbox(items, row=0, column=0)
    window.add_scrollbar('listbox', row=0, column=1)
    
    window.run()

if __name__ == "__main__":
    test_scrollbar()
