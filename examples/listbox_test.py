import sys
import os

# 添加项目根目录到sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from TkEasyGo.core import SimpleWindow

def test_listbox():
    window = SimpleWindow(title="Listbox Test", width=400, height=300)
    
    items = ["Item 1", "Item 2", "Item 3", "Item 4"]
    
    def on_select(event):
        selected = event.widget.curselection()
        if selected:
            window.log(f"Selected: {items[selected[0]]}")
    
    listbox = window.add_listbox(items, row=0, column=0)
    window.bind_event('listbox', '<<ListboxSelect>>', on_select)
    
    window.run()

if __name__ == "__main__":
    test_listbox()
