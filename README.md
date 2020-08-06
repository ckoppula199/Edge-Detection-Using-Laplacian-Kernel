# Edge Detection Using Laplacian Kernel

This program carries out edge detection by applying an image convolution kernal to a grayscale version of the image provided.

Technically the Laplacian kernel is:  
[ 0 -1  0]  
[-1  4 -1]  
[ 0 -1  0]  

whereas the kernal I use is:  
[-1 -1 -1]  
[-1  8 -1]  
[-1 -1 -1]  
  
This is because the latter uses more input values and hence is a bit more robust to noise in the image. 
