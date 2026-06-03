import cv2
from matplotlib import pyplot as plt
img = cv2.imread("Nature.jpg")
for i, col in enumerate(('b','g','r')):
    hist = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist, color=col)
plt.show()
