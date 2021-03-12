import matplotlib.pyplot as plt
import cv2
import numpy as np

img = cv2.imread("icon.jpg", 0)
#img = cv2.GaussianBlur(img, (3, 3), 0)
canny = cv2.Canny(img, 10, 180)

cv2.imshow('Icon', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("target.png", canny)