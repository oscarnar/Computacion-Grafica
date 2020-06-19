import cv2
import numpy as np
import matplotlib as plt

def resta(img1, img2):
    height = np.size(img1, 0)
    width = np.size(img1, 1)
    for i in range(width-1):
        for j in range(height-1):
            a = img1[j, i]
            b = img2[j, i]
            img1[j, i] = abs(a-b)
    return img1


def suma(img1, img2):
    height = np.size(img1, 0)
    width = np.size(img1, 1)
    for i in range(width-1):
        for j in range(height-1):
            a = img1[j, i]
            b = img2[j, i]
            temp = abs(a/2 + b/2)
            if(temp > 255):
                temp = 255
            img1[j, i] = temp
    return img1


def logical_OR(img1, img2):
    image_output = np.bitwise_or(img1, img2)
    return image_output

def adaptative(img, d, c):
    img_out = img
    img = img.astype(int)
    width,height = img.shape
    for i in range(width):
        for j in range(height):
            act = img[i, j]
            yes = i-d
            equis = j-d
            yesAum = i + d
            equisAum = j + d
            if(yes < 0):
                yes = 0
            if(equis < 0):
                equis = 0
            if(equisAum > height - 1):
                equisAum = height - 1
            if(yesAum > width - 1):
                yesAum = width - 1
            crop_img = img[yes:yesAum, equis:equisAum]
            prom = np.mean(crop_img) - c
            if(act > prom):
                img_out[i, j] = 255
            else:
                img_out[i, j] = 0
    return img_out


def division(img, img2):
    valorMax = 1
    valorMin = 255
    img_out = img
    img = img.astype(float)
    height = np.size(img,0)
    width = np.size(img,1)
    for i in range(width-1):
        for j in range(height-1):
            a = img[j, i]
            q = img2[j, i]
            a = a/q
            if(a>255):
                a = 255
            if(a > valorMax):
                valorMax = a
            if(a < valorMin):
                valorMin = a
            img[j, i] = a
    for i in range(width-1):
        for j in range(height-1):
            b = img[j, i]
            temp = (255/(valorMax-valorMin))+0
            img_out[j,i] = int((img[j,i]-valorMin)*temp)
    return img_out

def divisionWithoutSca(img, img2):
    height = np.size(img,0)
    width = np.size(img,1)
    for i in range(width-1):
        for j in range(height-1):
            a = img[j, i]
            q = img2[j, i]
            temp = (a/q)*20
            if(temp > 255):
                temp = 255
            img[j, i] = int(temp)
    return img

def multiplicationEsca(img,const):
    height = np.size(img,0)
    width = np.size(img,1)
    for i in range(width-1):
        for j in range(height-1):
            a = img[j,i] * const
            if(a > 255):
                a = 255
            img[j,i] = a
    return img


img = cv2.imread('paper6.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('paper7.jpg', cv2.IMREAD_GRAYSCALE)
width, height = img.shape
img2 = cv2.resize(img2, (height,width))

# First option threshol
#c = 2
#d = 5
#img_out = adaptative(img, d, c)
#img_out = logical_OR(img_out, img)

# Second option div
#img_out = division(img,img2)
#ter,img_out = cv2.threshold(img_out,130,255,cv2.THRESH_BINARY)

# Tercera opcion resta
#img_out = resta(img2,img)
#img_out = logical_OR(img_out, img)

# Best option
c = 2
d = 5
img_out = divisionWithoutSca(img,img2)
img_out = multiplicationEsca(img_out,5)
ter,img_out = cv2.threshold(img_out,89,255,cv2.THRESH_BINARY)
img_out1 = adaptative(img, d, c)
img_out = logical_OR(img_out,img_out1)

cv2.imshow('lena', img_out)
cv2.waitKey(0)