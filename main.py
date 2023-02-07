import tkinter as tk
from tkinter import filedialog
import os
import platform
from img_exchange import *
import json
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from support import *

platform_info = platform.uname()
system = platform_info.system
architecture = platform_info.machine

print(f'平台信息: \n\t系统: {system}\n\t架构: {architecture}')

root = ttk.Window(themename='flatly')
root.title('文件类型转化')
w, h = 600, 300
root.geometry(f'{w}x{h}')
root.minsize(w, h)
root.maxsize(w, h)

def issue():
    os.system('open https://github.com/iewnfod/Convert-file-type/issues')

def about_fn():
    with open('config.json', 'r') as f:
        info = json.loads(f.read())

    about = tk.Toplevel()
    about.title('About')
    w, h = 300, 150
    about.geometry(f'{w}x{h}')
    about.minsize(w, h)
    about.maxsize(w, h)

    version = info['version']
    title = info['title']
    author = info['author']

    title_label = tk.Label(about, text=title, font=('', 20))
    version_label = tk.Label(about, text=f'版本: {version}')
    author_label = tk.Label(about, text=f'作者: {author}')
    error_bt = ttk.Button(about, text='提交错误', command=issue, bootstyle=(PRIMARY, OUTLINE))

    title_label.pack(fill='both', pady=(5, 0))
    error_bt.pack(side='bottom', fill='both')
    version_label.pack(side='left', padx=(20, 20))
    author_label.pack(side='left', padx=(20, 20))

    about.mainloop()

def open_locally(path):
    if system == 'Darwin':
        os.system(f'open \'{path}\'')
    elif system == 'win32':
        os.system(f'\"{path}\"')

menubar = tk.Menu()
root.config(menu=menubar)
about_menu = tk.Menu(menubar)
about_menu.add_command(label='About', command=about_fn)
menubar.add_cascade(label='About', menu=about_menu)

pandoc_path = ''

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

    elif system == 'win32':
        if os.path.exists('Resources/pandoc-Windows/pandoc.exe'):
            pandoc_path = 'Resources/pandoc-Windows/pandoc.exe'
        else:
            unzip('Resources/pandoc-Windows.zip', 'Resources')

initialize_pandoc()

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

file_path = ''

log_area = ttk.Text(height=14, width=65)
log_area.config(state=tk.DISABLED)

def add_log(text):
    global log_area
    print(text)
    log_area.config(state=tk.NORMAL)
    log_area.insert(tk.END, str(text) + '\n\n')
    log_area.config(state=tk.DISABLED)

def get_file():
    global file_path
    file_path = filedialog.askopenfilename(title='请选择一个文件', filetypes=[])
    add_log('已选中文件: '+file_path)

def convert():
    if file_path == '':
        add_log('未选择文件')
        return

    target_type = target_type_entry.get()
    if len(target_type) == 0 or target_type == '.':
        add_log('请输入正确的文件类型')
        return

    if target_type[0] != '.':
        target_type = '.' + target_type

    file_name, file_type = os.path.splitext(file_path)

    target_path = f'{file_name}{target_type}'

    add_log(f'开始转化: {file_path} -> {target_path}')
    root.update()

    # 选择文件类型并转化
    if target_type in image_type:
        result = image_convert(file_path, target_path)

    elif target_type in gif_type:
        result = to_gif(file_path, target_path)

    elif target_type in video_type:
        result = to_video(file_path, target_path)

    else:
        result = os.system(f'{pandoc_path} \'{file_path}\' -o \'{target_path}\'')

    if os.path.exists(f'{target_path}'):
        add_log(text=f'转化成功。文件生成于: {target_path}')
        open_locally(target_path)
    else:
        add_log(text=f'转化失败。错误信息: \n{result}')

# 控件填充
get_file_bt = ttk.Button(root, text='选择文件', command=get_file, bootstyle=(PRIMARY, OUTLINE))
get_file_bt.pack(fill='both', padx=(1, 1))

log_area.pack(side='bottom', pady=(0, 1))

target_type_label = ttk.Label(root, text='目标文件类型: ')
target_type_label.pack(side='left', padx=(2, 0))
target_type_entry = Entry(root, '.docx')
target_type_entry.pack(side='left', padx=(0, 1))

convert_bt = ttk.Button(root, text='开始转化', command=convert, bootstyle=(PRIMARY, OUTLINE))
convert_bt.pack(side='left', expand=True, fill='both', pady=(.5, .5), padx=(0, 1))

root.mainloop()
