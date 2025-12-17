import cv2 as cv
import numpy as np

def treshold_demo(image):
    dst = cv.GaussianBlur(image,(3,3),0)
    gray = cv.cvtColor(dst,cv.COLOR_BGR2GRAY)
    rest, binary = cv.threshold(gray,0,255,cv.THRESH_OTSU | cv.THRESH_BINARY)
    cv.imshow("binary",binary)
    return binary


def canny_demo(image):
    t = 100
    canny_output = cv.Canny(image,t,t*2)
    cv.imshow("canny_output",canny_output)
    return canny_output

src = cv.imread("/home/kiyran/Masaüstü/opencv/opencv-301/1.webp")
cv.namedWindow("input",cv.WINDOW_AUTOSIZE)
cv.imshow("input",src)
cv.waitKey(0)

binary = treshold_demo(src)

canny = canny_demo(src)

contours, hierarchy = cv.findContours(canny,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

for c in range(len(contours)):
    cv.drawContours(src,contours,c,(0,0,255),2,0)

cv.imshow("contours-demo",src)
cv.waitKey(0)