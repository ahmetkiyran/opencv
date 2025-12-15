import cv2 as cv
path= "/Users/ahmetkiyran/Desktop/opencv/labirent.jpg"

src = cv.imread(path)

cv.namedWindow("test2",cv.WINDOW_AUTOSIZE)

cv.imshow("test2",src)

cv.waitKey(1200)

#colormap -> resim için renk haritasını oluşturur.resmi zengileştirmeye yarar.
"""
COLORMAP_AUTUMN
COLORMAP_BONE
COLORMAP_WINTER
COLORMAP_OCEAN
COLORMAP_SUMMER
COLORMAP_PINK
COLORMAP_COOL
COLORMAP_JET
"""
dst = cv.applyColorMap(src,cv.COLORMAP_BONE)
cv.imshow("output",dst)
cv.waitKey(1200)

# resimler üstündeki renk iyileştirmeleri yapılıyor.






