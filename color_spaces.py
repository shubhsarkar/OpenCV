import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("./images/dog.png")

cv.imshow("Dog",img)

# plt.imshow(img)
# plt.show()

# BGR to GRAY
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("hsv",hsv)

# BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("LAB",lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB",rgb)

plt.imshow(rgb)
plt.show()

cv.waitKey(0)

cv.destroyAllWindows()