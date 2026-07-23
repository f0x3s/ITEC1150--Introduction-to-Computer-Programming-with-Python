import cv2
import numpy as np

def pixel_to_bool(img, x,y):
    return True if img[x][y] else False


img = cv2.imread('peppers.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]

cv2.imwrite('output.jpg', img) 

print(pixel_to_bool(img,5,35))