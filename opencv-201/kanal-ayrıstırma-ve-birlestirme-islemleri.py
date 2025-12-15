import cv2 as cv
import numpy as np

path = "/Users/ahmetkiyran/Desktop/opencv/opencv_logo.png"

src = cv.imread(path)

#split

mv = cv.split(src)
mv[0][:,:] = 0

dist1 = cv.merge(mv)
cv.imshow("output1",dist1)  #B
cv.waitKey(3000)

mv = cv.split(src)
mv[1][:,:] = 0

dist2 = cv.merge(mv)
cv.imshow("output2",dist2)  #G
cv.waitKey(3000)

mv = cv.split(src)
mv[2][:,:] = 0

dist3 = cv.merge(mv)
cv.imshow("output3",dist3)  #R
cv.waitKey(3000)

"""
Bu kod, resmi BGR kanallarına ayırıyor, her seferinde bir rengi tamamen kapatıyor, sonra resmi yeniden 
birleştirip “mavi yok / yeşil yok / kırmızı yok” hallerini ayrı ayrı gösteriyor.
"""