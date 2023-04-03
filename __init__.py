import src
import sys
import os

if os.path.splitext(sys.path[0])[1] == '.zip':
    os.chdir(os.path.split(sys.path[0])[0])
src.__init__()
