import cv2
import numpy as np
import matplotlib as plt
import math

def myAffineOld(src, M, weigth, height):
    A = [ [M[0][0],M[0][1]] , [M[1][0],M[1][1]] ]
    B = [ [M[0][2]] , [M[1][2]] ]
    img_out = np.zeros(src.shape)
    img_out = img_out.astype(np.uint8)
    for x in range (height):
        for y in range (weigth):
            array = np.array([x,y,1])
            temp = np.dot(M,array.transpose())
            #temp = np.dot(A,[[x],[y]]) + B
            axisX = int(temp[0])#temp[0][0])
            axisY = int(temp[1])#temp[1][0])
            if(axisX < weigth and axisY < height):
                img_out[axisX,axisY] = src[y,x]
    return img_out

def myAffine(src, M, weigth, height):
    A = np.array([ [M[0][0],M[0][1]] , [M[1][0],M[1][1]] ])
    B = np.array([ [M[0][2]] , [M[1][2]] ])
    img_out = np.zeros((weigth,height))
    for x in range (weigth):
        for y in range (height):
            Y = np.array([[x],[y]]) - B
            temp=np.dot(np.linalg.inv(A),Y)
            axisX = int(temp[0])#temp[0][0])
            axisY = int(temp[1])#temp[1][0])
            if(axisX < src.shape[0] and axisY < src.shape[1] and axisX >= 0 and axisY >= 0):
                img_out[x,y] = src[axisX,axisY]
    img_out = img_out.astype(np.uint8)
    return img_out

def rotationSimple(src,grado):
    w,h = src.shape 
    px = w/2 
    py = h/2
    teta = (np.pi/180)*grado
    seno = np.sin(teta)
    cose = np.cos(teta)
    b1 = (1-cose)*px - seno*py
    b2 = seno*px + (1-cose)*py
    M = np.float32([[ cose, seno, b1],[-(seno), cose, b2]])
    #return cv2.warpAffine(src,M,(src.shape[1],src.shape[0]))
    return myAffine(src,M,w,h)

def rotation(src,grado):
    w,h = src.shape
    teta = (np.pi/180)*grado
    seno = np.sin(teta)
    cose = np.cos(teta)
    nh = h*cose+ w*seno
    nw= w*cose+h*seno
    MP = np.float32([[ 1, 0, (nh-h)/2],[0, 1, (nw-w)/2]])
    px = w/2#nh/2 
    py = h/2#nw/2
    b1 = (1-cose)*px - seno*py +(nw/2) - px
    b2 = seno*px + (1-cose)*py + (nh/2) - py
    M = np.float32([[ cose, seno, b1],[-(seno), cose, b2]])
    return myAffine(src,M,int(nw),int(nh))

def getAffine(src,dst):
    A = np.zeros((3,2))
    Ones = np.ones((3,1))
    Zeros = np.zeros((3,3))
    src1= np.concatenate((src,Ones,Zeros),axis=1)
    src2= np.concatenate((Zeros,src,Ones),axis=1)
    A = np.concatenate((src1,src2),axis=0)
    B = np.float64([[dst[0,0]],[dst[1,0]],[dst[2,0]],[dst[0,1]],[dst[1,1]],[dst[2,1]]])
    X = np.zeros((6))
    cv2.solve(A,B,X)
    M = np.zeros((2,3))
    a = 0
    for i in range (2):
        for j in range(3):
            M[i,j] = X[a]
            a+=1
    return M

img = cv2.imread('lena.png', cv2.IMREAD_GRAYSCALE)
width, height = img.shape

src=[[2,1],[2,3],[4,5]]
dst=[[3,1],[2,3],[6,5]]
M = getAffine(np.array(src),np.array(dst))
print(M)
img_out = rotation(img,15)

cv2.imshow('affine', img_out)
cv2.waitKey(0)
