from moviepy.editor import VideoFileClip
import os

# path = r"D:\CoachAI-Projects-main\CoachAI-Projects-main\ShuttleSet\set"
path = r"D:\CoachAI-Projects-main\ShuttleSet\set"

def split_video_into_one_second_segments(video_path, output_dir):
    # 确保输出目录存在
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
   # 加载视频文件
    video = VideoFileClip(video_path)
    video_duration = int(video.duration)

    # 分割视频
    for i in range(0, video_duration, 1):
        # 获取一秒的视频段
        new_clip = video.subclip(i, i+1)

        # 输出文件的路径
        output_file = os.path.join(output_dir, f"{video_path}_{i}.mp4")

        # 写入文件
        new_clip.write_videofile(output_file, codec="libx264", audio_codec="aac")


for dir in os.listdir(path):
    if os.path.isdir(os.path.join(path, dir)):
        folder = os.path.join(path, dir)
        for file in os.listdir(folder):
            if file.endswith("mp4") and (file.startswith("A_") or file.startswith("B_")):
                video_path = os.path.join(folder, file)
                output_dir = folder
                split_video_into_one_second_segments(video_path, output_dir)

"""for file in os.listdir(path):
            if file.endswith("mp4") and (file.startswith("A_") or file.startswith("B_")):
                video_path = os.path.join(path, file)
                output_dir = path
                split_video_into_one_second_segments(video_path, output_dir)"""