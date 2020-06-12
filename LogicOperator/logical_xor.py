import cv2
import numpy as np


image1 = cv2.imread("log_3.png")
image2 = cv2.imread("log_4.png")


height = np.size(image1, 0)
width = np.size(image1, 1)

def logical_XOR(img1,img2,height,width):
    for i in range (width-1):
        for j in range (height-1):
            b,r,g = img1[j,i]
            temp1 = int((b+r+g)/3)
            x,y,z = img2[j,i]
            temp2 = int((x+y+z)/3)
            temp3 = bin(int(bin(temp1),2) ^ int(bin(temp2),2))
            img2[j,i] = int(temp3,2)
    cv2.imwrite('output_XOR.png',img2)

if __name__ == "__main__":
   logical_XOR(image1,image2,height,width)