import cv2 as cv
import numpy as np
#setting up the canvas to draw
#first two parameter for the canvas size and third for how many colors 
blank = np.zeros((500, 500, 3), dtype='uint8')
# img = cv.imread('Photos/cat.jpg')
cv.imshow('Blank', blank)

#Painting the image in a certain color
blank[200:300, 300:400] = 0, 0, 255 # The parameters defines from where to where we are going to color
# blank[:]= 0, 255, 0
cv.imshow('Greeen', blank)

#drawing a rectangle
cv.rectangle(blank, (0,0), (250,250), (0, 255, 0), thickness=2)
cv.imshow('Rectangle', blank)

cv.waitKey(0)
