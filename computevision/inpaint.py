# -*- coding: utf-8 -*-
# @Time    : 2019/3/15 11:08
# @Author  : ZhangYang
# @Email   : ian.zhang.88@outlook.com

# Python 2/3 compatibility
from __future__ import print_function

import sys
import numpy as np
import cv2 as cv

def main():
    #file = sys.argv[1]
    file = 'D:/Temp/delogotest/input.mp4'
    cap = cv.VideoCapture(file)

    width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    print( 'width', width, 'height', height)

    mark = np.zeros((height, width), np.uint8)
    mark[700:900,1400:1800] = 255
    # cv.imshow('frame', mark)
    # cv.waitKey(0)

    fourcc = cv.VideoWriter_fourcc(*'XVID')
    out = cv.VideoWriter('output2.avi', fourcc, 20.0, (1024, 576))

    for _ in range(1000):
        ret, frame = cap.read()  # 捕获一帧图像
        if ret:
            #print(frame.shape, mark.shape)
            #cv.INPAINT_TELEA cv.INPAINT_NS
            res_img = cv.inpaint(frame, mark, 3, cv.INPAINT_TELEA)
            blur_img = res_img[700:900,1400:1800]
            # for _ in range(5):
            #     blur_img = cv.boxFilter(blur_img, -1, (9,9))
            blur_img = cv.GaussianBlur(blur_img, (19, 19),30)
            res_img[700:900, 1400:1800]=blur_img
            res_img = cv.resize(res_img,(1024, 576))
            out.write(res_img)
            cv.imshow('frame', res_img)
            cv.imshow('blur',blur_img)
            cv.waitKey(1)
        else:
            break

    cap.release()
    out.release()

if __name__ == '__main__':
    main()

