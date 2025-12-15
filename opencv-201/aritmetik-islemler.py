import cv2 as cv
import numpy as np

path = "/Users/ahmetkiyran/Desktop/opencv/"

src1 = cv.imread(path + "test0.png")
src2 = cv.imread(path + "test1.png")

h , w , ch = src1.shape # yükseklik genişlik ve kanal sayısı bilgisini almak için shape fonksiyonunu kullandık

print("h , w , ch ", h,w,ch)

# add metodu 
add_result = np.zeros(src1.shape,src1.dtype) # Bu satır, src1 ile aynı boyutta ve aynı veri tipinde, içi tamamen 0’larla dolu yeni bir NumPy dizisi (yani görüntü) üretir.

cv.add(src1,src2,add_result)# iki resmi add_result a ekle dedim

cv.imshow("add_result",add_result)
cv.waitKey(2700)

#substract (çıkarma)

sub_result = np.zeros(src1.shape,src1.dtype)
cv.subtract(src1,src2,sub_result)

cv.imshow("sub_result",sub_result)

cv.waitKey(2800)

#multiply (çarpma)

multi_result = np.zeros(src1.shape,src1.dtype)
cv.multiply(src1,src2,multi_result)
cv.imshow("mutli_result",multi_result)
cv.waitKey(2800)

#divide (bölme)

divide_result = np.zeros(src1.shape,src1.dtype)
cv.divide(src1,src2,divide_result)
cv.imshow("divide_result",divide_result)
cv.waitKey(2800)

cv.destroyAllWindows()