import cv2 as cv
import numpy as np

path = ("/Users/ahmetkiyran/Desktop/opencv/opencv_logo.png")

src = cv.imread(path)

# x flip 0 x olur

dist1 = cv.flip(src,0)# flip döndürme 
cv.imshow("x-flip",dist1)
cv.waitKey(0)

# y flip 1 y olur 

dist2 = cv.flip(src,1)# flip döndürme 
cv.imshow("y-flip",dist2)
cv.waitKey(0)

# xy flip -1 de hem x hem de y olur 

dist3 = cv.flip(src,-1)# flip döndürme 
cv.imshow("y-flip",dist3)
cv.waitKey(0)




