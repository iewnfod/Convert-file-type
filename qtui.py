from PySide6.QtWidgets import *
from PySide6.QtGui import QAction
import os
import json
from constants import *

class main_window(QMainWindow):
    def __init__(self, convert, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Convert File Type')
        self.file_path = ''
        self.system = system
        self.convert = convert

        # 加载 ui
        self.ui_init()
        # 加载 menubar
        # self.menubar_init()  # 目前还有问题...
        # 加载 qss
        self.qss_init()

    def ui_init(self):
        self.w = 500
        self.h = 305
        self.resize(self.w, self.h)
        self.setMinimumSize(self.w, self.h)
        self.setMaximumSize(self.w, self.h)
        # 文件选择
        self.get_file_path_bt = QPushButton('选择文件', self)
        self.get_file_path_bt.move(0, 5)
        self.get_file_path_bt.resize(500, 40)
        self.get_file_path_bt.clicked.connect(self.get_file_path)
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
        self.log_area.setEnabled(False)

        print('\033[1mFINISH LOADING UI\033[0m')

    def add_log(self, text):
        print(text)
        self.log_area.setEnabled(True)
        self.log_area.insertPlainText(str(text) + '\n\n')
        self.log_area.setEnabled(False)
        self.update()

    def get_file_path(self):
        path = QFileDialog(self, '选择文件').getOpenFileUrl()[0].path()
        if os.path.isfile(path):
            self.file_path = path
            self.add_log(f'已选中文件: {self.file_path}')
        else:
            self.add_log(f'请正确选择文件')

    def open_locally(self, path):
        if self.system == 'Darwin':
            os.system(f'open \'{path}\'')
        elif self.system == 'win32' or self.system == 'Windows':
            os.system(f'explorer file:\\\\\"{path}\"')

    def menubar_init(self):
        about_action = QAction(text='About', parent=self)
        about_action.triggered.connect(about)

        menu = self.menuBar()
        main_menu = menu.addMenu('Main')
        main_menu.addAction(about_action)

        print('\033[1mFINISH LOADING MENUBAR\033[0m')

    def get_target_file_type(self):
        text = self.target_file_entry.text()
        return text if text else self.target_file_entry.placeholderText()

    def qss_init(self):
        with open('main.qss', 'r', encoding='UTF-8') as f:
            qss = f.read()
        self.setStyleSheet(qss)

        print('\033[1mFINISH LOADING QSS\033[0m')


class about_window(QMainWindow):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.setWindowTitle('About')

        self.system = system

        with open('config.json', 'r') as f:
            self.data = json.loads(f.read())

        self.ui_init()

    def ui_init(self):
        # 加载 qss
        with open('main.qss', 'r', encoding='UTF-8') as f:
            qss = f.read()
        self.setStyleSheet(qss)

        # main
        self.w = 200
        self.h = 150
        self.resize(self.w, self.h)
        self.setMaximumSize(self.w, self.h)
        self.setMinimumSize(self.w, self.h)

        # 标题
        self.title = QLabel('Convert File Type', self)
        self.title.setStyleSheet('font-size: 30px')
        self.title.move(0, 0)
        self.title.resize(200, 50)

        # 作者，版本
        self.author = QLabel(f'Author: {self.data["author"]}', self)
        self.version = QLabel(f'Version: {self.data["version"]}', self)
        self.author.move(0, 60)
        self.author.resize(100, 30)
        self.version.move(30, 60)
        self.version.resize(100, 30)

        # 提交错误
        self.issue_bt = QPushButton('提交错误', self)
        self.issue_bt.move(0, 100)
        self.issue_bt.resize(200, 40)
        self.issue_bt.clicked.connect(self.issue)

    def issue(self):
        if self.system == 'Darwin':
            os.system('open https://github.com/iewnfod/Convert-file-type/issues')
        elif self.system == 'win32' or self.system == 'Windows':
            os.system('explorer https://github.com/iewnfod/Convert-file-type/issues')

def about():
    pass
