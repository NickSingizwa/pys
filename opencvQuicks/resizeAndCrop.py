import cv2

img = cv2.imread("resources/reece.png")
print(img.shape)  # (height, width, channels(color))

imgResize = cv2.resize(img, (300, 200))  # width, height

imgCropped = img[0:200, 200:500]  #height, width

cv2.imshow("Output", img)
cv2.waitKey(0)   #for not disappearing