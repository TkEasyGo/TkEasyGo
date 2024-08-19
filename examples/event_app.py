import sys
import os

# 添加项目根目录到sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from TkEasyGo.core import SimpleWindow, SimpleVariable

def test_event_binding():
    # 创建 SimpleWindow 实例
    window = SimpleWindow(title="Event Binding Test", width=500, height=300)
    
    # 创建 SimpleVariable 实例
    var = SimpleVariable("Default Text")
    
    # 添加输入框
    window.add_textbox(default_text="Type something...", width=30, row=0, column=0)
    
    # 添加事件绑定
    def on_key_press(event):
        window.log(f"Key Pressed: {event.keysym}")
    
    def on_focus(event):
        window.log("Textbox focused")
    
    window.bind_events('textbox', {'<KeyPress>': on_key_press, '<FocusIn>': on_focus})
    
    # 运行窗口
    window.run()

if __name__ == "__main__":
    test_event_binding()
