from moviepy.editor import VideoFileClip

def extract_audio_mp4_to_mp3(mp4_file, mp3_file):
    video = VideoFileClip(mp4_file)
    audio = video.audio
    audio.write_audiofile(mp3_file)
    # 关闭视频文件以释放资源
    video.close()


import ffmpeg

def extract_audio_ffmpeg_lib(mp4_file, mp3_file):
    stream = ffmpeg.input(mp4_file)
    stream = ffmpeg.output(stream.audio, mp3_file, format='mp3', **{'q:a': '0'})
    ffmpeg.run(stream)

if __name__ == "__main__":
    input_mp4 = "游子吟-孟郊(唐).mp4"   # 输入的MP4文件路径
    output_mp3 = "游子吟-孟郊(唐).mp3" # 输出的MP3文件路径
    extract_audio_ffmpeg_lib(input_mp4, output_mp3)
    #extract_audio_mp4_to_mp3(input_mp4, output_mp3)
    print(f"音频已成功提取到 {output_mp3}")
