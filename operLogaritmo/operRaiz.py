import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('log_12.jpg')

#Mostramos la imagen original
cv2.imshow('oring', img)
cv2.waitKey(0)

#Obtenemos el largo y ancho de la imagen original
heightOri = np.size(img, 0)
widthOri = np.size(img, 1)

# Constante 20,70,120 el mejor fue 70
c = 50

# Aplicamos el operador raiz
for i in range (widthOri-1):
    for j in range (heightOri-1):
        b,g,r=img[j,i]
        # Calculamos el la raiz
        temp = c * np.sqrt(b)
        # Controlamos si pasa de 0 y 255 
        if(temp > 255):
            temp = 255
        if(temp < 0):
            temp = 0
        img[j,i] = temp

cv2.imshow('Raiz', img)
cv2.waitKey(0)