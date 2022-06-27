import cv2 as cv

img = cv.imread('Photos/cat_large.jpg')
cv.imshow('Cat', img)

#making a function to take two parameters one is frame and another is the scaling i have put the frame on the first argument and
#0.75 as the scaling factor both are put into a tuple to avoid modifications and then resized
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


resized_img = rescaleFrame(img)
cv.imshow('Cat_Resized', resized_img)
capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, scale=.2)
    cv.imshow('VideoResized', frame_resized)
    cv.imshow('Video', frame)

    if 0xFF == ord('0') & cv.waitKey(20):
        break

capture.release()
cv.destroyAllWindows()
cv.waitKey(0)
