import cv2

## load image
img = cv2.imread('assets/download.png', 0)
img = cv2.resize(img, (0,0), fx = 0.5, fy = 0.5)
img = cv2.rotate(img, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imwrite('new_img.jpg', img)
cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

