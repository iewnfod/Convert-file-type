from PIL import Image


# 图片转换 使用 PIL.Image
image_type = {
    '.jpg',
    '.jpeg',
    '.png',
    '.bmp',
    '.ppm',
    '.tiff',
    '.dds',
    '.dib',
    '.eps',
    '.ps',
    '.fit',
    '.fits',
    '.h5',
    '.hdf',
    '.icns',
    '.ico',
    '.im',
    '.jfif',
    '.jpe',
    '.j2c',
    '.j2k',
    '.jp2',
    '.jpc',
    '.jpf',
    '.jpx',
    '.msp',
    '.pcx',
    '.pbm',
    '.pgm',
    '.pnm',
    '.ppm',
    '.bw',
    '.rgb',
    '.rgba',
    '.sgi',
    '.wepg',
    '.tif',
    '.emf',
    '.wmf',
    '.xbm',
}

def image_convert(file_path: str, target_path: str):
    """
    转化图片类型，使用 PIL.Image。

    :param file_path: 原文件路径
    :param target_path: 保存目标文件路径
    """
    img = Image.open(file_path)

    try:
        img.convert('RGB').save(target_path)
        return True

    except Exception as err:
        return err
