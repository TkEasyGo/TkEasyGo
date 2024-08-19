import sys
import os

# 添加项目根目录到sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from TkEasyGo.core import SimpleWindow

def test_layout_and_state_management():
    # 创建 SimpleWindow 实例
    window = SimpleWindow(title="Layout & State Management Test", width=500, height=400)
    
    # 设置全局网格布局配置
    window.set_grid_config(padx=5, pady=5, sticky="nsew")
    
    # 添加标签和按钮
    window.add_label("Label 1", row=0, column=0)
    window.add_label("Label 2", row=1, column=0)
    window.add_button("Disable Label 2", lambda: window.disable_widget('label'), row=2, column=0)
    window.add_button("Enable Label 2", lambda: window.enable_widget('label'), row=3, column=0)
    
    # 运行窗口
    window.run()

if __name__ == "__main__":
    test_layout_and_state_management()
