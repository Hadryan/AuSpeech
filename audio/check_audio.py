from os import listdir


dir_path = "../MELD.Raw/train/train_splits/"
audio_path = "../data/train/"

video_list = sorted(listdir(dir_path))
audio_path = sorted(listdir(audio_path))
audio_path = [a[:-3] + "mp4" for a in audio_path] # change mp3 to mp4

remain_videos = [v for v in video_list if v not in audio_path]

print(len(remain_videos))