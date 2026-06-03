import cv2
img = cv2.imread("Nature.jpg", 0)
img = cv2.resize(img, (800, 500))
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1)
cv2.imshow("Sobel X", sobelx)
cv2.imshow("Sobel Y", sobely)
cv2.waitKey(0)
cv2.destroyAllWindows()
