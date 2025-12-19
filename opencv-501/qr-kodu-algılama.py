import cv2 as cv
import numpy as np

path = ("/Users/ahmetkiyran/Desktop/opencv/opencv-501/QR_code_for_mobile_English_Wikipedia.png")

src = cv.imread(path)

gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY)

qrcoder = cv.QRCodeDetector()

codeinfo,points,straight_qrcode = qrcoder.detectAndDecode(gray)

print(points)

result = np.copy(src)
cv.drawContours(result,[np.int32(points)],0,(0,0,255),2)

print("qrcode information is: \n%s" %codeinfo)
