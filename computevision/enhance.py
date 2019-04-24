
import cv2

image_path='D:/Temp/DSC00179.JPG'
img = cv2.imread(image_path)
bgr = img.copy()
lab = cv2.cvtColor(bgr, cv2.COLOR_BGR2LAB)

lab_planes = cv2.split(lab)

gridsize = 8
clahe = cv2.createCLAHE(clipLimit=2.0,tileGridSize=(gridsize,gridsize))

lab_planes[0] = clahe.apply(lab_planes[0])

lab = cv2.merge(lab_planes)

bgr = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

img = cv2.resize(img,(960,540))
bgr = cv2.resize(bgr,(960,540))
cv2.imshow('ahe',bgr)
cv2.imshow('img',img)

blr = bgr.copy()
#blr = cv2.GaussianBlur(blr, (3, 3),0)
blr = cv2.boxFilter(blr, -1, (3,3))

cv2.imshow('blr',blr)
cv2.waitKey()