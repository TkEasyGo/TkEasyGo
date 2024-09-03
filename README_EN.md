
# TkEasyGo

**TkEasyGo** is a simple cross-platform GUI generator designed to help developers quickly create basic graphical user interfaces. It is implemented based on `tkinter` and provides a range of basic controls and functionalities to make it easy for users to build simple application interfaces.

[中文版](README.md)

## File Structure
```
├── docs
│   ├── contact.md                # Contact Information
│   ├── contributing.md           # Contribution Guidelines
│   ├── controls.md               # Controls Usage Guide
│   ├── docs.md                   # Project Documentation Overview
│   ├── event_binding.md          # Detailed Explanation of Event Binding
│   ├── faq.md                    # Frequently Asked Questions
│   ├── getting_started.md        # Getting Started Guide
│   ├── installation.md           # Installation Guide
│   ├── license.md                # License Details
│   ├── README.md                 # Documentation Homepage
│   ├── styling.md                # Styling and Theme Settings Guide
│   └── window_operations.md      # Window Operations Guide
├── examples
│   ├── Combobox_app.py           # Example: Using the Combobox Control
│   ├── event_app.py              # Example: Handling Events
│   ├── label_app.py              # Example: Using the Label Control
│   ├── layout_app.py             # Example: Using Different Layout Management Features
│   ├── notebook_Slider_app.py    # Example: Using the Notebook and Slider Controls
│   ├── paned_window_test.py      # Example: Using the PanedWindow Control
│   ├── Progressbar_app.py        # Example: Using the Progressbar Control
│   ├── scrollbar_test.py         # Example: Using the Scrollbar Control
│   ├── separator_test.py         # Example: Using the Separator Control
│   ├── spinbox_test.py           # Example: Using the Spinbox Control
│   ├── tabbed_app.py             # Example: Using the Tabbed Control
│   └── treeview_test.py          # Example: Using the Treeview Control
|   └── test_components.py        # Example: Calendar, Color Picker, File Chooser, Alert Box, etc.
├── LICENSE                       # Project License File
├── README.md                     # Project Description File
├── setup.py                      # Installation Script with Library Dependencies and Setup
├── test.ipynb                    # Jupyter Notebook for Testing and Experimentation
├── tests
│   └── test_core.py              # Test File for Core Functionality
└── TkEasyGo
    ├── core.py                   # Core Implementation File, Defining Main Controls and Window Management Features
    ├── events.py                 # Event Handling Functionality
    ├── layout.py                 # Layout Management Functionality
    ├── platform.py               # Platform-Specific Functionality
    ├── simple_variable.py        # Simple Variable Management Functionality
    ├── simple_window.py          # Simple Window Implementation, Integrating Various Controls and Layouts
    ├── themes.py                 # Theme and Style Management Functionality
    ├── __init__.py               # Library Initialization File
    |── module                    # Module Folder
    └── __pycache__               # Compiled Python Bytecode Files
        ├── core.cpython-310.pyc
        ├── events.cpython-310.pyc
        ├── layout.cpython-310.pyc
        ├── platform.cpython-310.pyc
        ├── simple_variable.cpython-310.pyc
        ├── simple_window.cpython-310.pyc
        └── themes.cpython-310.pyc
```

## Supported Features

- **Label**: Displays static text.
- **Button**: Triggers events.
- **Textbox**: For input and display of text.
- **Checkbox**: Allows users to select or deselect an option.
- **Radiobutton**: Allows users to choose one option from multiple choices.
- **Combobox**: Provides a dropdown list for user selection.
- **Progressbar**: Visual control for displaying progress.
- **Slider**: Allows selection of a value within a range.
- **Notebook**: Provides multiple tabs to organize content.
- **Frame**: Used to organize and group other controls.

## Future Plans

- **Enhanced Theme Support**: Introducing more themes and styling options to improve the appearance and user experience.
- **Additional Controls**: Adding more controls such as calendar and chart controls to meet more complex application needs.
- **Improved Layout Management**: Providing more flexible layout options for better control over widget placement and size.
- **Performance Improvement**: Optimizing control performance to ensure smooth operation in larger applications.

## To-Do List

- **User Documentation**: Complete user manuals and developer documentation to assist users in better utilizing the library.
- **Example Applications**: Provide more example applications and tutorials to demonstrate various uses and functionalities of the library.
- **Bug Fixes**: Continuously fix known bugs and issues to enhance the library’s stability.
- **Community Support**: Establish community support channels to collect user feedback and respond promptly.

# TkEasyGo User Guide

**TkEasyGo** is a simplified cross-platform GUI generator based on `tkinter`, designed to help developers quickly create graphical user interfaces. This document will introduce how to install and use TkEasyGo, showcase some common usage examples, and provide tips and considerations.

## Installation

To install TkEasyGo, use `pip` from PyPI:

