import sys
import os

# 添加项目根目录到sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from TkEasyGo.core import SimpleWindow

def test_spinbox():
    window = SimpleWindow(title="Spinbox Test", width=400, height=200)
    
    spinbox = window.add_spinbox(from_=0, to=10, row=0, column=0)
    
    def on_spinbox_change():
        value = spinbox.get()
        window.log(f"Spinbox Value: {value}")
    
    window.bind_event('spinbox', '<<Increment>>', lambda e: on_spinbox_change())
    window.bind_event('spinbox', '<<Decrement>>', lambda e: on_spinbox_change())
    
    window.run()

if __name__ == "__main__":
    test_spinbox()
