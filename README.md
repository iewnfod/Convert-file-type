# Convert-file-type

*tips: 我自己什么都没做，只是整合了一下几个可以用来转换文件类型的库以及工具，然后加了一个不怎么雅观的页面而已。*

~~我是调包侠，哈哈哈~~

## 安装与运行
下载zip，并解压
### MacOS
双击运行 ```exec``` 文件
若运行出错，请根据输出提示进行解决

若提示没有权限，请打开终端，进入项目目录并运行以下代码，再双击运行
```shell
chmod +x exec
```
若依旧出错，请打开系统偏好设置/系统设置 --> 隐私与安全性，仍要打开。

*其实这里我更加建议上网查询更加详细的教程，毕竟这里没办法讲得很清楚*

### Windows
手动运行 ```__init__.py``` 文件；
可在终端输入
```shell
# 进入项目，这里的目录(...)需要根据自己电脑的情况自行修改
cd ...\Convert-file-type
# 运行启动文件
python __init__.py
```
如果提示没有 python，请尝试 python3。
如果依旧没有，请查看 python sdk 路径是否包括在系统环境变量中，或重新安装 python，并在安装时选择将 python 加入到 PATH 中。

## 文件转化
基于的库:
* PyPandoc (这东西对pdf的支持挺迷的，除了pdf其他都可以用)
* PIL Image
* ffmpeg (暂不支持 Windows) (若已经自行安装了ffmpeg，可尝试)

***理论上***支持: 以上库的所有支持的文件类型

由于很多文件格式没有机会亲自尝试，因此暂不开放，若有需要可以修改 ```src/convert/``` 下的文件，在 ```..._type={...}``` 中添加自己想要的类型。 (请确保它们被以上库支持)

## GUI
* Qt: PySide6 - src/qtui.py
