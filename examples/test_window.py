import sys
import os

# 添加项目根目录到sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from TkEasyGo.core import SimpleWindow, SimpleVariable



def test_window():
    # Create the SimpleWindow instance
    window = SimpleWindow(title="Window Test", width=400, height=300)
    
    # Add buttons to test maximize, minimize, restore
    window.add_button("Maximize", window.maximize, row=0, column=0)
    window.add_button("Minimize", window.minimize, row=1, column=0)
    window.add_button("Restore", window.restore, row=2, column=0)
    
    # Run the window
    window.run()

if __name__ == "__main__":
    test_window()
