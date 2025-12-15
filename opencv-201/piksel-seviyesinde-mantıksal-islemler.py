import cv2 as cv
import numpy as np

path = "/Users/ahmetkiyran/Desktop/opencv/"

# resim1 

src1 = np.zeros(shape=[400,400,3],dtype=np.uint8)
src1[100:200, 100:200, 1]= 255
src1[100:200, 100:200, 2]= 255
cv.imshow("input1",src1)
cv.waitKey(2800)

#resim2

src2 = np.zeros(shape=[400,400,3],dtype=np.uint8)
src2[150:250, 150:250, 2]= 255

cv.imshow("input2",src2)
cv.waitKey(2800)

"""
python RGB yi alfabetik bir şekilde kodlar o da şu şekilde olur:
0: B
1: G
2: R
"""
#and
dist1 = cv.bitwise_and(src1,src2)
cv.imshow("dist1",dist1)
cv.waitKey(2800)

#or

dist2 = cv.bitwise_or(src1,src2)
cv.imshow("dist2",dist2)
cv.waitKey(2800)

#xor
dist3 = cv.bitwise_xor(src1,src2)
cv.imshow("dist3",dist3)
cv.waitKey(2800)


#bitwise_not

src = cv.imread(path + "opencv_logo.png")
cv.namedWindow("input",cv.WINDOW_AUTOSIZE)
cv.imshow("input",src)
cv.waitKey(1)

dist = cv.bitwise_not(src)
cv.imshow("dist",dist)
cv.waitKey(3000)

"""
AND → ortak olanı al

OR → dolu olanı al

XOR → farklı olanı göster

NOT → tersini yap
"""

