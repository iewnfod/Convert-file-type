from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon
import os
from src.constants import *


class MainWindow(QMainWindow):
    def __init__(self, convert, *args, **kwargs):
        """
        初始化
        :param convert: 主转化函数
        """
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Convert File Type')
        self.file_path = ''
        self.system = SYSTEM
        self.convert = convert
        self.target_path = ''
        self.status = ''
        self.status_color = 'red'
        self.text_style = 'margin: 10px'

        # 加载 ui
        self._ui_init()
        # 加载 qss
        self._qss_init()

    def _ui_init(self):
        """
        初始化 ui
        """

        self.w = 500
        self.h = 305
        self.resize(self.w, self.h)
        self.setMinimumSize(self.w, self.h)
        self.setMaximumSize(self.w, self.h)
        # 文件选择
        self.get_file_path_bt = QPushButton('选择文件', self)
        self.get_file_path_bt.move(0, 5)
        self.get_file_path_bt.resize(460, 40)
        self.get_file_path_bt.clicked.connect(self.get_file_path)
        # 前往主页
        self.to_homepage_bt = QPushButton(self)
        self.to_homepage_bt.move(460, 5)
        self.to_homepage_bt.resize(40, 40)
        self.to_homepage_bt.setIcon(QIcon('Resources/github.ico'))
        self.to_homepage_bt.clicked.connect(self.to_homepage)
        # 目标类型，label
        self.target_file_enter_label = QLabel('目标文件类型: ', self)
        self.target_file_enter_label.move(10, 45)
        self.target_file_enter_label.resize(100, 30)
        # 目标类型，输入框
        self.target_file_entry = QLineEdit(self)
        self.target_file_entry.setPlaceholderText('.docx')
        self.target_file_entry.move(100, 50)
        self.target_file_entry.resize(100, 25)
        # 转化按钮
        self.convert_bt = QPushButton('开始转化', self)
        self.convert_bt.move(210, 42)
        self.convert_bt.resize(290, 40)
        self.convert_bt.clicked.connect(self.convert)
        # 日志区域
        self.log_area = QTextEdit(self)
        self.log_area.move(0, 85)
        self.log_area.resize(500, 220)
        self.log_area.setReadOnly(True)

        print('\033[1mFINISH LOADING UI\033[0m')

    def update_log(self):
        """
        向 stdout 以及 log_area 更新日志，修改日志文本

        :return: None
        """

        file_path = f'<span style="{self.text_style}">当前文件: {self.file_path}</span>'
        target_path = f'<span style="{self.text_style}">目标文件: {self.target_path}</span>'
        status = f'<span style="color: {self.status_color}; white-space: pre-wrap">{self.status}</span>'

        self.log_area.clear()
        if self.file_path:
            self.log_area.insertHtml(file_path)
            self.log_area.insertPlainText('\n\n')
        if self.target_path:
            self.log_area.insertHtml(target_path)
            self.log_area.insertPlainText('\n\n')
        if self.status:
            self.log_area.insertHtml(status)

        self.update()

    def get_file_path(self):
        """
        获取文件选择

        :return: None
        """

        path, _ = QFileDialog(self, '请选择文件').getOpenFileName()
        self.target_path = ''
        self.status = ''
        self.file_path = ''

        if path:
            if os.path.isfile(path):
                self.file_path = path
                self.update_log()
            else:
                self.status = f'未找到文件: {path}'
                self.update_log()

    def open_locally(self, path):
        """
        在本地打开

        :param path: 任何路径，可以是文件或者网址
        """
        if self.system == 'Darwin':
            os.system(f'open \'{path}\'')
        elif self.system == 'win32' or self.system == 'Windows':
            os.system(f'explorer file:\\\\\"{path}\"')

    def get_target_file_type(self):
        """
        获取目标文件类型

        :return: 文件类型 str
        """
        text = self.target_file_entry.text()
        return text if text else self.target_file_entry.placeholderText()

    def _qss_init(self):
        """
        初始化 qss
        """
        with open(os.path.join('src', 'main.qss'), 'r', encoding='UTF-8') as f:
            qss = f.read()
        self.setStyleSheet(qss)

        print('\033[1mFINISH LOADING QSS\033[0m')

    def to_homepage(self):
        self.open_locally('https://github.com/iewnfod/Convert-file-type/')
