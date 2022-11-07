import cv2

faceCascade = cv2.CascadeClassifier("resources/haarcascade_frontalface_default.xml")  #trained model
img = cv2.imread("resources/reece.jpg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)  #scaleFactor=1.1, minNeighbors=4

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)  #draw rectangle around face

cv2.imshow("Result", img)
cv2.waitKey(0)