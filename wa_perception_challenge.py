import cv2

img = cv2.imread("/Users/boris/Documents/python/perception_challenge/red.png")
height, width, _ = img.shape #get height, width, and midpoint of image
midpoint = width // 2
imgL = img[:, :midpoint] #split img into left and right halves
imgR = img[:, midpoint:]

#creates mask and applies it to image
hsvImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #convert to HSV from BGR
darkCol = (10, 255, 255)
lightCol = (0, 150, 160) 
mask = cv2.inRange(hsvImg, lightCol, darkCol) #create mask with darkest and lightest colors
result = cv2.bitwise_and(img, img, mask=mask) #apply mask to image

#gets array of contours from cones
blur = cv2.GaussianBlur(result, (5, 5), 0)
edges = cv2.Canny(blur, 50, 150) #use Canny to get edges of cones
contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

filteredContours = [contour for contour in contours if cv2.contourArea(contour) > 100] 
#if area of cone's contour is greater than threshold, add to new array 
filteredContours.sort(key=lambda contour: cv2.minEnclosingCircle(contour)[0])  #sort contours by x-coordinate

conePositions = []
for contour in filteredContours:
    (x, y), _ = cv2.minEnclosingCircle(contour) #get x,y coords of each contour
    conePositions.append((int(x), int(y))) #append to new array conePositions
    
#draw lines betwen contour coords
lastPos = (0,height)
conePositions.append((width,height)) #start at the bottom left corner, draw lines down the left side and up the right
crossedMid = False
for position in conePositions: 
    if (position[0] > midpoint and crossedMid == False): #if the coord is on the right side and it's the first time, don't connect the line
        cv2.line(img, position, position, (255, 0, 0), 10)
        lastPos = position
        crossedMid = True
    else:
        cv2.line(img, position, lastPos, (255, 0, 0), 10) #draw line between current coordinate and previous coordinate
        lastPos = position #update previous coordinate

cv2.imwrite("answer.png", img) #save answer