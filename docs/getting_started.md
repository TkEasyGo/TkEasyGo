# 快速入门

## 创建一个基本的窗口

下面的示例展示了如何创建一个简单的窗口，并添加一些基本控件：

```python
from TkEasyGo.core import SimpleWindow, SimpleVariable

def basic_app():
    # 创建窗口
    window = SimpleWindow(title="Basic TkEasyGo App", width=300, height=200)
    
    # 添加标签
    window.add_label("Welcome to TkEasyGo!", row=0, column=0, columnspan=2)
    
    # 添加文本框
    textbox = window.add_textbox("Type here...", row=1, column=0, columnspan=2)
    
    # 添加按钮
    button = window.add_button("Submit", lambda: print("Submit clicked"), row=2, column=0, columnspan=2)
    
    # 添加复选框
    checkbox_var = SimpleVariable()
    window.add_checkbox("Check me", checkbox_var, row=3, column=0)
    
    # 运行窗口
    window.run()

if __name__ == "__main__":
    basic_app()
```