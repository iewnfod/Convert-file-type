from PIL import Image
import moviepy.editor as mp

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
def image_convert(file_path, target_path):
    img = Image.open(file_path)

    try:
        img.convert('RGB').save(target_path)
        return True

    except Exception as err:
        return err

gif_type = {
    '.gif'
}
def to_gif(file_path, target_path):
    clip = mp.VideoFileClip(file_path)

    clip.write_gif(target_path)

video_type = {
    '.mp4',
    '.wmv',
    '.rm',
    '.avi',
    '.flv',
    '.webm'
}
def to_video(file_path, target_path):
    clip = mp.VideoFileClip(file_path)

    clip.write_videofile(target_path)
