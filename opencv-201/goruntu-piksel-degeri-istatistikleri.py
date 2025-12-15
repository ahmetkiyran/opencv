import cv2 as cv
import numpy as np

path = "/Users/ahmetkiyran/Desktop/opencv/opencv_logo.png"

src = cv.imread(path,cv.IMREAD_GRAYSCALE)

#minMaxLocation

min_value,max_value,min_loc,max_loc =cv.minMaxLoc(src)

print(min_value,max_value)
print(min_loc,max_loc)

#meanStdDev

means,stdev = cv.meanStdDev(src)

print(means,stdev)

src[np.where(src<means)] = 0
src[np.where(src>means)] = 255

cv.imshow("binary",src)
cv.waitKey(4000)
