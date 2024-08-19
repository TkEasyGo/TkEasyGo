import sys
import os

# 添加项目根目录到sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from TkEasyGo.core import SimpleWindow

def progressbar_app():
    # 创建窗口
    window = SimpleWindow(title="Progressbar Example", width=300, height=150)
    
    # 添加进度条
    progressbar = window.add_progressbar(value=50, row=0, column=0, columnspan=2)
    
    # 添加按钮以增加进度
    def increase_progress():
        new_value = min(progressbar["value"] + 10, 100)  # 增加10，但不超过100
        progressbar["value"] = new_value
        print(f"Progress: {new_value}%")
    
    window.add_button("Increase Progress", increase_progress, row=1, column=0, columnspan=2)
    
    # 运行窗口
    window.run()

if __name__ == "__main__":
    progressbar_app()

