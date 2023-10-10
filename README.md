# Answer
Refer to *answer.png* for the solution

# Methodology
First, I read the image and obtained the height, width, and midpoint (1/2 of width) of *red.png*. I then created a mask to isolate the cones from the background. I did this by converting the image from BGR to HSV, then determining the bounds of the mask based on the darkest and lightest colors on the cones. After applying the mask to the image, I then proceeded to create an array of the cones' contours. I did this by applying a slight Gaussian blur to smooth the image out, then using Canny to obtain the edges of the cones and using cv2.findCountours to create an array of contours. I then filtered the contours by area to make sure they were the same size as the cones, and sorted the resulting array by the x-coordinates of the contours. After that, I created a new array of the x and y coordiantes of each contour, and used it to draw lines between each cone. I started at the bottom left corner of the image, and drew a line to the next sorted set of coordinates. When the coordinates would cross over from the left to the right side of the image, I broke the line as to not connect the two path sides together. Finally, I saved the resulting image in *answer.png*.

# What I Tried
At first, I tried splitting the image in left and right halves, and calculating the path on each side and combining the two halves. However, this proved inefficient as I would have to repeat the process twice for each half. Connecting the halves back together also proved problematic. I also tried to remove the top 1/4 of the image to eliminate inaccurate contours, but this was more efficiently remedied by adjusting the bounds of the mask's darker color. I also tried to find the line of best fit using _matplotlib_, but ultimately decided that connecting each point separately was more efficient and concise.

# Libaries Used
I used _OpenCV_ (cv2) in my program.