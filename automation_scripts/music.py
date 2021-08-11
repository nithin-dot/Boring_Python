import librosa
import youtube_dl
from spleeter.separator import Separator
# Jupyter Notebook visualization functions
from IPython.display import Audio, display
from IPython.display import HTML
print("1")
url = "BPwZaQfoIbU" #@param {type:"string"}
embed_url = "https://www.youtube.com/embed/%s?rel=0&amp;controls=0&amp;showinfo=0" % (url)
HTML('<iframe width="560" height="315" src=' + embed_url + 'frameborder="0" allowfullscreen></iframe>')
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'example_song.wav'
}
print("1")
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download=False)
    status = ydl.download([url])
audio, rate = librosa.load('C:/Users/nithin/Desktop/temp/video/example_song.wav', sr=44100, mono=False)
display(Audio(audio[:, 0*rate:40*rate], rate=rate))
separator=Separate ("example_song.mp3") 
separator = Separator('spleeter:2stems')
separator = Separator('C:/Users/nithin/Desktop/temp/video/hello.mp3')