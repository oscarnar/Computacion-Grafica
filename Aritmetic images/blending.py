import cv2
import numpy as np 
from matplotlib import pyplot as plt 

img = cv2.imread("sub_11.jpg")
img2 = cv2.imread("mul_4.jpg")

img2 = cv2.resize(img2, img.shape[1::-1])


h_img = np.size(img,0)
w_img = np.size(img,1)

x = 0.2

for i in range(w_img-1):
    for j in range(h_img-1):
        img[j,i] = x * img[j,i] + (1-x)*img2[j,i]

#cv2.imshow("blending",img)
cv2.imwrite("blending2.png",img)
cv2.waitKey(0)