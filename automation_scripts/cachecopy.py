import os
import shutil
from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS,os
from moviepy.editor import *
import moviepy.editor as mp
from PIL import Image
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import traceback
import time
from time import sleep
y=0
z=0
w=0
crttime=0
for i in ["audio","clip","gif"]:
 count1=1
 source = f'C:/Users/nithin/Desktop/temp/{i}/'
 for file in os.listdir(source):
  if file.endswith('.mp3'):
     os.unlink(r"C:/Users/nithin/Desktop/temp/audio/"+ str(count1)+".mp3")
     count1=count1+1
     print(count1)
  if file.endswith('.mp4'):
     os.unlink(r""+source + str(count1)+".mp4")
     count1=count1+1
     print(count1)
source = r'C:/Users/nithin/Desktop/nithin/'
for file in os.listdir(source):
     if file.endswith('.mp3'):
        y=y+1
        original_path = source+ file
        shutil.copy(original_path,f'C:/Users/nithin/Desktop/temp/audio/{y}.mp3')
     if file.endswith('.mp4'):
       original_path =  VideoFileClip(source+ file)
       dur=  original_path.duration
       if (file.endswith('.mp4') & (dur < 600 )):
        for i in range(10):
          z=z+1
          original_path = source+ file
          shutil.copy(original_path,f'C:/Users/nithin/Desktop/temp/gif/{z}.mp4')
       else:
        w=w+1
        original_path = source+ file
        shutil.copy(original_path,f'C:/Users/nithin/Desktop/temp/clip/{w}.mp4')
thumbnail_dir = os.path.join(SAMPLE_INPUTS, "audio")
this_dir = os.listdir(thumbnail_dir)
filepaths = [os.path.join(thumbnail_dir, fname) for fname in this_dir if fname.endswith("mp3")]
directory = {}
for root, dirs, files in os.walk(thumbnail_dir):
   for fname in files:
      filepath = os.path.join(root, fname)
      try:
       key = float(fname.replace(".mp3", ""))
      except:
       key = None
      if key != None:
       directory[key] = filepath
new_path = []
for k in sorted(directory.keys()):
   filepath = directory[k]
   print(filepath)
   new_path.append(AudioFileClip(filepath))
clip= concatenate_audioclips(new_path)
clip.write_audiofile("C:/Users/nithin/Desktop/movie/cache/temp.mp3")
clips= VideoFileClip("C:/Users/nithin/Desktop/movie/cache/temp.mp3")
print("Audio duration"+clips.duration)
if (z):
    count2=1
    time=0
    thumbnail_dir = os.path.join(SAMPLE_INPUTS, "gif")
    audioclip =AudioFileClip("C:/Users/nithin/Desktop/movie/cache/temp.mp3")
    for this_dir in os.listdir(thumbnail_dir):
        clip = VideoFileClip(r"C:/Users/nithin/Desktop/temp/gif/"+ str(count2)+".mp4")
        time = time + clip.duration
        count2=count2+1
        if( round(time//60)>60):
          min=round(time//3600)*60 
          minutes = round(time//60)-min
        else:
           minutes = round(time//60)
    print(f"Total Duration: {round(time//3600)}:{minutes}:{round(time%60)}")
    filepaths = [os.path.join(thumbnail_dir, fname) for fname in this_dir if fname.endswith("mp4")]
    directory = {}
    for root, dirs, files in os.walk(thumbnail_dir):
            for fname in files:
                filepath = os.path.join(root, fname)
                try:
                    key = float(fname.replace(".mp4", ""))
                except:
                    key = None
                if key != None:
                    directory[key] = filepath
    new_path = []
    for k in sorted(directory.keys()):
            filepath = directory[k]
            new_path.append(VideoFileClip(filepath))
    clip= concatenate_videoclips( new_path,method="compose")
    new_audio = afx.audio_loop(audioclip, duration=clip.duration)
    clip.audio = new_audio
    clip.write_videofile("C:/Users/nithin/Desktop/movie/temp.mp4",preset='ultrafast',codec='libx264')
else:
    audioclip =AudioFileClip("C:/Users/nithin/Desktop/movie/cache/temp.mp3")
    clip= mp.VideoFileClip("C:/Users/nithin/Desktop/temp/clip/1.mp4")
    new_audio = afx.audio_loop(audioclip, duration=clip.duration)
    clip.audio = new_audio
    clip.write_videofile("C:/Users/nithin/Desktop/movie/temp.mp4",preset='ultrafast',codec='libx264')
  
