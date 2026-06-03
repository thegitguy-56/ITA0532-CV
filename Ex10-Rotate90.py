import cv2
img = cv2.imread("Nature.jpg")
img = cv2.resize(img, (800, 500))
rot = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("Rotate 90", rot)
cv2.waitKey(0)
cv2.destroyAllWindows()
