
# 控件介绍

---

## 标签 (`Label`)

用于显示静态文本。可以通过 `add_label` 方法添加。

### 初始化方法

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


---

## 按钮 (`Button`)

用于触发事件。可以通过 `add_button` 方法添加。

### 初始化方法

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

---

## 文本框 (`Textbox`)

用于输入和显示文本。可以通过 `add_textbox` 方法添加。

### 初始化方法

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


---

## 复选框 (`Checkbox`)

允许用户选择或取消选择一个选项。可以通过 `add_checkbox` 方法添加。

### 初始化方法

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


---

## 单选按钮 (`Radiobutton`)

允许用户在多个选项中选择一个。可以通过 `add_radiobutton` 方法添加。

### 初始化方法

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

---

## 下拉框 (`Combobox`)

提供一个下拉列表供用户选择。可以通过 `add_combobox` 方法添加。

### 初始化方法

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

---

## 进度条 (`Progressbar`)

用于显示进度的可视化控件。

### 初始化方法

```python
progressbar = window.add_progressbar(variable, row, column, columnspan=1)
```

### 参数

- **`variable`**: 一个 `SimpleVariable` 实例，用于保存进度条的当前值。
- **`row`**: 进度条所在的行。
- **`column`**: 进度条所在的列。
- **`columnspan`** (可选): 进度条跨越的列数，默认为 1。

### 示例

```python
progress_value = SimpleVariable(50)
progressbar = window.add_progressbar(progress_value, row=6, column=0, columnspan=2)
```

### 更新进度值

- **设置值**: 使用 `set()` 方法更新进度条的值。
  
  ```python
  progress_value.set(75)  # 更新进度条值
  ```


---

## 滑块 (`Slider`)

用于选择一个数值范围内的值。可以通过 `add_slider` 方法添加。

### 初始化方法

```python
window.add_slider(variable, row, column, columnspan=1)
```

### 参数

- **`variable`**: 一个 `SimpleVariable` 实例，用于保存滑块的当前值。
- **`row`**: 滑块所在的行。
- **`column`**: 滑块所在的列。
- **`columnspan`** (可选): 滑块跨越的列数，默认为 1。

### 示例

```python
slider_value = SimpleVariable(50)
slider = window.add_slider(slider_value, row=7, column=0, columnspan=2)
```

### 获取和设置值

- **获取值**: 使用 `get()` 方法获取当前滑块的值。
  
  ```python
  current_value = slider_value.get()
  ```

- **设置值**: 使用 `set()` 方法设置滑块的值。
  
  ```python
  slider_value.set(25)
  ```


---

## 选项卡 (`Notebook`)

提供多个标签页以组织内容。可以通过 `add_notebook` 方法添加。

### 初始化方法

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

- **获取当前选中的标签页**: 使用 `get()` 方法获取当前选中的标签页。
  
  ```python
  selected_tab = notebook.get()
  ```

- **设置当前选中的标签页**: 使用 `set()` 方法设置当前选中的标签页。
  
  ```python
  notebook.set("标签页 2")
  ```


---

## 窗口分隔条 (`PanedWindow`)

用于创建可调整大小的窗格。可以通过 `add_paned_window` 方法添加。

###

 初始化方法

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


---

## 滚动条 (`Scrollbar`)

用于在内容超出视图范围时滚动视图。可以通过 `add_scrollbar` 方法添加。

### 初始化方法

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


---

## 分隔符 (`Separator`)

用于在控件之间创建视觉上的分隔。可以通过 `add_separator` 方法添加。

### 初始化方法

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


---

## 数字输入框 (`Spinbox`)

允许用户选择一个数值范围内的值。可以通过 `add_spinbox` 方法添加。

### 初始化方法

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

### 获取和设置值

- **获取值**: 使用 `get()` 方法获取当前数字输入框的值。
  
  ```python
  current_value = spinbox.get()
  ```

- **设置值**: 使用 `set()` 方法设置数字输入框的值。
  
  ```python
  spinbox.set(50)
  ```


---

## 树视图 (`Treeview`)

用于显示层次结构的数据。可以通过 `add_treeview` 方法添加。

### 初始化方法

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

### 添加和操作项

- **添加项**: 使用 `insert()` 方法向树视图添加项。
  
  ```python
  treeview.insert("", "end", text="Item 1", values=("Value 1", "Value 2"))
  ```

- **删除项**: 使用 `delete()` 方法删除指定项。
  
  ```python
  treeview.delete(item_id)
  ```



---

## 工具提示 (`Tooltip`)

添加工具提示（tooltip）到指定的组件，当鼠标悬停在组件上时显示提示信息。

#### 初始化方法

```python
window.add_tooltip(widget_name, text)
```

#### 参数

- **`widget_name`**: 需要添加工具提示的组件名称。
- **`text`**: 显示的提示文本。

#### 示例

```python
window.add_tooltip('button1', 'Click to submit')
```

---

## 右键菜单 (`ContextMenu`)

为指定的组件添加右键菜单（上下文菜单）。

#### 初始化方法

```python
window.add_context_menu(widget_name, menu_items)
```

#### 参数

- **`widget_name`**: 需要添加右键菜单的组件名称。
- **`menu_items`**: 菜单项的字典，键为菜单项名称，值为命令函数。

#### 示例

```python
def copy_command():
    print("Copy selected")

def paste_command():
    print("Paste selected")

window.add_context_menu('text1', {'Copy': copy_command, 'Paste': paste_command})
```

---

##  文本标签 (`Text`)

向窗口添加一个文本标签。

#### 初始化方法

