import ffmpeg

audio_video_type = {
    '.flv',
    '.mp3',
    '.ogg',
    '.raw',
    '.wav',
    '.m4a',
    '.gif',
    '.mp4'
}
def to_audio_video(file_path, target_path):
    try:
        stream = ffmpeg.input(file_path)
        stream = ffmpeg.output(stream, target_path)
        ffmpeg.run(stream)
        return True

    except Exception as err:
        return err
