import cv2 as cv

img = cv.imread("./images/dani.jpg")
cv.imshow("Dani", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray) 

# Creating a CascadeClassifier Object
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Search the co-ordinates of the image
faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 3)

print(f"No. of faces = {len(faces)}")

for x,y,w,h in faces:
    img = cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

cv.imshow("Detected", img)

cv.waitKey(0)
cv.destroyAllWindows()
