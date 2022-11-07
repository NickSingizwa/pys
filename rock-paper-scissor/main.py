import cv2
import cvzone

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while True:
    imgBg = cv2.imread("resources/bg.png")
    success, img = cap.read()

    imgScaled = cv2.resize(img,(0,0),None,0.875,0.875)
    imgScaled = imgScaled[:, 80:480]    # : meaning the width doesn't change

    imgBg[234:654,795:1195] = imgScaled # Replace the background with the webcam image

    # cv2.imshow("Image", img)
    # cv2.imshow("Image Scaled", imgScaled)
    cv2.imshow("Image Background", imgBg)

    cv2.waitKey(1)