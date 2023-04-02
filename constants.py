import os
import platform
from support import *

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
        os.chmod('ffmpeg/MacOS/ffmpeg', 777)
        os.environ['IMAGEIO_FFMPEG_EXE'] = 'ffmpeg/MacOS/ffmpeg'

    print('\033[1mFINISH LOADING FFMPEG\033[0m')


def initialize_pandoc():
    """
    初始化 pandoc。设置 pandoc 路径

    :return: None
    """

    global pandoc_path
    if system == 'Darwin':
        # 苹果系统
        if os.path.exists('Resources/pandoc-MacOS/bin/pandoc'):
            os.chmod('Resources/pandoc-MacOS/bin/pandoc', 777)
            pandoc_path = 'Resources/pandoc-MacOS/bin/pandoc'
        else:
            unzip('Resources/pandoc-MacOS.zip', 'Resources')
            initialize_pandoc()

    elif system == 'win32' or system == 'Windows':
        if os.path.exists('Resources/pandoc-Windows/pandoc.exe'):
            pandoc_path = os.path.join(os.getcwd(), 'Resources\\pandoc-Windows\\pandoc.exe')
        else:
            unzip('Resources/pandoc-Windows.zip', 'Resources')
            initialize_pandoc()

    print('\033[1mFINISH LOADING PANDOC\033[0m')
    print('Pandoc Path: ', pandoc_path)
