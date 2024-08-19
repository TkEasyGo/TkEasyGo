# 样式设置

## 设置窗口标题

设置窗口标题使用 `title` 参数。

### 示例

```python
window = SimpleWindow(title="My Styled Window")
```

## 设置窗口大小

设置窗口大小使用 `width` 和 `height` 参数。

### 示例

```python
window = SimpleWindow(width=600, height=400)
```

## 控件样式

你可以使用控件的方法设置样式，比如设置按钮的文本、背景色等。

### 示例

```python
button = window.add_button("Styled Button", command)
button.set_background_color("#ff0000")
```