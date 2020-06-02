import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('add_10.jpg')
#img = img.astype(int)
img2 = cv2.imread('add_11.jpg')
#img2 = img2.astype(int)

#Obtenemos el largo y ancho de la imagen original
height1 = np.size(img, 0)
width1 = np.size(img, 1)
height2 = np.size(img2, 0)
width2 = np.size(img2, 1)
height = 0
width = 0
if(width1 > width2):
    width=width2 
else: width=width1

if(height1 > height2):
    height=height2
else: height=height1

#Aplicamos Contrast Stretching 
for i in range (width-1):
    for j in range (height-1):
        b1,g1,r1 = img[j,i]
        b2,g2,r2 = img2[j,i]
        b = b1/2 + b2/2
        g = g1/2 + g2/2
        r = r1/2 + r2/2
        if((b or g or r) < 0):
            temp = 0
        if((b or g or r) > 255):
            temp = 255
        img[j,i] = b,g,r

cv2.imshow('adicion', img)
cv2.waitKey(0)