import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('contr2.jpg')

#Mostramos la imagen original
cv2.imshow('oring', img)
cv2.waitKey(0)

#Obtenemos el largo y ancho
height = np.size(img, 0)
width = np.size(img, 1)

#Aplicamos Contrast Stretching 
for i in range (width-1):
    for j in range (height-1):
        b,g,r=img[j,i]
        #Aqui sacamos la parte constante
        temp=(255/(140-55))+0
        #Aqui aplicamos la constante
        #Y modificamos el pixel
        img[j,i]=(img[j,i]-55)*temp


cv2.imshow('chica BW', img)
cv2.waitKey(0)

####################################

img2 = cv2.imread('contr2.jpg')

#Aqui agregamos un outliers a la imagen
for i in range (20):
    for j in range (20):
        img2[j,i]=0

cv2.imshow('chica BW con outlier', img2)
cv2.waitKey(0)

#Obtenemos el histograma
color = ('b','g','r')
for i, c in enumerate(color):
    hist = cv2.calcHist([img2], [i], None, [256], [0, 256])
    plt.plot(hist, color = c)
    plt.xlim([0,256])

#Muestra el histograma
plt.show()

#TODO Aqui falta aplicar con los limites
#Aplicamos Contrast Stretching limitado
for i in range (width-1):
    for j in range (height-1):
        b,g,r=img2[j,i]
        #Aqui sacamos la parte constante
        #c=140 y d=55 -> c=
        porcentaje=0#(140-55)*0.1
        d=133-porcentaje
        c=70+porcentaje
        temp=(255/(d-c))+0
        #Aqui aplicamos la constante
        #Y modificamos el pixel
        temp=(b-c)*temp
        if(temp>255):
            temp=255
        if(temp<0):
            temp=0
        img2[j,i]=temp


cv2.imshow('chica BW con limites', img2)
cv2.waitKey(0)

cv2.destroyAllWindows()
