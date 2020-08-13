import cv2
import os

cam = cv2.VideoCapture('Name of Youtube Video Downloaded')

current_frame = 0

while True:
    no_error, frame = cam.read()
    if no_error:
        # Take one frame for every 5 frames of the video
        # Reduces 30fps video to 6fps
        # Less time spent on edge detection
        if current_frame % 5 == 0:
            name = f'pics/{current_frame}.jpg'
            print(f"saving {name}")
            cv2.imwrite(name, frame)
        current_frame += 1
    else:
        break

cam.release()
cv2.destroyAllWindows()
