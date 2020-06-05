import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("sub_1.jpg", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("sub_2.jpg", cv2.IMREAD_GRAYSCALE)

img = img.astype(int)
img2 = img2.astype(int)

height = np.size(img,0)
width = np.size(img,1)

valorMax = 1
valorMin = 255
for i in range(width-1):
    for j in range(height-1):
        a = img[j,i]
        q = img2[j,i]
        a = int(a/q) * 30
        if(a > valorMax):
            valorMax = a
        if(a < valorMin):
            valorMin = a
        img[j,i] = a

for i in range (width-1):
    for j in range (height-1):
        b = img[j,i]
        temp = (255/(valorMax-valorMin))+0
        img[j,i] = (img[j,i]-valorMin)*temp

img = img.astype(np.uint8)
cv2.imshow("Pixel division",img)
cv2.waitKey(0)