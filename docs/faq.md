# 常见问题

## 如何修改控件的样式？

你可以使用控件的 `config()` 方法来修改样式，比如背景色、字体等。

### 示例

```python
button.config(background_color="#ff0000")
```

## 如何处理多个事件？

你可以绑定多个事件处理函数到一个控件，例如多个按钮点击事件。

### 示例

```python
def on_click_1():
    print("Button 1 clicked!")

def on_click_2():
    print("Button 2 clicked!")

window.add_button("Button 1", on_click_1)
window.add_button("Button 2", on_click_2)
```