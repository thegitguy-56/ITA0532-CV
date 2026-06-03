import cv2
import numpy as np
img = cv2.imread("Nature.jpg", 0)
img = cv2.resize(img, (800, 500))
kernel = np.ones((5,5), np.uint8)
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow("Blackhat", blackhat)
cv2.waitKey(0)
cv2.destroyAllWindows()