```sh
pip install TkEasyGo
```

## Quick Start

### Creating a Basic Window

The following example demonstrates how to create a simple window and add some basic controls:

```python
from TkEasyGo.core import SimpleWindow, SimpleVariable

def basic_app():
    # Create a window
    window = SimpleWindow(title="Basic TkEasyGo App", width=300, height=200)
    
    # Add a label
    window.add_label("Welcome to TkEasyGo!", row=0, column=0, columnspan=2)
    
    # Add a textbox
    textbox = window.add_textbox("Type here...", row=1, column=0, columnspan=2)
    
    # Add a button
    button = window.add_button("Submit", lambda: print("Submit clicked"), row=2, column=0, columnspan=2)
    
    # Add a checkbox
    checkbox_var = SimpleVariable()
    window.add_checkbox("Check me", checkbox_var, row=3, column=0)
    
    # Run the window
    window.run()

if __name__ == "__main__":
    basic_app()
```

### Control Introduction

#### Label

Used to display static text. Added via the `add_label` method.

```python
window.add_label("This is a label", row=0, column=0)
```

#### Button

Used to trigger events. Added via the `add_button` method.

```python
window.add_button("Click Me", lambda: print("Button clicked"), row=1, column=0)
```

#### Textbox

For input and display of text. Added via the `add_textbox` method.

```python
textbox = window.add_textbox("Default text", row=2, column=0)
```

#### Checkbox

Allows users to select or deselect an option. Added via the `add_checkbox` method.

```python
checkbox_var = SimpleVariable()
window.add_checkbox("Check me", checkbox_var, row=3, column=0)
```

#### Radiobutton

Allows users to choose one option from multiple choices. Added via the `add_radiobutton` method.

```python
radiobutton_var = SimpleVariable("1")
window.add_radiobutton("Option 1", "1", radiobutton_var, row=4, column=0)
```

#### Combobox

Provides a dropdown list for user selection. Added via the `add_combobox` method.

```python
combobox = window.add_combobox(["Option 1", "Option 2", "Option 3"], row=5, column=0)
```

#### Progressbar

Visual control for displaying progress. Added via the `add_progressbar` method.

```python
progressbar = window.add_progressbar(value=50, row=6, column=0, columnspan=2)
```

#### Slider

Allows selection of a value within a range. Added via the `add_slider` method.

```python
slider = window.add_slider(value=50, row=7, column=0, columnspan=2)
```

#### Notebook

Provides multiple tabs to organize content. Added via the `add_notebook` method.

```python
def tab1_content(window, frame):
    window.add_label("This is Tab 1", row=0, column=0, frame=frame)
    window.add_button("Button in Tab 1", lambda: print("Tab 1 Button clicked"), row=1, column=0, frame=frame)

def tab2_content(window, frame):
    window.add_label("This is Tab 2", row=0, column=0, frame=frame)
    window.add_button("Button in Tab 2", lambda: print("Tab 2 Button clicked"), row=1, column=0, frame=frame)

window.add_notebook({"Tab 1": tab1_content, "Tab 2": tab2_content}, row=8, column=0, columnspan=2)
```

## Event Binding

Events can be bound to controls using the `bind_event` method:

```python
window.bind_event('textbox', '<KeyRelease>', lambda event: print(f"Text changed to: {textbox.get()}"))
window.bind_event('button', '<Button-1>', lambda event: print("Button clicked"))
```

## Window Operations

### Setting Window Minimize, Maximize, and Restore Functions

`SimpleWindow` provides methods for window operations including maximize, minimize, and restore:

- **Maximize**: Use the `maximize()` method

 to switch the window to fullscreen mode.
- **Minimize**: Use the `minimize()` method to minimize the window to the taskbar.
- **Restore**: Use the `restore()` method to restore the window to its original size.

Example code:

```python
def window_operations_app():
    window = SimpleWindow(title="Window Operations App", width=400, height=300)
    
    # Add operation buttons
    window.add_button("Maximize", window.maximize, row=0, column=0)
    window.add_button("Minimize", window.minimize, row=1, column=0)
    window.add_button("Restore", window.restore, row=2, column=0)
    
    # Run the window
    window.run()

if __name__ == "__main__":
    window_operations_app()
```

## Common Questions

### How to Adjust the Style of Controls?

You can configure the style of controls using the `SimpleWindow`'s `configure_styles` method. For example:

```python
window.configure_styles('TButton', padding=6, relief="flat", background="#4CAF50", font=("Arial", 12))
```

### How to Contribute?

If you wish to contribute to TkEasyGo, you can submit Pull Requests via GitHub, or report issues and suggestions. We welcome contributions of all kinds.

## Contact Us

- **Email**: tkeasygo@gmail.com
- **GitHub**: [https://github.com/TkEasyGo/TkEasyGo](https://github.com/TkEasyGo/TkEasyGo)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

