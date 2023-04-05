import zipfile
from src.constants import *
import os


def unzip(zip_path: str, save_path: str):
    """
    解压 zip

    :param zip_path: 压缩文件的路径
    :param save_path: 解压后文件保存路径
    """
    file = zipfile.ZipFile(zip_path)
    file.extractall(save_path)
    file.close()
