

# 控件介绍

## 标签 (`Label`)

用于显示静态文本。可以通过 `add_label` 方法添加。

### 方法签名

```python
window.add_label(text, row, column, columnspan=1)
```

### 参数

- **`text`**: 标签显示的文本内容。
- **`row`**: 标签所在的行。
- **`column`**: 标签所在的列。
- **`columnspan`** (可选): 标签跨越的列数，默认为 1。

### 示例

```python
window.add_label("这是一个标签", row=0, column=0, columnspan=2)
```

## 按钮 (`Button`)

用于触发事件。可以通过 `add_button` 方法添加。

### 方法签名

```python
window.add_button(text, command, row, column, columnspan=1)
```

### 参数

- **`text`**: 按钮上的文本。
- **`command`**: 按钮点击时调用的回调函数。
- **`row`**: 按钮所在的行。
- **`column`**: 按钮所在的列。
- **`columnspan`** (可选): 按钮跨越的列数，默认为 1。

### 示例

```python
window.add_button("点击我", lambda: print("按钮被点击"), row=1, column=0)
```

## 文本框 (`Textbox`)

用于输入和显示文本。可以通过 `add_textbox` 方法添加。

### 方法签名

```python
window.add_textbox(text, row, column, columnspan=1)
```

### 参数

- **`text`**: 文本框显示的初始文本。
- **`row`**: 文本框所在的行。
- **`column`**: 文本框所在的列。
- **`columnspan`** (可选): 文本框跨越的列数，默认为 1。

### 示例

```python
textbox = window.add_textbox("默认文本", row=2, column=0, columnspan=2)
```

### 获取和设置值

- **获取值**: 使用 `get()` 方法获取文本框的当前值。
  
  ```python
  value = textbox.get()
  ```

- **设置值**: 使用 `set()` 方法设置文本框的值。
  
  ```python
  textbox.set("新文本")
  ```

## 复选框 (`Checkbox`)

允许用户选择或取消选择一个选项。可以通过 `add_checkbox` 方法添加。

### 方法签名

```python
window.add_checkbox(text, variable, row, column)
```

### 参数

- **`text`**: 复选框的标签文本。
- **`variable`**: 一个 `SimpleVariable` 实例，用于保存复选框的状态。
- **`row`**: 复选框所在的行。
- **`column`**: 复选框所在的列。

### 示例

```python
checkbox_var = SimpleVariable()
window.add_checkbox("勾选我", checkbox_var, row=3, column=0)
```

### 获取和设置值

- **获取值**: 使用 `get()` 方法获取复选框的状态（布尔值）。
  
  ```python
  checked = checkbox_var.get()
  ```

- **设置值**: 使用 `set()` 方法设置复选框的状态。
  
  ```python
  checkbox_var.set(True)  # 选中
  checkbox_var.set(False) # 取消选中
  ```

## 单选按钮 (`Radiobutton`)

允许用户在多个选项中选择一个。可以通过 `add_radiobutton` 方法添加。

### 方法签名

```python
window.add_radiobutton(text, value, variable, row, column)
```

### 参数

- **`text`**: 单选按钮的标签文本。
- **`value`**: 单选按钮的值。
- **`variable`**: 一个 `SimpleVariable` 实例，用于保存当前选中的值。
- **`row`**: 单选按钮所在的行。
- **`column`**: 单选按钮所在的列。

### 示例

```python
radiobutton_var = SimpleVariable("1")
window.add_radiobutton("选项 1", "1", radiobutton_var, row=4, column=0)
```

### 获取和设置值

- **获取值**: 使用 `get()` 方法获取当前选中的值。
  
  ```python
  selected_value = radiobutton_var.get()
  ```

- **设置值**: 使用 `set()` 方法设置选中的值（通常在创建控件时设置）。
  
  ```python
  radiobutton_var.set("2")  # 选择值为 "2" 的单选按钮
  ```

## 下拉框 (`Combobox`)

提供一个下拉列表供用户选择。可以通过 `add_combobox` 方法添加。

### 方法签名

```python
window.add_combobox(options, row, column)
```

### 参数

- **`options`**: 一个列表，包含下拉框的所有选项。
- **`row`**: 下拉框所在的行。
- **`column`**: 下拉框所在的列。

### 示例

```python
combobox = window.add_combobox(["选项 1", "选项 2", "选项 3"], row=5, column=0)
```

### 获取和设置值

- **获取值**: 使用 `get()` 方法获取当前选中的值。
  
  ```python
  selected_option = combobox.get()
  ```

- **设置值**: 使用 `set()` 方法设置选中的值（如果下拉框是可编辑的）。
  
  ```python
  combobox.set("选项 2")
  ```

## 进度条 (`Progressbar`)

用于显示进度的可视化控件。

### 示例

```python
progressbar = window.add_progressbar(value=progress_value.get(), row=0, column=0, columnspan=2)
```

