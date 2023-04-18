import os
import requests
import time


cwd = os.getcwd()
update_data = []
update_time = 0


def get_files_modify_time(path):
    times = {}
    files = os.listdir(path)
    for file in files:
        times[file] = os.path.getmtime(os.path.join(path, file))
    return times


def check_update(old_time):
    global update_time, update_data
    if not update_time:  # 如果已经获取过 update time 了，那就没有必要再重新请求了
        api_url = 'https://api.github.com/repos/iewnfod/Convert-file-type'
        data = requests.get(api_url).json()
        if 'updated_at' not in data:  # 如果请求结果中没有 updated_at 表示请求失败了，返回 False，不进行更新
            return False

        update_data = data
        update_time = time.mktime(time.strptime(
            data['updated_at'], '%Y-%m-%dT%H:%M:%SZ'))
    if not old_time:
        old_time = update_time

    return update_time > old_time


def install_update():
    pass


def update():
    file = get_files_modify_time(cwd)
    for i in file:
        if check_update(file[i]):
            install_update()
            break
