import os
import platform
from src.support import *
from pypandoc.pandoc_download import download_pandoc
import pypandoc
import ssl

platform_info = platform.uname()
system = platform_info.system
architecture = platform_info.machine
pandoc_path = ''

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


def initialize_pandoc():
    """
    初始化 pandoc，下载 pandoc sdk

    :return: None
    """

    ssl._create_default_https_context = ssl._create_unverified_context
    download_pandoc()


def __init__():
    initialize_ffmpeg()
    initialize_pandoc()
