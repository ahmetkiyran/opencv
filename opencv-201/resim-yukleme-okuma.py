import cv2 as cv # opencv kütüphanesini yükledik ve ekledik

path = "/Users/ahmetkiyran/Desktop/opencv/kedi.png" #resim dosyasının yolunu ekledik

img = cv.imread(path) # bu da resmi okumak için

print(type(img))# resmin tipini öğrendik numpy array olması resim üzerinde değişiklikler yapabileceğimizi gösteriyor.

# nameWindow -> resimleri tutmak için bir pencere oluşturcaz

cv.namedWindow("test",cv.WINDOW_AUTOSIZE) # burada window_autosize ile resmi boyutlarında tutmuş oluyoruz.
# test adını biz verdik resmin adı test oldu
# imshow -> resimleri gösterme

cv.imshow("test",img)# test adındaki resmi ve img yolundaki fotoğrafı göster anlamında
cv.waitKey(1200) # beklet anlamında aslında ve 1 yerine 0 yazılsa sonsuza kadar bellekte tutacağı anlamına gelir.
# içine yazılacak sayı milisaniye cinsinden ne kadar açık tutulacağını söyler bize 

cv.destroyAllWindows() # bu da opencv içindeki tüm pencereleri kapatmak için yazmamız gereken pencere kodu 
