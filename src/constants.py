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


min_width = float('inf')

def draw_bar(current, total, width=80):
    global min_width
    if current == -1 or total == -1:
        return
    msg = f' {current} / {total}'
    width -= len(msg) - 5
    min_width = min(width, min_width)
    percent = int(current / total * min_width)
    text = '[' + '\033[92m─\033[0m'*percent + '─'*(min_width - percent) + ']' + msg
    print('\r' + text + ' ' * (width - len(text)), end='')


def install_pandoc():
    """
    安装 pandoc sdk
    """
    ssl._create_default_https_context = ssl._create_unverified_context
    # 下载安装，如果保存，就手动下载安装
    print('Getting Pandoc SDK...')
    url, version = pypandoc.pandoc_download._get_pandoc_urls()
    if system == 'Darwin':
        name = url['darwin'].split('/')[-1]
        if not os.path.exists(name):
            wget.download(url['darwin'], bar=draw_bar)
            print()
        os.system(f'open \'{name}\'')

    elif system == 'win32' or system == 'Windows':
        name = url['darwin'].split('/')[-1]
        if not os.path.exists(name):
            wget.download(url['win32'], bar=draw_bar)
            print()
        print(f'If the install file does not start automatically, please start it by yourself: {name}')
        os.startfile(name)

    else:
        print('Unsupported platform. ')
        exit(0)

def getPATH():
    path = set()
    for i in os.environ['PATH'].split(':'):
        if not os.path.exists(i):
            continue
        files = os.listdir(i)
        for file in files:
            if os.path.isfile(os.path.join(i, file)):
                path.add(file)

    return path

def initialize_pandoc():
    """
    初始化 pandoc，下载 pandoc sdk

    :return: None
    """

    # 如果 pandoc 不存在，或者没有，就下载安装
    try:
        if pypandoc.get_pandoc_path() not in getPATH():
            install_pandoc()
    except:
        install_pandoc()

    print('\033[1mFINISH LOADING PANDOC\033[0m')


def __init__():
    initialize_ffmpeg()
    initialize_pandoc()
