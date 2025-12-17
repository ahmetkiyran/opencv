import cv2 as cv
import numpy as np

# bilateralFilter

src = cv.imread("/home/kiyran/Masaüstü/opencv/opencv-301/1.webp")
cv.namedWindow("input",cv.WINDOW_AUTOSIZE)
cv.imshow("input",src)
cv.waitKey(0)

h,w =src.shape[:2]

dst =cv.bilateralFilter(src,0,100,20)

result = np.zeros([h,w * 2,3],dtype=src.dtype)

result[0:h,0:w,:] =src
result[0:h,w:2  * w,:] =dst

cv.imshow("result",result)
cv.waitKey(0)