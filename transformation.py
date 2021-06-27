import cv2 as cv
import numpy as np

img = cv.imread("./images/Cat.png")

cv.imshow("Cat",img)

# Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

translated = translate(img, -100, 100)
cv.imshow("Translated", translated)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint == None:
        rotPoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 90)
cv.imshow("rotated", rotated)

# Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow("resized", resized)

# Flipping
flip = cv.flip(img, 1)
cv.imshow("flip", flip)

cv.waitKey(0)

cv.destroyAllWindows()