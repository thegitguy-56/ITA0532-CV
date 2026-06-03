import cv2
img = cv2.imread("Nature.jpg")
img = cv2.resize(img, (800, 500))
roi = img[100:300, 200:400]
img[0:200, 0:200] = roi
cv2.imshow("ROI Copy", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
