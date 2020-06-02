import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('add_1.jpg')
img2 = cv2.imread('add_2.jpg')

#Obtenemos el largo y ancho de la imagen original
height = np.size(img, 0)
width = np.size(img, 1)

#Aplicamos Contrast Stretching 
for i in range (width-1):
    for j in range (height-1):
        a,x,y = img[j,i]
        b,w,z = img2[j,i]
        temp = a/2 + b/2
        if(temp < 0):
            temp = 0
        if(temp > 255):
            temp = 255
        img[j,i] = temp

cv2.imshow('adicion', img)
cv2.waitKey(0)