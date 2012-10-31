# -*- coding: utf-8 -*-
import cv
 
fullColorImage = cv.LoadImage("../../Images/sos-dan.jpg")

grayscaleImage = cv.CreateImage((fullColorImage.width, fullColorImage.height), cv.IPL_DEPTH_8U, 1)
cv.CvtColor(fullColorImage, grayscaleImage, cv.CV_RGB2GRAY)

binaryImage = cv.CreateImage((fullColorImage.width, fullColorImage.height), cv.IPL_DEPTH_8U, 1)
cv.Threshold(grayscaleImage, binaryImage, 100, 255, cv.CV_THRESH_BINARY)

cv.ShowImage("fullcolor", fullColorImage)
cv.ShowImage("grayscale", grayscaleImage)
cv.ShowImage("binary", binaryImage)
cv.WaitKey()
cv.DestroyAllWindows()