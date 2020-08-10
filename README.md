# Edge Detection Using Laplacian Kernel

This program carries out edge detection by applying an image convolution kernel to a grayscale version of the image provided.

Technically the Laplacian kernel is:  
[ 0 -1  0]  
[-1  4 -1]  
[ 0 -1  0]  

whereas the kernal I use is:  
[-1 -1 -1]  
[-1  8 -1]  
[-1 -1 -1]  
  
This is because the latter uses more input values and hence is a bit more robust to noise in the image.  
  
A guassian blur is also applied to smooth the image and make it less prone to noise in the image, this allows it to draw edges around larger objects and not draw edges around every single difference in the image. If you want to see lines for every single edge in the image then remove the line that adds the guassian blur.
