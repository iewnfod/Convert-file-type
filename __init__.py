import sys
import os

# 目录设置
if os.path.splitext(sys.path[0])[1] == '.zip':
    os.chdir(os.path.split(sys.path[0])[0])

print(f'当前运行目录: {os.getcwd()}')

# 启动
import src

src.__init__()
