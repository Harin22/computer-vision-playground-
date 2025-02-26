import cv2 as cv
import numpy as np

#Read the original image
image = cv.imread("D:\K.jpg")


image_info = image.shape
print(image_info[0])

resizing_img = cv.resize(image,(300, 300))
cv.imshow("Resized Image", resizing_img)

scale_percent = 50  
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
resized = cv.resize(image, (width, height))
cv.imshow("Resized image", resized)

#converting grayscale image
hsv = cv.cvtColor(resized, cv.COLOR_BGR2HSV)
lab = cv.cvtColor(resized, cv.COLOR_BGR2LAB)
cv.imshow("HSV", hsv)
cv.imshow("LAB", lab)

contrasting = cv.convertScaleAbs(image, alpha = 1.5, beta = 0)
cv.imshow("contrast image", contrasting)


#Wait for a key press and close the windows
cv.waitKey(0)
cv.destroyAllWindows()


