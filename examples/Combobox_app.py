import sys
import os

# 添加项目根目录到sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from TkEasyGo.core import SimpleWindow

def combobox_app():
    # 创建窗口
    window = SimpleWindow(title="Combobox Example", width=300, height=200)
    
    # 添加标签
    window.add_label("Select an option:", row=0, column=0)
    
    # 添加下拉框
    combobox = window.add_combobox(["Option 1", "Option 2", "Option 3"], row=1, column=0)
    
    # 添加按钮以显示选择
    window.add_button("Show Selection", lambda: print(f"Selected: {combobox.get()}"), row=2, column=0)
    
    # 运行窗口
    window.run()

if __name__ == "__main__":
    combobox_app()
