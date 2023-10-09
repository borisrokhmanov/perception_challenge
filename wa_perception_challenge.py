import numpy as np
import cv2

img = cv2.imread("red.png") #load image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert to grayscale
blur = cv2.GaussianBlur(gray, (5, 5), 0) #gaussian blur to reduce noise
edges = cv2.Canny(blur, 50, 150) #edge detection
contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#find contours in edge-detected image

output = img.copy()
for cont in contours:
    if cv2.arcLength(cont, True) > 100: #filter out small contours
        cv2.drawContours(output, [cont], -1, (0, 0, 255), 2)

cv2.imwrite("answer.png", output) #save answer image