```python
window.add_text(text, row=None, column=None, columnspan=1, style=None)
```

#### 参数

- **`text`**: 显示的文本。
- **`row`**: 文本标签所在的行（可选）。
- **`column`**: 文本标签所在的列（可选）。
- **`columnspan`**: 文本标签跨越的列数（可选），默认为 1。
- **`style`**: 字典形式的样式配置（可选）。

#### 示例

```python
window.add_text('Hello World', row=0, column=0)
```

---

## 列表框 (`Listbox`)
向窗口添加一个列表框（Listbox）。

#### 初始化方法

```python
window.add_listbox(items, row=None, column=None, columnspan=1, style=None, frame=None)
```

#### 参数

- **`items`**: 列表框中的项列表。
- **`row`**: 列表框所在的行（可选）。
- **`column`**: 列表框所在的列（可选）。
- **`columnspan`**: 列表框跨越的列数（可选），默认为 1。
- **`style`**: 字典形式的样式配置（可选）。
- **`frame`**: 列表框所在的帧（可选），默认为根帧。

#### 示例

```python
window.add_listbox(['Item 1', 'Item 2'], row=1, column=0)
```




---

## 消息控件 (`Message`)

向窗口添加一个消息控件。

#### 初始化方法

```python
window.add_message(text, row=None, column=None, columnspan=1, style=None)
```

#### 参数

- **`text`**: 显示的消息文本。
- **`row`**: 消息控件所在的行（可选）。
- **`column`**: 消息控件所在的列（可选）。
- **`columnspan`**: 消息控件跨越的列数（可选），默认为 1。
- **`style`**: 字典形式的样式配置（可选）。

#### 示例

```python
window.add_message('This is a message', row=2, column=0)
```




---

## 添加组件 (`add_widget`)

帮助函数，将指定的组件添加到窗口中，使用网格布局。

#### 初始化方法

```python
window.add_widget(widget, row=None, column=None, rowspan=1, columnspan=1)
```

#### 参数

- **`widget`**: 需要添加的组件。
- **`row`**: 组件所在的行（可选）。
- **`column`**: 组件所在的列（可选）。
- **`rowspan`**: 组件跨越的行数（可选），默认为 1。
- **`columnspan`**: 组件跨越的列数（可选），默认为 1。

#### 示例

```python
label = tk.Label(window.root, text="Label")
window.add_widget(label, row=0, column=0)
```

---

## 菜单栏 (`Menu`)

向窗口添加一个菜单栏。

#### 初始化方法

```python
window.add_menu(menu_structure)
```

#### 参数

- **`menu_structure`**: 菜单结构的字典，键为菜单名称，值为子菜单字典。

#### 示例

```python
def open_command():
    print("Open selected")

def exit_command():
    window.root.quit()

menu_structure = {
    'File': {'Open': open_command, 'Exit': exit_command},
    'Help': {'About': lambda: print("About")}
}
window.add_menu(menu_structure)
```

---

## 下拉菜单按钮 (`Menubutton`)

向窗口添加一个下拉菜单按钮。

#### 初始化方法

```python
window.add_menubutton(text, menu_items, row=None, column=None, style=None)
```

#### 参数

- **`text`**: 菜单按钮上的文本。
- **`menu_items`**: 菜单项的字典，键为菜单项名称，值为命令函数。
- **`row`**: 菜单按钮所在的行（可选）。
- **`column`**: 菜单按钮所在的列（可选）。
- **`style`**: 字典形式的样式配置（可选）。

#### 示例

```python
def new_command():
    print("New selected")

window.add_menubutton('File', {'New': new_command}, row=1, column=0)
```




---

## 选项菜单 (`OptionMenu`)

向窗口添加一个选项菜单（OptionMenu）。

#### 初始化方法

```python
window.add_option_menu(variable, values, row=None, column=None, style=None, frame=None)
```

#### 参数

- **`variable`**: 关联的 Tkinter 变量。
- **`values`**: 选项菜单的值列表。
- **`row`**: 选项菜单所在的行（可选）。
- **`column`**: 选项菜单所在的列（可选）。
- **`style`**: 字典形式的样式配置（可选）。
- **`frame`**: 选项菜单所在的帧（可选），默认为根帧。

#### 示例

```python
variable = tk.StringVar()
window.add_option_menu(variable, ['Option 1', 'Option 2'], row=3, column=1)
```

---

## 图片 (`Image`)

向窗口添加一张图片。

#### 初始化方法

```python
window.add_image(path, row=None, column=None, columnspan=1, frame=None)
```

#### 参数

- **`path`**: 图片文件的路径。
- **`row`**: 图片所在的行（可选）。
- **`column`**: 图片所在的列（可选）。
- **`columnspan`**: 图片跨越的列数（可选），默认为 1。
- **`frame`**: 图片所在的帧（可选），默认为根帧。

#### 示例

```python
window.add_image('path/to/image.png', row=4, column=0, columnspan=2)
```

---

## 文件对话框 (`FileDialog`)

打开一个文件对话框（用于打开或保存文件）。

#### 初始化方法

```python
window.add_file_dialog(dialog_type='open', filetypes=(("All Files", "*.*"),), initialdir="/", title="Select a file")
```

#### 参数

- **`dialog_type`**: 对话框类型（`'open'` 或 `'save'`）。
- **`filetypes`**: 文件类型过滤器列表。
- **`initialdir`**: 初始目录。
- **`title`**: 对话框标题。

#### 示例

```python
file_path = window.add_file_dialog(dialog_type='open', filetypes=[("Text Files", "*.txt")])
```

