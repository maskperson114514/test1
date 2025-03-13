# a.py 示例代码
import time
import os

def save_data():
    # 你的数据处理逻辑（例如生成或更新数据文件）
    with open("data.txt", "a") as f:
        f.write(f"Data updated at {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    
if __name__ == "__main__":
    save_data()
