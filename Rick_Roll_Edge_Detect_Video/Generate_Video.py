import cv2
import numpy as np
import glob
import re

img_array = []

# Folder containing images to convert to video
files = glob.glob('output/*.png')
# sort images by ascending number
# Images will be in order 1, 2, 3, 4, 5, 6 etc rather than 1, 10, 11, 2, 20, 21 etc
files = sorted(files, key=lambda x:float(re.findall("(\d+)",x)[0]))
for filename in files:
    try:
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)
    except:
        print(f"issue with {filename}")

# Generate a video at 6 frames per second
out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 6, size)

# Add each image as a frame to the video
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
