# Convert-file-type

*tips: 我自己什么都没做，只是整合了一下几个可以用来转换文件类型的库以及工具，然后加了一个丑不垃圾的页面而已。*

## 文件转化
现已使用的库:
* Pandoc
* PIL Image
* Moviepy

**理论上**支持: 以上库的所有支持的文件类型

## UI
* Qt: PySide6 - qtui.py
* *原来使用的是 tkinter - ui.py , 后来改为了 Qt6*
* *ui.py 已经不可用，因为 main.py 中部分函数的调用已经为了适配 Qt 而修改了*
