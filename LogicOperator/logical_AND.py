import cv2
import numpy as np


image1 = cv2.imread("log_3.png")
image2 = cv2.imread("log_4.png")

def logical_AND(img1,img2):
    image_output = np.bitwise_and(image1,image2)
    cv2.imwrite('output_and.png',image_output)


if __name__ == "__main__":
   logical_AND(image1,image2)






