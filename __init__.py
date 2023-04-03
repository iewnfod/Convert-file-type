import src
import sys
import os

# 目录设置
if os.path.splitext(sys.path[0])[1] == '.zip':
    os.chdir(os.path.split(sys.path[0])[0])

# 启动
src.__init__()
