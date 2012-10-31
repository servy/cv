# -*- coding: utf-8 -*-
import cv
 
fullColorImage = cv.LoadImage("../../Images/sos-dan.jpg")

grayscaleImage = cv.CreateImage((fullColorImage.width, fullColorImage.height), cv.IPL_DEPTH_8U, 1)
cv.CvtColor(fullColorImage, grayscaleImage, cv.CV_RGB2GRAY)

binaryImage = cv.CreateImage((fullColorImage.width, fullColorImage.height), cv.IPL_DEPTH_8U, 1)

# threshold binarization
threshold = 100
for i in xrange(binaryImage.height):
  for j in xrange(binaryImage.width):    
    if grayscaleImage[i,j] > threshold:
      binaryImage[i,j] = 255
    else:
      binaryImage[i,j] = 0

cv.ShowImage("fullcolor", fullColorImage)
cv.ShowImage("grayscale", grayscaleImage)
cv.ShowImage("binary", binaryImage)
cv.WaitKey()
cv.DestroyAllWindows()