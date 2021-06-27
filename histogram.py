import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("./images/dog.png")
cv.imshow("Dog",img)

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray",gray)

# # Grayscale Histogram
# gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])

# Using mask
blank = np.zeros(img.shape[:2], dtype="uint8")
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow("Masked", masked)

# mask_hist = cv.calcHist([gray], [0], masked, [256], [0,256])

# plt.figure()
# plt.title("Grayscale Hist")
# plt.xlabel("Bins")
# plt.ylabel("# of pixels")
# plt.plot(mask_hist)
# plt.xlim([0,256])
# plt.show()

# Colour Histogram
plt.figure()
plt.title("Grayscale Hist")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
colors = ('b','g','r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()