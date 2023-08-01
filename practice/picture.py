import cv2
import numpy as np

img = cv2.imread('./image/1.jpg')
cv2.imshow('img', img)

num = np.zeros(img.shape, img.dtype) + 150
imgIncrease = cv2.add(img, num)
imgSubtract = cv2.subtract(img, num)

# cv2.imwrite("2.jpg",imgIncrease)
# cv2.imwrite("3.jpg",imgSubtract)
cv2.imshow('img', img)
cv2.imshow('increase', imgIncrease)
cv2.imshow('subtract', imgSubtract)

cv2.waitKey()
cv2.destroyAllWindows()
