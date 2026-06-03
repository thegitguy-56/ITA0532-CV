import cv2
import numpy as np
img = cv2.imread("Nature.jpg", 0)
img = cv2.resize(img, (800, 500))
kernel = np.ones((5,5), np.uint8)
dilation = cv2.dilate(img, kernel)
cv2.imshow("Morph Dilation", dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()