创建一个进度条，初始值为 `progress_value`。

```python
progressbar.config(value=progress_value.get())
```

更新进度条的值，`progress_value.get()` 提供新的值。

## 滑块 (`Slider`)

用于选择一个数值范围内的值。可以通过 `add_slider` 方法添加。

### 方法签名

```python
window.add_slider(value, row, column, columnspan=1)
```

### 参数

- **`value`**: 滑块的初始值。
- **`row`**: 滑块所在的行。
- **`column`**: 滑块所在的列。
- **`columnspan`** (可选): 滑块跨越的列数，默认为 1。

### 示例

```python
slider = window.add_slider(value=50, row=7, column=0, columnspan=2)
```

### 获取和设置值

- **获取值**: 使用 `get()` 方法获取当前滑块的值。
  
  ```python
  current_value = slider.get()
  ```

- **设置值**: 使用 `set()` 方法设置滑块的值。
  
  ```python
  slider.set(25)
  ```

## 选项卡 (`Notebook`)

提供多个标签页以组织内容。可以通过 `add_notebook` 方法添加。

### 方法签名

```python
window.add_notebook(tabs, row, column, columnspan=1)
```

### 参数

- **`tabs`**: 一个列表，包含标签页的标题。
- **`row`**: 选项卡所在的行。
- **`column`**: 选项卡所在的列。
- **`columnspan`** (可选): 选项卡跨越的列数，默认为 1。

### 示例

```python
notebook = window.add_notebook(["标签页 1", "标签页 2"], row=8, column=0, columnspan=2)
```

### 使用选项卡

你可以根据需要设置和获取选项卡的内容和当前选择。

```python
# 获取当前选中的标签页
selected_tab = notebook.get()

# 设置标签页内容
notebook.set("标签页 2")
```

## 窗口分隔条 (`PanedWindow`)

用于创建可调整大小的窗格。可以通过 `add_paned_window` 方法添加。

### 方法签名

```python
window.add_paned_window(orient, row, column, columnspan=1)
```

### 参数

- **`orient`**: 分隔条的方向（`horizontal` 或 `vertical`）。
- **`row`**: 分隔条所在的行。
- **`column`**: 分隔条所在的列。
- **`columnspan`** (可选): 分隔条跨越的列数，默认为 1。

### 示例

```python
paned_window = window.add_paned_window(orient="vertical", row=9, column=0, columnspan=2)
```

## 滚动条 (`Scrollbar`)

用于在内容超

出视图范围时滚动视图。可以通过 `add_scrollbar` 方法添加。

### 方法签名

```python
window.add_scrollbar(orient, row, column, columnspan=1)
```

### 参数

- **`orient`**: 滚动条的方向（`vertical` 或 `horizontal`）。
- **`row`**: 滚动条所在的行。
- **`column`**: 滚动条所在的列。
- **`columnspan`** (可选): 滚动条跨越的列数，默认为 1。

### 示例

```python
scrollbar = window.add_scrollbar(orient="vertical", row=10, column=0)
```

## 分隔符 (`Separator`)

用于在控件之间创建视觉上的分隔。可以通过 `add_separator` 方法添加。

### 方法签名

```python
window.add_separator(orient, row, column, columnspan=1)
```

### 参数

- **`orient`**: 分隔符的方向（`horizontal` 或 `vertical`）。
- **`row`**: 分隔符所在的行。
- **`column`**: 分隔符所在的列。
- **`columnspan`** (可选): 分隔符跨越的列数，默认为 1。

### 示例

```python
separator = window.add_separator(orient="horizontal", row=11, column=0, columnspan=2)
```

## 数字输入框 (`Spinbox`)

允许用户选择一个数值范围内的值。可以通过 `add_spinbox` 方法添加。

### 方法签名

```python
window.add_spinbox(values, row, column, columnspan=1)
```

### 参数

- **`values`**: 一个元组，定义了数值范围和步长（例如 `(0, 100, 1)`）。
- **`row`**: 数字输入框所在的行。
- **`column`**: 数字输入框所在的列。
- **`columnspan`** (可选): 数字输入框跨越的列数，默认为 1。

### 示例

```python
spinbox = window.add_spinbox(values=(0, 100, 1), row=12, column=0)
```

## 树视图 (`Treeview`)

用于显示层次结构的数据。可以通过 `add_treeview` 方法添加。

### 方法签名

```python
window.add_treeview(columns, row, column, columnspan=1)
```

### 参数

- **`columns`**: 一个列表，定义树视图的列。
- **`row`**: 树视图所在的行。
- **`column`**: 树视图所在的列。
- **`columnspan`** (可选): 树视图跨越的列数，默认为 1。

### 示例

```python
treeview = window.add_treeview(columns=["Column 1", "Column 2"], row=13, column=0, columnspan=2)
```

