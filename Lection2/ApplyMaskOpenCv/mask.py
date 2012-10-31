# -*- coding: utf-8 -*-
import cv
import numpy
 
fullColorImage = cv.LoadImage("../../Images/sos-dan.jpg")

grayscaleImage = cv.CreateImage((fullColorImage.width, fullColorImage.height), cv.IPL_DEPTH_8U, 1)
cv.CvtColor(fullColorImage, grayscaleImage, cv.CV_RGB2GRAY)

mask = cv.fromarray(numpy.array([
  [1 , 2, 1],
  [2, 4, 2],
  [1, 2, 1] ]) / 16.0)


result = cv.CreateImage((fullColorImage.width, fullColorImage.height), cv.IPL_DEPTH_8U, 1)

cv.Filter2D(grayscaleImage, result, mask, (1, 1))

cv.ShowImage("fullcolor", fullColorImage)
cv.ShowImage("grayscale", grayscaleImage)
cv.ShowImage("result", result)
cv.WaitKey()
cv.DestroyAllWindows()