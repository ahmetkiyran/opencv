import cv2 as cv
import numpy as np

capture = cv.VideoCapture("/Users/ahmetkiyran/Desktop/opencv/videoplayback.mp4")

# yükseklik genişlik fram count fps bilgisi

height =capture.get(cv.CAP_PROP_FRAME_HEIGHT)
width = capture.get(cv.CAP_PROP_FRAME_WIDTH)
count = capture.get(cv.CAP_PROP_FRAME_COUNT)
fps = capture.get(cv.CAP_PROP_FPS)

print(height,width,count,fps)

out =cv.VideoWriter("/Users/ahmetkiyran/Desktop/opencv/videoplayback.mp4",cv.VideoWriter_fourcc("d","ı","v","x"),15,
                    (int(width),int(height)),True)

while True:
    ret, frame = capture.read()

    if ret is True:
        cv.imshow("video-input",frame)
        out.write(frame)

        c = cv.waitKey(50)
        if c == 27:
            break
    else:
        break

capture.release()
out.release()