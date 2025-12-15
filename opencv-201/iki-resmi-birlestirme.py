import cv2 as cv
import numpy as np

path1= "/Users/ahmetkiyran/Desktop/opencv/test0.png"
path2= "/Users/ahmetkiyran/Desktop/opencv/test1.png"

img1 = cv.imread(path1)
img2 = cv.imread(path2)

cv.imshow("img1",img1)
cv.waitKey(3000)
cv.imshow("img2",img2)
cv.waitKey(3000)

horizontal = np.hstack((img1,img2))
cv.imshow("img3",horizontal)
cv.waitKey(3000)
