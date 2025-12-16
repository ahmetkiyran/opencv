import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def custom_hist(gray):

    h,w =gray.shape
    hist = np.zeros([256],dtype=np.int32)
    for row in range(h):
        for col in range(w):
            pv = gray[row,col]
            hist[pv]+= 1

src = cv.imread("/home/kiyran/Masaüstü/opencv/opencv-201/labirent.jpg")

gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
cv.imshow("input",gray)
cv.waitKey(0)

custom_hist(gray)
dst = cv.equalizeHist(gray)
cv.imshow("eh",dst)
cv.waitKey(0)

custom_hist(dst)