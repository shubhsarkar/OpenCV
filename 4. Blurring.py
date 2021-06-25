import cv2 as cv
import numpy as np

img = cv.imread("./images/dog.png")
cv.imshow("Dog",img)

# Averaging Blur
average = cv.blur(img, (7,7))
cv.imshow("Average Blur",average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow("Gaussian",gauss)

# Median Blur
median = cv.medianBlur(img, 7)
cv.imshow("Median",median)

#bilateral
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow("Bilateral",bilateral)

cv.waitKey(0)
cv.destroyAllWindows()