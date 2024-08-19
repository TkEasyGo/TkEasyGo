# 事件绑定

## 绑定事件

### 按钮点击事件

绑定按钮点击事件使用 `add_button` 方法。

### 示例

```python
window.add_button("Click Me", on_button_click)

def on_button_click():
    print("Button was clicked")
```

## 事件处理函数

事件处理函数可以定义任何逻辑，处理相应的事件。

### 示例

```python
def on_button_click():
    print("Button clicked!")
```