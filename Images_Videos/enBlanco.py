import cv2 as cv
import numpy as np

#Para poder dibujar un cuadro en blanco
blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)

#Podemos pintar de cierto color
#blank[:] = 0,255,0
blank[200:300,300:400] = 0,0,255
cv.imshow('Green',blank)

#Podemos dibujar un rectangulo indicando la pos, ancho, altura, color y
#cv.rectangle(blank,(0,0),(250,250),(0,255,0), thickness=2)
cv.rectangle(blank,(0,0),(250,500),(0,255,0), thickness=cv.FILLED)
cv.imshow('Rectangulo',blank)


cv.waitKey(0)