import cv2
import numpy as np
from matplotlib import pyplot as plt

photo1 = cv2.imread("img.jpg", 0)

histogram = [0]*256 #I created an array that have all element values 0 and length 255

[h, w] = photo1.shape

for i in range(h):
    for j in range(w):
         value = photo1[i, j] #This value is intensity of color
         histogram[value] += 1

plt.figure(1)
plt.plot(histogram)
plt.show()

photo2 = cv2.imread("img.jpg", 0)

hist = cv2.calcHist([photo2], [0], None, [256], [0, 256])


plt.figure(1)
plt.plot(histogram)
plt.show()
