import os
import platform
from img_exchange import *
from support import *
from ui import *

platform_info = platform.uname()
system = platform_info.system
architecture = platform_info.machine
pandoc_path = ''

print(f'平台信息: \n\t系统: {system}\n\t架构: {architecture}')


def convert():
    if root.file_path == '':
        root.add_log('未选择文件')
        return

    target_type = root.target_type_entry.get()
    if len(target_type) == 0 or target_type == '.':
        root.add_log('请输入正确的文件类型')
        return

    if target_type[0] != '.':
        target_type = '.' + target_type

    file_name, file_type = os.path.splitext(root.file_path)

    target_path = f'{file_name}{target_type}'

    root.add_log(f'开始转化: {root.file_path} -> {target_path}')
    root.update()

    # 选择文件类型并转化
    if target_type in image_type:
        result = image_convert(root.file_path, target_path)

    elif target_type in gif_type:
        result = to_gif(root.file_path, target_path)

    elif target_type in video_type:
        result = to_video(root.file_path, target_path)

    else:
        result = os.system(f'{pandoc_path} \'{root.file_path}\' -o \'{target_path}\'')

    # 判断目标路径是否有所想要的文件，以验证文件是否转化成功
    if os.path.exists(f'{target_path}'):
        root.add_log(text=f'转化成功。文件生成于: {target_path}')
        root.open_locally(target_path)
    else:
        root.add_log(text=f'转化失败。错误信息: \n{result}')


def initialize_pandoc():
    global pandoc_path
    # pandoc 路径设置
    if system == 'Darwin':
        # 苹果系统
        if os.path.exists('Resources/pandoc-MacOS/bin/pandoc'):
            pandoc_path = 'Resources/pandoc-MacOS/bin/pandoc'
        else:
            unzip('Resources/pandoc-MacOS.zip', 'Resources')
            os.system('chmod +x Resources/pandoc-MacOS/bin/pandoc')
            restart()

    elif system == 'win32':
        if os.path.exists('Resources/pandoc-Windows/pandoc.exe'):
            pandoc_path = 'Resources/pandoc-Windows/pandoc.exe'
        else:
            unzip('Resources/pandoc-Windows.zip', 'Resources')


if __name__ == '__main__':

    # 初始化 pandoc
    initialize_pandoc()

    # 初始化窗口
    root = main_window(system, convert, 'flatly')

    # 初始化 menubar
    init_menubar(root)

    root.mainloop()
