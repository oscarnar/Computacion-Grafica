import cv2
import numpy as np
import matplotlib as plt

def myAffine(src, M, weigth, height):
    A = [ [M[0][0],M[1][0]] , [M[0][1],M[1][1]] ]
    B = [ [M[0][2]] , [M[1][2]] ]
    img_out = np.zeros(src.shape)
    img_out = img_out.astype(np.uint8)
    for y in range (height):
        for x in range (weigth):
            temp = np.dot(A,[[x],[y]]) + B
            axisX = int(temp[0][0])
            axisY = int(temp[1][0])
            if(axisX < weigth and axisY < height):
                img_out[axisX,axisY] = src[x,y]
    return img_out

def zoom(src, incremento):
    width, height = src.shape
    newWidth = int(width * incremento)
    newHheight = int(height * incremento)
    img_out = np.zeros((newWidth,newHheight))
    
    A = [[incremento,0],[0,incremento]]
    pasos = int(incremento)
    interpo = incremento-1
    for y in range (height):
        for x in range (width):
            temp = np.dot(A,[[x],[y]])
            axisX = int(temp[0][0])
            axisY = int(temp[1][0])
            img_out[axisX,axisY] = src[x,y]

            act = img_out[axisX,axisY]
            hor = img_out[axisX-incremento,axisY]
            ver = img_out[axisX,axisY-incremento]
            supIz = img_out[axisX-interpo,axisY-incremento]
            for i in range (incremento):
                axisX -= i
                axisY -= i
                for j in range (incremento-i,0,-1):
                    #### Tipo Blending
                    x = j/incremento
                    #img_out[axisX,axisY-j] = (1-x)*supIz + x*ver#(ver+act)/2#
                    #img_out[axisX-j,axisY] = (1-x)*supIz + x*hor#(hor+act)/2#
                    #img_out[axisX-j,axisY-j] = (1-x)*supIz + x*act #(supIz+act)/2#
                    #### Promedio entre pixeles
                    img_out[axisX,axisY-j] = (ver+act)/2#
                    img_out[axisX-j,axisY] = (hor+act)/2#
                    img_out[axisX-j,axisY-j] = (supIz+act)/2#                                 

    img_out = img_out.astype(np.uint8)
    return img_out

img = cv2.imread('contr2.jpg', cv2.IMREAD_GRAYSCALE)
width, height = img.shape

# Shear
#M = np.float32([[ 1, 0.25, 0],[0.25, 1, 0]])
# Rotate
teta = 180
seno = np.sin(teta)
cose = np.cos(teta)
b1 = (1-cose)*width - seno*height
b2 = seno*width + (1-seno)*height
M = np.float32([[ cose, seno, b1],[-(seno), cose, b2]])
# Traslación
#M = np.float32([[ 1, 0, 10],[0, 1, 20]])
# Escala
#M = np.float32([[ 1.5, 0, 0],[0, 2, 0]])

#M = np.float32([[ 0.5, 0.5, 0],[0.5, 1, 0]])

#img_out = myAffine(img,M,width,height)
#img_out = zoom(img,3)

img_out = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

cv2.imshow('affine', img_out)
cv2.waitKey(0)