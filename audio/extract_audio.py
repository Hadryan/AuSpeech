import sys
from moviepy.editor import *
from os import listdir, walk
import time
from check_audio import remain_videos


dir_path = "../MELD.Raw/train/train_splits/"
audio_path = "../data/train/"

start = time.time()
video_list = listdir(dir_path) ## return a list of all files
# print(type(walk(dir_path))) ## return a generator
# video_list = remain_videos.copy() ## only convert the remained videos
gen = (dir_path + v for v in video_list)
not_process = []
for this_path in gen:
    # print(this_path)
    try:
        this_video = VideoFileClip(this_path)
        this_audio = this_video.audio
        to_path = f"{audio_path}{this_path.split('/')[-1][:-4]}.wav"
        # print(to_path)
        this_audio.write_audiofile(to_path)
    except:
        print("Cannot process this video:", this_path)
        not_process.append(this_path)

    
    
end = time.time()
print(end - start)
print(not_process)
