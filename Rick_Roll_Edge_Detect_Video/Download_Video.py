import pytube

video = pytube.YouTube('Youtube-Video-Link-To-Download')
# Takes the first video stream option, usually 30fps
vid = video.streams.first()
# List of available stream options
print(vid)
vid.download()
# Video length in seconds
print(video.length)
