"""
This program takes in an image, converts it to greyscale then applies an image
convolution kernal in order to detect edges in the image.
"""

import cv2
from PIL import Image
import numpy as np
import glob
import re

def edge_detection(img, row, col):
    """
    Function takes in a row and column number. (row, col) indicate the co-ordinates of the
    top right pixel in the 3x3 pixel matrix that the convolution kernal is to be
    applied to.
    """
    pixels = []
    for i in range(row, row + 3):
        for j in range(col, col + 3):
            try:
                pixels.append(img[i][j])
            except:
                # DEBUG
                print(f"row: {row}")
                print(f"col: {col}")

    # Multiply corresponding sections of pixel matrix and convolution kernal
    value = sum([x * y for x, y in zip(pixels, kernal)])
    # Multiply value by 1000 so that difference can be seen more clearly
    return value * 1000




count = 1
files = glob.glob('pics/*.jpg')
files = sorted(files, key=lambda x:float(re.findall("(\d+)",x)[0]))
for filename in files:
    try:
        image = cv2.imread(filename)
        # Apply guassian blur to smooth image and reduce noise in the image
        # image = cv2.GaussianBlur(image, (5,5), cv2.BORDER_DEFAULT)
        # Convert to greyscale for increased accuracy and simpler pixel representation
        grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        width, height = grey_image.shape

        # Modified laplacian kernal using more input values to be more robust to noise.
        kernal = [-1, -1, -1,
                  -1,  8, -1,
                  -1, -1, -1]


        edge_detect_image = []

        # width-2 and height-2 as (width, height) are the top right of a 3x3 pixel matrix
        # and ensures no index out of bounds exceptions
        for row in range(width - 2):
            image_row = []
            # inner loop creates a row of pixels in the final output
            for col in range(height - 2):
                value = edge_detection(grey_image, row, col)
                image_row.append(value)
            edge_detect_image.append(image_row)

        arr = np.array(edge_detect_image)
        image_out = Image.fromarray(arr)

        image_out.save(f'output/{count}.png')
        count+=1
    except:
        print(f"issue with {filename}")
