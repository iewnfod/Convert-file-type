import os
from src.constants import *  # 所有常量，平台信息等
from src.convert import *
from src.support import *
from src.qtui import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import pypandoc


def convert():
    """
    进行转化的主函数，所有转化都会首先调用此函数，再根据类型被分配到不同的函数进行执行。

    :return: None
    """

    target_type = root.get_target_file_type()
    if len(target_type) == 0 or target_type == '.':
        root.status_color = 'red'
        root.status = '请输入正确的文件类型'
        root.update_log()
        return

    if target_type[0] != '.':
        target_type = '.' + target_type

    file_name, file_type = os.path.splitext(root.file_path)

    target_path = f'{file_name}{target_type}'

    result = ''

    if file_type != target_type:  # 如果不一样则需要转化

        root.target_path = target_path
        root.status_color = 'green'
        root.status = '正在转化...'
        root.update_log()

        # 选择文件类型并转化
        if target_type in image_type:
            result = image_convert(root.file_path, target_path)

        elif target_type in audio_video_type:
            result = to_audio_video(root.file_path, target_path)

        else:
            try:
                pypandoc.convert_file(source_file=root.file_path, to=target_type[1:], format=file_type[1:], outputfile=target_path)
            except Exception as err:
                result = err

    # 判断目标路径是否有所想要的文件，以验证文件是否转化成功
    if os.path.exists(f'{target_path}'):
        root.target_path = target_path
        root.status_color = 'green'
        root.status = '转化成功'
        root.update_log()
        root.open_locally(target_path)
    else:
        root.status_color = 'red'
        root.status = f'转化失败。\n{result}'
        root.update_log()


def main():
    """
    主函数

    :return: None
    """
    global app, root
    # 初始化软件
    app = QApplication([])
    icon = QIcon()
    icon.addPixmap(QPixmap('icon.icns'), QIcon.Normal, QIcon.Off)
    app.setWindowIcon(icon)
    app.setApplicationDisplayName('Convert File Type')
    app.setApplicationName('Convert File Type')
    # 初始化ui
    root = MainWindow(convert)
    # ui显示
    root.show()
    # 更新日志
    root.update_log()
    # 软件运行
    app.exec()
