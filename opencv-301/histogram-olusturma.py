#sayısal değerlerin dağılımını göstermek için kullanılan bir grafik yöntemidirç

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def custom_hist(gray):
    h,w =gray.shape
    hist = np.zeros([256],dtype=np.int32)
    for row in range(h):
        for col in range(w):
            pv = gray[row,col]
            hist[pv]+= 1
    
    y_pos = np.arange(0,250,1,dtype=np.int32)
    plt.bar(y_pos,hist,align="center",color="r",alpha=0.5)
    plt.xticks(y_pos,y_pos)
    plt.ylabel("Frequency")
    plt.title("Histogram")
    plt.show()

def img_hist(image):
    cv.imshow("input",image)
    color = ("blue","green","red")
    for i,color in enumerate(color):
        hist = cv.calcHist([image],[i],None,[256],[0,256])
        plt.plot(hist,color=color)
        plt.xlim([0,256])
    plt.show()

src = cv.imread("/home/kiyran/Masaüstü/opencv/opencv-201/labirent.jpg")

cv.namedWindow("input",cv.WINDOW_AUTOSIZE)
cv.imshow("input",src)
cv.waitKey(0)

gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
custom_hist(gray)
img_hist(src)
cv.destroyAllWindows()