import sys
import os
import pip

# 目录设置
if os.path.splitext(sys.path[0])[1] == '.zip':
    os.chdir(os.path.split(sys.path[0])[0])

print(f'当前运行目录: {os.getcwd()}')

# 安装所需库
libs = ['PySide6', 'pypandoc', 'wget', 'moviepy', 'pillow']
pip.main(['install', *libs, '-i', 'https://pypi.tuna.tsinghua.edu.cn/simple'])

# 启动
import src

src.__init__()
