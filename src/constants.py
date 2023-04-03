import os
import platform
from src.support import *

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
