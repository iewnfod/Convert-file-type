import tkinter as tk
from tkinter import filedialog
import json
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import os

class main_window(ttk.Window):
    def __init__(self, system, convert, themename, *args, **kwargs) -> None:
        super().__init__(themename=themename, *args, **kwargs)
        self.file_path = ''
        self.system = system
        self.title('文件类型转化')
        # self.iconbitmap('icon.icns')
        if self.system == 'Darwin':
            w, h = 600, 300
        elif self.system == 'Windows' or self.system == 'win32':
            w, h = 600, 545
        else:
            w, h = 600, 400
        self.geometry(f'{w}x{h}')
        self.minsize(w, h)
        self.maxsize(w, h)

        self.log_area = ttk.Text(height=14, width=65)
        self.log_area.config(state=tk.DISABLED)

        # 控件填充
        get_file_bt = ttk.Button(self, text='选择文件', command=self.get_file, bootstyle=(PRIMARY, OUTLINE))
        get_file_bt.pack(fill='both', padx=(1, 1))

        self.log_area.pack(side='bottom', pady=(0, 1))

        target_type_label = ttk.Label(self, text='目标文件类型: ')
        target_type_label.pack(side='left', padx=(2, 0))
        self.target_type_entry = Entry(self, '.docx')
        self.target_type_entry.pack(side='left', padx=(0, 1))

        convert_bt = ttk.Button(self, text='开始转化', command=convert, bootstyle=(PRIMARY, OUTLINE))
        convert_bt.pack(side='left', expand=True, fill='both', pady=(.5, .5), padx=(0, 1))


    def get_file(self):
        self.file_path = filedialog.askopenfilename(title='请选择文件', filetypes=[])
        self.add_log('已选中文件: '+self.file_path)


    def add_log(self, text):
        print(text)
        self.log_area.config(state=tk.NORMAL)
        self.log_area.insert(tk.END, str(text) + '\n\n')
        self.log_area.config(state=tk.DISABLED)


    def open_locally(self, path):
        if self.system == 'Darwin':
            os.system(f'open \'{path}\'')
        elif self.system == 'win32' or self.system == 'Windows':
            os.system(f'explorer file:\\\\\"{path}\"')


    def about_fn(self):
        with open('config.json', 'r') as f:
            info = json.loads(f.read())

        about = tk.Toplevel()
        about.title('About')
        if self.system == 'Darwin':
            w, h = 250, 100
        elif self.system == 'win32' or self.system == 'Windows':
            w, h = 500, 200
        else:
            w, h = 500, 300
        about.geometry(f'{w}x{h}')
        about.minsize(w, h)
        about.maxsize(w, h)

        version = info['version']
        title = info['title']
        author = info['author']

        title_label = tk.Label(about, text=title, font=('', 20))
        version_label = tk.Label(about, text=f'版本: {version}')
        author_label = tk.Label(about, text=f'作者: {author}')
        error_bt = ttk.Button(about, text='提交错误', command=self.issue, bootstyle=(PRIMARY, OUTLINE))

        title_label.pack(fill='both', pady=(5, 0))
        error_bt.pack(side='bottom', fill='both')
        version_label.pack(side='left', padx=(20, 20))
        author_label.pack(side='left', padx=(20, 20))

        about.mainloop()

    def issue(self):
        if self.system == 'Darwin':
            os.system('open https://github.com/iewnfod/Convert-file-type/issues')
        elif self.system == 'win32' or self.system == 'Windows':
            os.system('explorer https://github.com/iewnfod/Convert-file-type/issues')


def init_menubar(root:main_window):
    menubar = tk.Menu()
    root.config(menu=menubar)
    about_menu = tk.Menu(menubar)
    about_menu.add_command(label='About', command=root.about_fn)
    menubar.add_cascade(label='About', menu=about_menu)


class Entry(ttk.Entry):
    def __init__(self, master, placeholder, **kw):
        super().__init__(master, **kw)

        self.placeholder = placeholder
        self._is_password = True if placeholder == "password" else False

        self.bind("<FocusIn>", self.on_focus_in)
        self.bind("<FocusOut>", self.on_focus_out)

        self._state = 'placeholder'
        self.insert(0, self.placeholder)

    def on_focus_in(self, event):
        if self._is_password:
            self.configure(show='*')

        if self._state == 'placeholder':
            self._state = ''
            self.delete('0', 'end')

    def on_focus_out(self, event):
        if not self.get():
            if self._is_password:
                self.configure(show='')

            self._state = 'placeholder'
            self.insert(0, self.placeholder)
