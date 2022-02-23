from pytube import YouTube

# where to save
SAVE_PATH = "F:\yt-downloads"

link = input("Enter a YouTube Video Link: ")

try:
	yt = YouTube(link)
except:
	print("Connection Error") 

mp4files = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

yt.set_filename(input('Enter Filename: '))

d_video = yt.get(mp4files[-1].extension, mp4files[-1].resolution)
try:
	d_video.download(SAVE_PATH)
except:
	print("Error! Video could not be downloaded!")
print('Video has Successfully Downloaded!')
