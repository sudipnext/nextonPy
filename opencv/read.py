import cv2 as cv

img = cv.imread('Photos/cat_large.jpg') #saving image to a variable called img

cv.imshow('Cat', img) #Displaying image

cv.waitKey(0) #Time is in miliseconds
