import cv2
image = cv2.imread('./lena.jpg')
y=0
x=0
h=100
w=200
lena_cropped = image[y:y+h, x:x+w]

# Save cropped image
cv2.imwrite("./lena_cropped.jpg", lena_cropped)

cv2.imshow('Lena Cropped', lena_cropped)
cv2.waitKey(0)
