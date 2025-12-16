import cv2 as cv

#HSV renk uzayı

img = cv.imread("/home/kiyran/Masaüstü/opencv/opencv-201/opencv_logo.png")
cv.namedWindow("rgb",cv.WINDOW_AUTOSIZE)
cv.imshow("rgb",img)
cv.waitKey(1000)

#RGB to GRAY

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)
cv.waitKey(1000)

#RGB to HSV
hsv= cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("hsv",hsv)
cv.waitKey(0)

