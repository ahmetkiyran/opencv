import cv2 as cv
import numpy as np

path = "/Users/ahmetkiyran/Desktop/opencv/opencv_logo.png"

src = cv.imread(path)

print(src.shape)

# görüntünün değerleri (2048, 1662, 3)

# normalizasyon için önce resmi griye çevirelim

gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)
cv.waitKey(2000)

print(gray.shape) # renk gösterme derdi olmadığından (2048, 1662) bu değerlere geldi 

print(gray)

gray = np.float32(gray)
print(gray)

min_value,max_value,min_loc,max_loc =cv.minMaxLoc(gray)

print(min_value,max_value)
print(min_loc,max_loc)

means,stdev = cv.meanStdDev(gray)

print(means,stdev)

dst = np.zeros(gray.shape,dtype=np.float32)
cv.normalize(gray, dst=dst, alpha =0,beta=1.0,norm_type=cv.NORM_MINMAX)

print(dst)

print(np.uint8(dst*255))


min_value,max_value,min_loc,max_loc =cv.minMaxLoc(gray)

print(min_value,max_value)
print(min_loc,max_loc)

means,stdev = cv.meanStdDev(gray)

print(means,stdev)

cv.imshow("NORM_MINMAX",dst)
cv.waitKey(2000)

min_value,max_value,min_loc,max_loc =cv.minMaxLoc(dst)

print(min_value,max_value)
print(min_loc,max_loc)

means,stdev = cv.meanStdDev(dst)

print(means,stdev)