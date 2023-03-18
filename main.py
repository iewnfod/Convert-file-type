import os
from constants import *  # 所有常量，平台信息等
from img_exchange import *
from support import *
from qtui import *
from PySide6.QtWidgets import *


def convert():
    """
    进行转化的主函数，所有转化都会首先调用此函数，再根据类型被分配到不同的函数进行执行。

    :return: None
    """

    target_type = root.get_target_file_type()
    if len(target_type) == 0 or target_type == '.':
        root.add_log('请输入正确的文件类型')
        return

    if target_type[0] != '.':
        target_type = '.' + target_type

    file_name, file_type = os.path.splitext(root.file_path)

    target_path = f'{file_name}{target_type}'

    result = ''

    if file_type != target_type:  # 如果不一样则需要转化

        root.add_log(f'开始转化: {root.file_path} -> {target_path}')

        # 选择文件类型并转化
        if target_type in image_type:
            result = image_convert(root.file_path, target_path)

        elif target_type in gif_type:
            result = to_gif(root.file_path, target_path)

        elif target_type in video_type:
            result = to_video(root.file_path, target_path)

        else:
            if system == 'Darwin':
                result = os.system(f'{pandoc_path} \'{root.file_path}\' -o \'{target_path}\'')
            elif system == 'Windows' or system == 'win32':
                result = os.system(f'powershell; {pandoc_path} \'{root.file_path}\' -o \'{target_path}\'')

    # 判断目标路径是否有所想要的文件，以验证文件是否转化成功
    if os.path.exists(f'{target_path}'):
        root.add_log(text=f'转化成功。文件生成于: {target_path}')
        root.open_locally(target_path)
    else:
        root.add_log(text=f'转化失败。错误信息: \n{result}')


def initialize_pandoc():
    """
    初始化 pandoc，设置 pandoc 路径

    :return: None
    """

    global pandoc_path
    if system == 'Darwin':
        # 苹果系统
        if os.path.exists('Resources/pandoc-MacOS/bin/pandoc'):
            pandoc_path = 'Resources/pandoc-MacOS/bin/pandoc'
        else:
            unzip('Resources/pandoc-MacOS.zip', 'Resources')
            os.system('chmod +x Resources/pandoc-MacOS/bin/pandoc')
            initialize_pandoc()

    elif system == 'win32' or system == 'Windows':
        if os.path.exists('Resources/pandoc-Windows/pandoc.exe'):
            pandoc_path = os.path.join(os.getcwd(), 'Resources\\pandoc-Windows\\pandoc.exe')
        else:
            unzip('Resources/pandoc-Windows.zip', 'Resources')
            initialize_pandoc()

    print('\033[1mFINISH LOADING PANDOC\033[0m')
    print('Pandoc Path: ', pandoc_path)


if __name__ == '__main__':
    # 初始化 pandoc
    initialize_pandoc()
    # 初始化软件
    app = QApplication([])
    # 初始化ui
    root = MainWindow(convert)
    # ui显示
    root.show()
    # 软件运行
    app.exec()
