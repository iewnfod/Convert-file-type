import zipfile
import sys
import os

def unzip(zip_path, save_path):
    file = zipfile.ZipFile(zip_path)
    file.extractall(save_path)
    file.close()

def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)
