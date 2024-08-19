# 窗口操作

## 创建窗口

创建一个窗口使用 `SimpleWindow` 类。

### 示例

```python
from TkEasyGo.core import SimpleWindow

window = SimpleWindow(title="My Window", width=400, height=300)
```

## 运行窗口

使用 `run()` 方法启动事件循环。

### 示例

```python
window.run()
```

## 关闭窗口

使用 `close()` 方法关闭窗口。

### 示例

```python
window.close()
```