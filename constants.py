import platform

platform_info = platform.uname()
system = platform_info.system
architecture = platform_info.machine
pandoc_path = ''

print(f'平台信息: \n\t系统: {system}\n\t架构: {architecture}')
