import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("Akagami Shanks.jpg", 0)

cv2.imshow("default", image)

[h, w] = image.shape

maxValue = 0

for i in range(h):  # This is for found max color rate
    for j in range(w):
        if image[i, j] > maxValue:
            maxValue = image[i, j]

for i in range(h):  # This is for inverting
    for j in range(w):
        image[i, j] = maxValue - image[i, j]

cv2.imshow("last", image)
cv2.waitKey()
