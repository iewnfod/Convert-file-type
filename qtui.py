from PySide6.QtWidgets import *
import os

class main_window(QMainWindow):
    def __init__(self, system, convert, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file_path = ''
        self.system = system
        self.convert = convert

        # 加载 ui
        self.ui_init()

    def ui_init(self):
        self.w = 500
        self.h = 300
        self.resize(self.w, self.h)
        self.setMinimumSize(self.w, self.h)
        self.setMaximumSize(self.w, self.h)
        # 文件选择
        self.get_file_path_bt = QPushButton('选择文件', self)
        self.get_file_path_bt.move(10, 0)
        self.get_file_path_bt.resize(480, 40)
        self.get_file_path_bt.clicked.connect(self.get_file_path)
        # 目标类型，label
        self.target_file_enter_label = QLabel('目标文件类型: ', self)
        self.target_file_enter_label.move(10, 40)
        self.target_file_enter_label.resize(100, 30)
        # 目标类型，输入框
        self.target_file_entry = QLineEdit(self)
        self.target_file_entry.setPlaceholderText('.docx')
        self.target_file_entry.move(110, 40)
        self.target_file_entry.resize(100, 30)
        # 转化按钮
        self.convert_bt = QPushButton('开始转化', self)
        self.convert_bt.move(220, 35)
        self.convert_bt.resize(270, 40)
        self.convert_bt.clicked.connect(self.convert)
        # 日志区域
        self.log_area = QTextEdit(self)
        self.log_area.move(10, 80)
        self.log_area.resize(480, 210)

    def add_log(message):
        pass

    def get_file_path(self):
        path = QFileDialog(self, '选择文件').getOpenFileUrl()
        if os.path.isfile(path):
            self.file_path = path
            self.add_log(f'已选中文件: {self.file_path}')
        else:
            self.add_log(f'请正确选择文件')

app = QApplication([])
w = main_window()
w.show()
app.exec()
