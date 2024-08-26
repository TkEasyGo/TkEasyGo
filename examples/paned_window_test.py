import sys
import os

# 添加项目根目录到sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from TkEasyGo.core import SimpleWindow

def test_paned_window():
    window = SimpleWindow(title="Paned Window Test", width=600, height=400)
    
    paned_window = window.add_paned_window(row=0, column=0)
    
    frame1 = window.add_label_frame("Frame 1", row=0, column=0, rowspan=1, columnspan=1, style=None)
    frame2 = window.add_label_frame("Frame 2", row=0, column=1, rowspan=1, columnspan=1, style=None)
    
    paned_window.add(frame1)
    paned_window.add(frame2)
    
    window.add_label("Content in Frame 1", row=0, column=0, frame=frame1)
    window.add_label("Content in Frame 2", row=0, column=0, frame=frame2)
    
    window.run()

if __name__ == "__main__":
    test_paned_window()
