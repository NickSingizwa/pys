import cv2
import numpy as np

img = cv2.imread("./lena.jpg")

# Get the dimensions of the image
height, width = img.shape[:2]

# Define the scaling factor
scale_factor = 0.3

# Compute the new dimensions of the image
new_height = int(height * scale_factor)
new_width = int(width * scale_factor)

# Resize the image using the computed dimensions
resized_img = cv2.resize(img, (new_width, new_height))

# gray image
img_gray = cv2.cvtColor(resized_img,cv2.COLOR_BGR2GRAY)

# blur image
img_blur = cv2.GaussianBlur(resized_img,(5,5),0)

# edges of an image
canny_img = cv2.Canny(img_blur, 100, 200)

# Define the kernel for morphological operations
kernel = np.ones((5, 5), np.uint8)

# Apply erosion to the image
eroded_img = cv2.erode(img_gray, kernel, iterations=1)
dilated_img = cv2.dilate(img_gray, kernel, iterations=1)

cv2.imshow("edges",dilated_img)
cv2.waitKey(0)