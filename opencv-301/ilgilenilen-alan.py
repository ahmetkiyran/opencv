import cv2 as cv
import numpy as np

# ROI region of interest 
# bir resimde ilgilenmek istediğim alan için kullanmamız gereken yapı
src = cv.imread("/home/kiyran/Masaüstü/opencv/opencv-201/kedi.png")



h,w = src.shape[:2]

img = src.copy()

roi = img[300:750,500:600,:]

print(roi.shape[:2])

cv.imshow("roi",roi)
cv.waitKey(0)

img[0:450,0:100,:] = roi

cv.imshow("img",img)
cv.waitKey(0)