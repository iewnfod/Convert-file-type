import os
import platform
from src.support import *
import pypandoc
import ssl
import wget

platform_info = platform.uname()
system = platform_info.system
architecture = platform_info.machine

print(f'平台信息: \n\t系统: {system}\n\t架构: {architecture}')


def initialize_ffmpeg():
    """
    初始化 ffmpeg ，为 moviepy 做准备

    :return: None
    """

    if system == 'Darwin':
        try:
            os.chmod('ffmpeg/MacOS/ffmpeg', 777)
        except Exception as err:
            print(err)
        os.environ['IMAGEIO_FFMPEG_EXE'] = 'ffmpeg/MacOS/ffmpeg'

    print('\033[1mFINISH LOADING FFMPEG\033[0m')


def install_pandoc():
    """
    安装 pandoc sdk
    """
    ssl._create_default_https_context = ssl._create_unverified_context
    # 下载安装，如果保存，就手动下载安装
    try:
        pypandoc.pandoc_download.download_pandoc()
    except:
        url, version = pypandoc.pandoc_download._get_pandoc_urls()
        if system == 'Darwin':
            wget.download(url['darwin'])
            url = url['darwin'].split('/')[-1]
            os.system(f'open \'{url}\'')

        elif system == 'win32' or system == 'Windows':
            wget.download(url['win32'])
            url = url['win32'].split('/')[-1]
            os.system(f'explorer file:\\\\\"{url}\"')

        else:
            print('Unsupported platform. ')
            exit(0)

def initialize_pandoc():
    """
    初始化 pandoc，下载 pandoc sdk

    :return: None
    """

    # 如果 pandoc 不存在，或者没有，就下载安装
    try:
        if not os.path.exists(pypandoc.get_pandoc_path()):
            install_pandoc()
    except:
        install_pandoc()

    print('\033[1mFINISH LOADING PANDOC\033[0m')


def __init__():
    initialize_ffmpeg()
    initialize_pandoc()
