import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat',img)

#Srive para imagenes,videos, videos en vivo
def rescaleFrame(frame,scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] *scale)
    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

#videos en vivo
def changeResolution(width,height):
    capture.set(3,width)
    capture.set(4,height)




resized_image = rescaleFrame(img)
cv.imshow('large',resized_image)


#Captura video
capture = cv.VideoCapture('Videos/dog.mp4')
while True:
    isTrue,frame = capture.read()
    frame_resized = rescaleFrame(frame)
    cv.imshow('Video',frame)
    cv.imshow('VideoResized', frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release
cv.destroyAllWindows()
