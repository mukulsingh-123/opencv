import cvTwo as cv

# img = cv.imread('photos/dog1.jpg', )  # Step 1: Read image
# cv.imshow('Dog', img)  # Step 2: Show image in a new window
# cv.waitKey(0) #cv.waitKey(0) (or cv2.waitKey(0)) is a keyboard binding function used in OpenCV to wait for a key event. It is typically used after displaying an image using cv2.imshow().
# How It Works
# The argument passed to waitKey() is in milliseconds.
# 0 means wait indefinitely for a key press.
# If you pass a number like 1000, it will wait 1000 milliseconds (1 second) before continuing.


# how to resize and rescale the image------------
# this method is works for images video or live video------
# def rescaleImage(img, scale=0.75):
#    width = int(img.shape[1] * scale)
#    height = int(img.shape[0] * scale)
#    dimensions = (width, height)
#    return cv.resize(img, dimensions, interpolation=cv.INTER_AREA)

# resize_image = rescaleImage(img)
# cv.imshow('Image', resize_image)
# cv.waitKey(0)



# Reading videos-----
# capture = cv.VideoCapture('videos/dog.mp4')

# while True: #Run this loop forever (unless we break it manually)
    # isTrue, frame = capture.read() # Read the next video frame. If it works, isTrue = True
#     # Allows the video to play frame-by-frame smoothly.
#     # gives you one frame (image) at a time from the video.
    # cv.imshow('video', frame)
#     if cv.waitKey(20) & 0xFF==ord('d'): # it means if letter d is press then out of the loop
#         break
#     #some wait is stoped the video from playing indefinitely
# capture.release()
# cv.destroyAllWindows()



# How to Resize and Rescale the image-----
# this method is works for images, video,  live video---------
# def rescaleFrame(frame, scale=0.75):
#     width = int(frame.shape[1] * scale)
#     height = int(frame.shape[0] * scale)
#     dimensions = (width , height)

#     return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# while True: #Run this loop forever (unless we break it manually)
    # isTrue, frame = capture.read() # Read the next video frame. If it works, isTrue = True
    # frame_resized = rescaleFrame(frame)
    # frame_resized = rescaleFrame(frame, scale=.2)
    # cv.imshow('video', frame)
    # cv.imshow('video Resized' , frame_resized)
    # if cv.waitKey(20) & 0xFF==ord('d'):
    #     break
    #some wait is stoped the video from playing indefinitely
# capture.release()
# cv.destroyAllWindows()


# this method is works for  live video---------
# def changeRes(width, height):
#     capture.set(3, width)  # 3 = width
#     capture.set(4, height) # 4 = height

# capture = cv.VideoCapture('videos/dog.mp4')  # Use 0 for webcam
# changeRes(640, 480)



#2 how to drawing shapes and putting Text-------------------------
import cvTwo as cv
import numpy as np


# How to create blank image--
# blank = np.zeros((500,500,3), dtype='uint8')  # pass height , width and number of color channel
# cv.imshow('Blank', blank)

# paint the image a certain color---
# blank[:] = 0,255,0
# if you want to color a certain portion---
# blank[200:300, 300:400] = 0,0,255
# cv.imshow('green', blank)


# Draw a rectangle---
# on the axis, width and height,  color, thickness---
# cv.rectangle(blank, (0,0), (250,250), (0,0,255), thickness=2)
# if you want to color half of the images then----thickness=cv.FILLED or thickness=-1
# reactangle with filled with color---
# cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0, 0, 255,), thickness=-1)
# cv.rectangle(image, pt1, pt2, color, thickness)
# pt1: top-left corner (x1, y1)
# pt2: bottom-right corner (x2, y2)
# color: (B, G, R)
# thickness: -1 means fill the rectangle
# cv.imshow('rectangle', blank)

# draw a circle--
# cv.circle(blank, (blank.shape[1]//2,  blank.shape[0]//2), 40, (0, 255, 0), thickness=-1)
# cv.circle(image, center_coordinates, radius, color, thickness)


# Draw the line-------
# cv.line(blank, (0,0), (blank.shape[1]//2,  blank.shape[0]//2), (255, 255, 255), thickness=3)
# cv.imshow('line', blank)
# cv.waitKey(0)



# write text on image-------
# cv.putText(blank, 'hello', (255, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
# cv.imshow('Text', blank)
# cv.waitKey(0)




# 3. Essential Functions------------------------------------
import cvTwo as cv

img = cv.imread('photos/dog1.jpg')  
cv.imshow('Dog', img) 

# function that are convert an image to gray sale-----
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('GrayImage', gray)
cv.waitKey(0) 

# how to blur an image----
# Blur = cv.GaussianBlur(img, (7, 7), 0)
# cv.imshow('BlurImage', Blur)
# cv.waitKey(0)

# how to do threshold the image-------
# _, thresh = cv.threshold(Blur, 127, 255, cv.THRESH_BINARY)
# If a pixel value in gray_img is greater than 127, it will be set to 255 (white).
# If it is less than or equal to 127, it will be set to 0 (black).

# cv.imshow('threshold', thresh)
# cv.waitKey(0)

# how to create an edge cascode-------------------------------------
# canny = cv.Canny(img, 125, 175)
# cv.imshow('cannny Edge' , canny)



# dialted the image----------
# dialeted = cv.dilate(canny, (7,7), iterations=1)
# cv.imshow('dilatedImage', dialeted)
# # cv.waitKey(0)

# Eroding-------
# eroded = cv.erode(dialeted, (7,7), iterations=3)
# cv.imshow('Eroded', eroded)
# cv.waitKey(0)

# Resize
# resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
# cv.imshow('Resized', resized)
# cv.waitKey(0)


#  cropped
# cropped = img[50:200, 200:400]
# cv.imshow('Cropped', cropped)
# cv.waitKey(0)


# image transformation-----------

# trnaslation------
# Let's shift image 100 pixels right and 50 pixels down
# shift_x = 100
# shift_y = 50
# translation_matrix = np.float32([[1, 0, shift_x], [0, 1, shift_y]])

# # Get the dimensions of the image
# height, width = img.shape[:2]

# # Apply warpAffine for translation
# translated_img = cv.warpAffine(img, translation_matrix, (width, height))

# # Show the result
# cv.imshow("Translated Image", translated_img)
# cv.waitKey(0)
# cv.destroyAllWindows()

# how to rotate the image and flip the image---------


