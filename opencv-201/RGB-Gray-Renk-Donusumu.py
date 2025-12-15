import cv2 as cv

path = "/Users/ahmetkiyran/Desktop/opencv/labirent.jpg"

img = cv.imread(path)
cv.namedWindow("colored",cv.WINDOW_AUTOSIZE)
cv.imshow("colored",img)

cv.waitKey(1200)

#cvtColor

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.imshow("Gray",gray)

cv.waitKey(1800)
# bu sayede resim artık gri tonlara döndü

# imwrite -> kayot yapmak istediğimizde kullanacağımız fonksiyon

cv.imwrite(path + "gray_color.png",gray)
cv.destroyAllWindows()

