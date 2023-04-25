import sys
import os
import pip
import importlib

# 目录设置
if os.path.splitext(sys.path[0])[1] == '.zip':
    os.chdir(os.path.split(sys.path[0])[0])

print(f'当前运行目录: {os.getcwd()}')

# 安装所需库
# (包名，导入名)
libs = [
    ('PySide6', 'PySide6'),
    ('pypandoc', 'pypandoc'),
    ('wget', 'wget'),
    ('ffmpeg-python', 'ffmpeg'),
    ('pillow', 'PIL')
]
for lib_name, import_name in libs:
    try:
        print(importlib.import_module(import_name))
    except:
        pip.main(['install', lib_name, '-i', 'https://pypi.tuna.tsinghua.edu.cn/simple'])

# 启动
import src

src.__init__()
