import cv2
import numpy as np
img = cv2.imread("Nature.jpg")
img = cv2.resize(img, (800, 500))
pts1 = np.float32([[0,0],[800,0],[0,500],[800,500]])
pts2 = np.float32([[0,0],[700,50],[50,450],[750,500]])
M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(img, M, (800,500))
cv2.imshow("Perspective", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
