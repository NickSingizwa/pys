import cv2
import numpy as np

img = cv2.imread("resources/kit.png")

width,height = 250,350   #width and height of a playing card
pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])  #use paint to get the values of each corner
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image",img)
cv2.imshow("output",imgOutput)
cv2.waitKey(0)