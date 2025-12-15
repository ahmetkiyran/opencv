import cv2 as cv 
import numpy as np

path = "/Users/ahmetkiyran/Desktop/opencv/opencv_logo.png"

img = cv.imread(path)
cv.namedWindow("image_create",cv.WINDOW_AUTOSIZE)
cv.imshow("image_create",img)
cv.waitKey(2800)

m1 =np.copy(img)# resmi kopyaladık

m2 = img

img[100:500, 200:500, :] = 255
cv.imshow("m2",m2)
cv.waitKey(2800)

# resimle aynı boyutta 0 oluşturma -> tüm ekran siyah oldu 
m3 = np.zeros(img.shape,img.dtype)
cv.imshow("m3",m3)
cv.waitKey(2800)

m4 = np.zeros([512,512],np.uint8)
"""
np.zeros([512, 512])
→ 512 satır × 512 sütunluk bir matris üretir
→ İçindeki tüm değerler 0

np.uint8
→ Her piksel 8 bitlik unsigned integer
→ Değer aralığı: 0–255
→ OpenCV’nin görüntüyle konuştuğu ana dil
"""
cv.imshow("m4",m4)
cv.waitKey(2800)
# orijinal boyuttan daha küçük bir şekilde boyutlandırdık ve siyah yaptık

#gri yapmak 

m5 = np.zeros([512,512],np.uint8)
m5[:,:] = 127
cv.imshow("m5",m5)
cv.waitKey(2800)
"""siyah bir tuval alıp onu tek hamlede orta griye boyuyor."""

# 1. Siyah arka plan oluştur
img = np.zeros((512, 512, 3), np.uint8)

# 2. Daire çiz (merkez, yarıçap, renk, kalınlık)
center = (256, 256)
radius = 120
cv.circle(img, center, radius, (0, 255, 0), 2)

# 3. Yazıyı dairenin içine yaz
text = "bu bir daire"
font = cv.FONT_HERSHEY_SIMPLEX
font_scale = 0.8
thickness = 2

# Yazıyı ortalamak için boyutunu hesapla
(text_width, text_height), _ = cv.getTextSize(text, font, font_scale, thickness)
text_x = center[0] - text_width // 2
text_y = center[1] + text_height // 2

cv.putText(
    img,
    text,
    (text_x, text_y),
    font,
    font_scale,
    (255, 255, 255),
    thickness,
    cv.LINE_AA
)

# 4. Göster
cv.imshow("Daire", img)
cv.waitKey(0)
cv.destroyAllWindows()