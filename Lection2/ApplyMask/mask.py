# -*- coding: utf-8 -*-
import cv
import numpy

def applyMaskToPixel(image, resimage, mask, pixel, center):
  r = 0
  maskSum = 0
  for i in xrange(mask.height):
    for j in xrange(mask.width):
      # координаты в маске - i, j
      # координаты в изображении?
      y = pixel[0] + (i - center[0])
      x = pixel[1] + (j - center[1])
      
      r += image[y, x] * mask[i, j]
      maskSum += mask[i,j]
  resimage[pixel] = r / maskSum
 
fullColorImage = cv.LoadImage("../../Images/sos-dan.jpg")

grayscaleImage = cv.CreateImage((fullColorImage.width, fullColorImage.height), cv.IPL_DEPTH_8U, 1)
cv.CvtColor(fullColorImage, grayscaleImage, cv.CV_RGB2GRAY)

mask = cv.fromarray(numpy.array([
  [1, 2, 1],
  [2, 4, 2],
  [1, 2, 1] ]))

result = cv.CreateImage((fullColorImage.width, fullColorImage.height), cv.IPL_DEPTH_8U, 1)

for i in xrange(1,result.height-1):
  for j in xrange(1,result.width-1):
    applyMaskToPixel(grayscaleImage, result, mask, (i, j), (1, 1))

cv.ShowImage("fullcolor", fullColorImage)
cv.ShowImage("grayscale", grayscaleImage)
cv.ShowImage("result", result)
cv.WaitKey()
cv.DestroyAllWindows()