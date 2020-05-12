import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('hist6.jpg')

#Mostramos la imagen original
cv2.imshow('oring', img)
cv2.waitKey(0)

#Obtenemos el largo, ancho y total de pixeles
height = np.size(img, 0)
width = np.size(img, 1)
totalPixel =  height * width

#Obtenemos el histograma
color = ('b','g','r')
for i, c in enumerate(color):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color = c)
    plt.xlim([0,256])

#Muestra el histograma
#plt.show()

#Calculamos Pn
pn = []
for i in range(0,256):
    pn.append(hist[i]/totalPixel)

#Calculamos Sn
sn = []
for i in range(256):
    sumP = 0
    for j in range(i+1):
        sumP += pn[j]
    sn.append(int(255*sumP))

#Cambiamos por los valores de Sn
for i in range (width-1):
    for j in range (height-1):
        b,g,r=img[j,i]
        img[j,i]=sn[b]

cv2.imshow('hist', img)
cv2.waitKey(0)