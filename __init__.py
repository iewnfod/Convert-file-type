import tkinter as tk
import platform

def init():
    import main

platform_info = platform.uname()

system = platform_info.system

if system == 'Darwin':
    w, h = 250, 100
elif system == 'win32' or system == 'Windows':
    w, h = 300, 150
else:
    w, h = 500, 300
starting_window = tk.Tk()
starting_window.geometry(f'{w}x{h}')
starting_window.title('Convert File Type')

tk.Label(starting_window, text='Convert File Type', font=('', 20)).pack(pady=10)
tk.Label(starting_window, text='Loading...').pack()

starting_window.update()

init()

starting_window.destroy()
