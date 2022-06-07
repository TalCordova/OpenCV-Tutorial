import cv2
import random

img = cv2.imread('assets/vecna.jpeg', 1)

tag = img[400:600, 600:900]
img[200:400, 100:400] = tag

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

