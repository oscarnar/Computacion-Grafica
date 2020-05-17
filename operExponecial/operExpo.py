import cv2
import numpy as np
from matplotlib import pyplot as plt

# Raice to the power operator (RTTOP)
# img para oper. exponecial, img2 para RTTPO, img3 para myOperator
img = cv2.imread('exp_5.jpg')
img2 = img
img3 = img

# Mostramos la imagen original
#cv2.imshow('oring', img)
#cv2.waitKey(0)

#Obtenemos el largo y ancho de la imagen original
height = np.size(img, 0)
width = np.size(img, 1)

# Constante C
c = 20

# Constante B, esta es la base
b = 1.01

# Aplicamos el operador exponencial
for x in range (width-1):
    for y in range (height-1):
        be,ge,re = img[y,x]
        # Calculamos el logaritmo
        temp = c * (pow(b,be) - 1)
        # Controlamos si pasa de 0 y 255 
        if(temp > 255):
            temp = 255
        if(temp < 0):
            temp = 0
        img[y,x] = temp

# TODO: Que tiene mayor costo computacional
# Si elevamos 1.001 a 255 o si 50 a 1.5?

cv2.imshow('Exponencial', img)
cv2.waitKey(0)

######### RAICE TO THE POWER OPERATOR ############

# Constante C
c = 0.05

# Constante R, este es el exponente
r = 1.5

# Aplicamos RTTPO
for x in range (width-1):
    for y in range (height-1):
        be,ge,re = img2[y,x]
        # Calculamos el RTTOP
        temp = c * (pow(be,r))
        # Controlamos si pasa de 0 y 255 
        if(temp > 255):
            temp = 255
        if(temp < 0):
            temp = 0
        img2[y,x] = temp

# Mostramos la imagen
cv2.imshow('Raice to the power operator', img2)
cv2.waitKey(0)
