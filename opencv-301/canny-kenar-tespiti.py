#CANNY EDGE DETECTION

import cv2 as cv
import numpy as np

src = cv.imread("/home/kiyran/Masaüstü/opencv/opencv-301/1.webp")
cv.imshow("input",src)
cv.waitKey(0)

edge = cv.Canny(src,100,300)# treshold1 ve treshold2 parametrelerini tutuyor
cv.imshow("canny",edge)
cv.waitKey(0)