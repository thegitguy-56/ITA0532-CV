import cv2
img = cv2.imread("Nature.jpg", 0)
img = cv2.resize(img, (800, 500))
eq = cv2.equalizeHist(img)
cv2.imshow("Equalized", eq)
cv2.waitKey(0)
cv2.destroyAllWindows()
