import cv2
import numpy as np
# img = cv2.imread('photos/dog1.jpg')

# image is showing vertical and horizontal--------------
# imgHor = np.hstack((img, img))
# imgVer = np.vstack((img,img))

# cv2.imshow("Horizontal" , imgHor)
# cv2.imshow("vertical" , imgVer)

# cv2.waitKey(0)

# image is showing vertical and horizontal from stackImage--------------
# def stackImages(scale, imgArray):
#     import cv2
#     import numpy as np
    
#     rows = len(imgArray)
#     cols = len(imgArray[0]) if isinstance(imgArray[0], list) else 1
#     rowsAvailable = isinstance(imgArray[0], list)

#     width = imgArray[0][0].shape[1] if rowsAvailable else imgArray[0].shape[1]
#     height = imgArray[0][0].shape[0] if rowsAvailable else imgArray[0].shape[0]

#     if rowsAvailable:
#         for x in range(rows):
#             for y in range(cols):
#                 img = imgArray[x][y]
#                 if img.shape[:2] != (height, width):
#                     imgArray[x][y] = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)
#                 if len(img.shape) == 2:  # if grayscale, convert to color
#                     imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
#         hor = [np.hstack(imgArray[x]) for x in range(rows)]
#         ver = np.vstack(hor)
#     else:
#         for x in range(rows):
#             if imgArray[x].shape[:2] != (height, width):
#                 imgArray[x] = cv2.resize(imgArray[x], (width, height), interpolation=cv2.INTER_AREA)
#             if len(imgArray[x].shape) == 2:
#                 imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
#         ver = np.hstack(imgArray)

#     return cv2.resize(ver, (0, 0), fx=scale, fy=scale)

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# imgStack = stackImages(0.5, ([img, gray, img]))
# imgStack = stackImages(0.5, ([img, img, img], [img, img, img]))
# cv2.imshow("ImageStack", imgStack)
# cv2.waitKey(0)


# COLOR DETECTION-------------
def empty(a):
    pass

def stackImages(scale, imgArray):
    import cv2
    import numpy as np
    
    rows = len(imgArray)
    cols = len(imgArray[0]) if isinstance(imgArray[0], list) else 1
    rowsAvailable = isinstance(imgArray[0], list)

    width = imgArray[0][0].shape[1] if rowsAvailable else imgArray[0].shape[1]
    height = imgArray[0][0].shape[0] if rowsAvailable else imgArray[0].shape[0]

    if rowsAvailable:
        for x in range(rows):
            for y in range(cols):
                img = imgArray[x][y]
                if img.shape[:2] != (height, width):
                    imgArray[x][y] = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)
                if len(img.shape) == 2:  # if grayscale, convert to color
                    imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        hor = [np.hstack(imgArray[x]) for x in range(rows)]
        ver = np.vstack(hor)
    else:
        for x in range(rows):
            if imgArray[x].shape[:2] != (height, width):
                imgArray[x] = cv2.resize(imgArray[x], (width, height), interpolation=cv2.INTER_AREA)
            if len(imgArray[x].shape) == 2:
                imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        ver = np.hstack(imgArray)

    return cv2.resize(ver, (0, 0), fx=scale, fy=scale)

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 120, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 248, 255, empty)
cv2.createTrackbar("val Min", "TrackBars", 112, 255, empty)
cv2.createTrackbar("val Max", "TrackBars", 255, 255, empty)

while True:
 img = cv2.imread('photos/dog1.jpg')
 imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
 h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
 h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
 s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
 s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
 val_min = cv2.getTrackbarPos("val Min", "TrackBars") 
 val_max = cv2.getTrackbarPos("val Max", "TrackBars") 

 print(h_min, h_max, s_min, s_max, val_min, val_max)
 lower = np.array([h_min,s_min,val_min])
 upper = np.array([h_max,s_max,val_max])
 mask = cv2.inRange(imgHSV,lower,upper)
 imgresult = cv2.bitwise_and(img, img, mask=mask)
 imgStack = stackImages(0.6,([img, imgHSV], [mask, imgresult]))
 cv2.imshow("stacked images", imgresult)

 print(h_min)
#  cv2.imshow("original", img)
#  cv2.imshow("HsvImg", imgHSV)
#  cv2.imshow("Mask", mask)
#  cv2.imshow("imgresult", imgresult)
 cv2.imshow("imageStack", imgStack)
 cv2.waitKey(1)