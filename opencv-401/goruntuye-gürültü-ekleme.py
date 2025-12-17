import cv2 as cv
import numpy as np

def add_salt_and_pepper_noise(image):
    h,w =image.shape[:2]
    nums = 10000
    rows = np.random.randint(0, h, nums, dtype=int)
    cols = np.random.randint(0, w, nums, dtype=int)

    for i in range(nums):
        if i%2 == 1:
            image[rows[i],cols[i]] = (255,255,255)
        else:
            image[rows[i],cols[i]] = (0,0,0)
    return image

src = cv.imread("/home/kiyran/Masaüstü/opencv/opencv-201/opencv_logo.png")

h,w = src.shape[:2]
copy = np.copy(src)

copy = add_salt_and_pepper_noise(copy)

result = np.zeros([h,w*2,3],dtype=src.dtype)
result[0:h,0:w,:] = src
result[0:h,w:2 * w,:] = copy

cv.imshow("input",result)
cv.waitKey(0)