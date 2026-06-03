import cv2
image=cv2.imread("Nature.jpg")
blur=cv2.GaussianBlur(image,(5,5),0)
cv2.imwrite("blurred_image.jpg",blur)
cv2.imshow("Blurred Image",blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
