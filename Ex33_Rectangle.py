import numpy as np
import cv2
img = np.ones((500,500,3), dtype=np.uint8) * 255
cv2.rectangle(img, (100,100), (400,400), (255,0,0), 3)
cv2.imshow("Rectangle", img)
print("Press any key on image window to close")
cv2.waitKey(0)
cv2.destroyAllWindows()
