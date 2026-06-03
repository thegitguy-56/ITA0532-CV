import cv2

face = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

img = cv2.imread("People.jpeg")

img = cv2.resize(img, (1000,700))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face.detectMultiScale(
    gray,
    scaleFactor=1.05,
    minNeighbors=4,
    minSize=(50,50)
)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

print("Number of faces:", len(faces))

cv2.imshow("Faces", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
