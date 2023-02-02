import tkinter as tk
from tkinter import filedialog
import os
import platform

platform_info = platform.uname()
system = platform_info.system
architecture = platform_info.machine

print(f'平台信息: \n\t系统: {system}\n\t架构: {architecture}')

root = tk.Tk()
root.title('文件类型转化')
root.geometry('600x300')
root.minsize(600, 300)
root.maxsize(600, 300)

if system == 'Darwin':
    # 苹果系统
    pandoc_path = 'Resources/pandoc-MacOS/bin/pandoc'
elif system == 'win32':
    pandoc_path = 'Resources/pandoc-Windows/pandoc.exe'

class Entry(tk.Entry):
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

log_area = tk.Text(height=18, width=83)
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

    add_log(f'开始转化: {file_type} -> {target_type}')
    root.update()

    os.system(f'{pandoc_path} \'{file_path}\' -o \'{file_name}{target_type}\'')
    if os.path.exists(f'{file_name}{target_type}'):
        add_log(text=f'转化成功。文件生成于: {file_name}{target_type}')
        os.system(f'open {file_name}{target_type}')
    else:
        add_log(text='转化失败。请尝试安装或重新安装本地Pandoc')
        os.system('open https://github.com/jgm/pandoc/releases')

get_file_bt = tk.Button(root, text='选择文件', command=get_file)
get_file_bt.pack(fill='both')

log_area.pack(side='bottom', pady=(0, 1))

target_type_label = tk.Label(root, text='目标文件类型: ')
target_type_label.pack(side='left', padx=(1, 0))
target_type_entry = Entry(root, '.docx')
target_type_entry.pack(side='left')

convert_bt = tk.Button(root, text='开始转化', command=convert)
convert_bt.pack(side='left', expand=True, fill='both', pady=(.5, .5))

root.mainloop()
