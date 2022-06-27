import cv2 as cv
# Takes either integer if i am going to use webcam then if i am using videos i simply put the path of the video file
# capture = cv.VideoCapture(0)
capture = cv.VideoCapture('Videos/dog.mp4')
#I am reading videos as images by frame by frame while it's true it will continue to extract the files into two types one is a boolean and another is a frame
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
#Until i press the key d then the loop goes on an on and when i finally press d it breaks the loops and exits
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
#it's used to capture the release and destroy all windows for that i don't need that windows so
capture.realease()
cv.destroyAllWindows()
