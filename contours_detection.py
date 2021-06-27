import cv2 as cv
import numpy as np

img = cv.imread("./images/Cat.png")

cv.imshow("Cat",img)
blank = np.zeros(img.shape, dtype='uint8')


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

# blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
# cv.imshow("Blur", blur)

# canny = cv.Canny(blur, 125, 175)
# cv.imshow("Canny",canny)

''' Alternate way '''

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(len(contours))
cv.imshow("thresh",thresh)

cv.drawContours(blank,contours, -1, (0,255,0),1)
cv.imshow("blank",blank)


cv.waitKey(0)

cv.destroyAllWindows()