import cv2
import numpy as np

img = np.zeros((400,300,3), np.uint8)
img2 = cv2.rectangle(img, (100,100),(200,200),(0, 255, 255))
cv2.putText(img,'zhangyang',(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255))
cv2.imshow('img',img)
cv2.waitKey(0)
