import cvTwo as cv
import numpy as np

img = cv.imread('photos/dog1.jpg', ) 
cv.imshow('dog', img)

blank = np.zeros(img.shape, dtype='uint8')
# cv.imshow('Blank', blank)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (5, 5), 0)
edges = cv.Canny(blur, 50, 150)
contours, hierarachies = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
# This line is used to find the contours (boundaries) of objects in an image. 
# Here's a part-by-part explanation:----

# The source image, which must be a binary image (i.e., black and white).
# You usually get this from cv.Canny() or cv.threshold().
# Non-zero pixels (white) are considered part of objects.

# This is the contour retrieval mode.

# RETR_EXTERNAL means: Only get the outermost (external) contours, ignoring any child contours (like holes inside shapes).
# 🔁 Other modes:

# RETR_LIST: Retrieves all contours, but doesn’t create a hierarchy.

# RETR_TREE: Retrieves all contours and reconstructs the full hierarchy of nested contours.

# 3. cv.CHAIN_APPROX_SIMPLE
# This is the contour approximation method.

# It removes all redundant points and compresses the contour to save memory.

# 📉 For example, a rectangle may only be represented by 4 corner points instead of dozens.

# 🔁 Other option:

# CHAIN_APPROX_NONE: Stores all the contour points (more memory).

print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (0,0,255), 2)
cv.imshow('Contours Drawn', blank)
cv.waitKey(0)





# how to convert an image to BSR to HSV-------------------------
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV' , hsv)
cv.waitKey(0)