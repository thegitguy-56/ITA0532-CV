import cv2
img = cv2.imread("Road.jpg")
img = cv2.resize(img, (800, 500))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 127, 255, 0)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for c in contours:
    x,y,w,h = cv2.boundingRect(c)
    if w>50 and h>50:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow("Object Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
