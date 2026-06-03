import cv2
img = cv2.imread("Nature.jpg")
img = cv2.resize(img, (800, 500))
cv2.putText(img, "Nature Picture", (200,250),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
cv2.imshow("Watermark", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
