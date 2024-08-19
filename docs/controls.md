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
window.add_label("This is a label", row=0, column=0, columnspan=2)
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
window.add_button("Click Me", lambda: print("Button clicked"), row=1, column=0)
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
textbox = window.add_textbox("Default text", row=2, column=0, columnspan=2)
```

### 获取和设置值

- **获取值**: 使用 `get()` 方法获取文本框的当前值。
  
  ```python
  value = textbox.get()
  ```

- **设置值**: 使用 `set()` 方法设置文本框的值。
  
  ```python
  textbox.set("New text")
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
window.add_checkbox("Check me", checkbox_var, row=3, column=0)
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
window.add_radiobutton("Option 1", "1", radiobutton_var, row=4, column=0)
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
combobox = window.add_combobox(["Option 1", "Option 2", "Option 3"], row=5, column=0)
```

### 获取和设置值

- **获取值**: 使用 `get()` 方法获取当前选中的值。
  
  ```python
  selected_option = combobox.get()
  ```

- **设置值**: 使用 `set()` 方法设置选中的值（如果下拉框是可编辑的）。
  
  ```python
  combobox.set("Option 2")
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

- **

`tabs`**: 一个列表，包含标签页的标题。
- **`row`**: 选项卡所在的行。
- **`column`**: 选项卡所在的列。
- **`columnspan`** (可选): 选项卡跨越的列数，默认为 1。

### 示例

```python
notebook = window.add_notebook(["Tab 1", "Tab 2"], row=8, column=0, columnspan=2)
```

### 使用选项卡

你可以根据需要设置和获取选项卡的内容和当前选择。

```python
# 获取当前选中的标签页
selected_tab = notebook.get()

# 设置标签页内容
notebook.set("Tab 2")
```