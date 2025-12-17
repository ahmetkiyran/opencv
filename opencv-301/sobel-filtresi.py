# SOBEL OPERATOR

import cv2 as cv
import numpy as np

src = cv.imread("/home/kiyran/Masaüstü/opencv/opencv-201/opencv_logo.png")

h,w = src.shape[:2]

x_grad = cv.Sobel(src,cv.CV_32F,1,0)
y_grad = cv.Sobel(src,cv.CV_32F,0,1)

x_grad = cv.convertScaleAbs(x_grad)
y_grad = cv.convertScaleAbs(y_grad)



cv.imshow("x",x_grad)
cv.waitKey(0)

cv.imshow("y",y_grad)
cv.waitKey(0)

dst = cv.add(x_grad,y_grad,dtype=cv.CV_16S)
dst = cv.convertScaleAbs(dst)

cv.imshow("g",dst)
cv.waitKey(0)
