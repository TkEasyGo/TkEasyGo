import sys
import os

# 添加项目根目录到sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from TkEasyGo.core import SimpleWindow

def test_treeview():
    window = SimpleWindow(title="Treeview Test", width=600, height=400)
    
    columns = ["Name", "Age", "City"]
    
    # 移除或使用默认的 Treeview 样式
    treeview = window.add_treeview(columns, row=0, column=0)
    
    # 插入一些数据
    treeview.insert("", "end", values=("Alice", "30", "New York"))
    treeview.insert("", "end", values=("Bob", "25", "Los Angeles"))
    treeview.insert("", "end", values=("Charlie", "35", "Chicago"))
    
    def on_select(event):
        selected_item = treeview.selection()
        if selected_item:
            item = treeview.item(selected_item)
            window.log(f"Selected: {item['values']}")
    
    window.bind_event('treeview', '<<TreeviewSelect>>', on_select)
    
    window.run()

if __name__ == "__main__":
    test_treeview()
