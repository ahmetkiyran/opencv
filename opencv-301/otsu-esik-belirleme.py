# otsu tresholding -> görüntünün siyah veya beyaz olara tanımlanmasını sağlıyoruz


import cv2 as cv
import numpy as np

src = cv.imread("/home/kiyran/Masaüstü/opencv/opencv-301/1.webp")
cv.namedWindow("input",cv.WINDOW_AUTOSIZE)
cv.imshow("input",src)
cv.waitKey(0)

gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY)

ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY | cv.THRESH_OTSU)

h,w = src.shape[:2]

cv.imshow("binary",binary)
cv.waitKey(0)