import zipfile

def unzip(zip_path, save_path):
    file = zipfile.ZipFile(zip_path)
    file.extractall(save_path)
    file.close()
