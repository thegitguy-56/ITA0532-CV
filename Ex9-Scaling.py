import cv2
img = cv2.imread("Nature.jpg")
small = cv2.resize(img, (400, 250))
big = cv2.resize(img, (1200, 800))
cv2.imshow("Small", small)
cv2.imshow("Big", big)
cv2.waitKey(0)
cv2.destroyAllWindows()
