# -*- coding: utf-8 -*-
import cv2
import time

file = 'D:/Temp/214000703_214000703_tv_P1080_crf_161306_25474.mp4'
cap = cv2.VideoCapture(file)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print( 'width', width, 'height', height)

cap.set(cv2.CAP_PROP_POS_MSEC, 6966000)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('starwar-Denoising.avi', fourcc, 25.0, (width/2, height/2))

for i in range(5000):
    ret, frame = cap.read()  # 捕获一帧图像
    if ret:
        if i %100 ==0:
            print('\r%s'%i)

        begin = time.time()
        bgr = frame
        lab = cv2.cvtColor(bgr, cv2.COLOR_BGR2LAB)
        lab_planes = cv2.split(lab)

        gridsize = 8
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(gridsize, gridsize))

        lab_planes[0] = clahe.apply(lab_planes[0])

        lab = cv2.merge(lab_planes)

        bgr = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

        # denoise
        # bgr = cv2.fastNlMeansDenoisingColored(bgr)

        bgr = cv2.resize(bgr, (width/2, height/2))
        bgr = cv2.fastNlMeansDenoisingColored(bgr)
        cv2.imshow('video', bgr)

        end = time.time()
        diff = int((end - begin)*1000)
        wait = 1
        if diff < 40:
            wait = 40 - diff
        cv2.waitKey(wait)

        out.write(bgr)
    else:
        break

cap.release()
out.release()
