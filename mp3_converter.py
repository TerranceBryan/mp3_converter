from pytube import YouTube
from moviepy.editor import *

#Get the video URL
video_url = input("Enter the URL: ")

#create a Youtube object and get the audio stream
tube = YouTube(video_url)

#Get the audio stream of the video
audio_stream = tube.streams.filter(only_audio=True).first()

#download the audio stream
audio_file = audio_stream.download()

#convert the audio file to mp3
audio = AudioFileClip(audio_file)
audio.write_audiofile(audio_file.replace(".mp4",".mp3"))

print("Conversion Completed!")
