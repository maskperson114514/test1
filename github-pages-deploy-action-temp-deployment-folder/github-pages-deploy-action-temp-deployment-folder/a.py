# a.py 示例代码
import time
import os

def save_data():
    # 你的数据处理逻辑（例如生成或更新数据文件）
    with open("data.txt", "a") as f:
        f.write(f"Data updated at {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # 自动提交到GitHub
    os.system("git add data.txt")  # 添加文件到暂存区
    os.system("git commit -m 'Auto-update data'")  # 提交更改
    os.system("git push origin main")  # 推送到远程仓库

if __name__ == "__main__":
    save_data()
