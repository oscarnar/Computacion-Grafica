import cv2
import numpy as np


image1 = cv2.imread("log_3.png")
image2 = cv2.imread("log_4.png")

def logical_OR(img1,img2):
    image_output = np.bitwise_or(image1,image2)
    cv2.imwrite('output_or.png',image_output)


if __name__ == "__main__":
   logical_OR(image1,image2)