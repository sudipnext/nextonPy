import cv2 as cv

# img = cv.imread('Photos/cat_large.jpg')
# cv.imshow('Cat', img)

#making a function to take two parameters one is frame and another is the scaling i have put the frame on the first argument and
#0.75 as the scaling factor both are put into a tuple to avoid modifications and then resized
def rescaleFrame(frame, scale=0.75):
        #this will work perfectly fine for images, videos and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
#this not work on standalone files only on live videos
    capture.set(3, width)
    capture.set(4, height)

capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    cv.imshow('Resoultion', frame)
    if 0xFF == ord('d') & cv.waitKey(20):
        break

capture.release()
cv.destroyAllWindows()
cv.waitKey(0)



