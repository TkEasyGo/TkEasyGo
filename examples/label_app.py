import sys
import os

# 添加项目根目录到sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from TkEasyGo.core import SimpleWindow

def test_dynamic_widgets_and_logging():
    # 创建 SimpleWindow 实例
    window = SimpleWindow(title="Dynamic Widgets & Logging Test", width=600, height=400)
    
    # 添加初始组件
    window.add_label("Dynamic Label", row=0, column=0)
    window.add_button("Remove Label", lambda: window.remove_widget('label'), row=1, column=0)
    window.add_button("Log Message", lambda: window.log("This is a log message"), row=2, column=0)
    
    # 运行窗口
    window.run()

if __name__ == "__main__":
    test_dynamic_widgets_and_logging()
