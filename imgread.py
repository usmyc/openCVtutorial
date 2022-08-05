import cv2 as cv

cat = cv.imread('1.jpeg')
print(cat)
cv.imshow('Cat', cat)


def rescaleFrame(frame, scale=0.75):  # we created scale function here.
    # working with image, video and livevideo
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def changeRes(width, height):
    # Just for live video
    capture.set(3, width)
    capture.set(4, height)


catscaled = rescaleFrame(cat)
cv.imshow('scaledcat', catscaled)
capture = cv.VideoCapture('cat.mp4')

while True:
    isTrue, frame = capture.read()

    # we can scale again from here.
    frame_resized = rescaleFrame(frame, scale=.2)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)
