import cv2 as cv

#Usamos el metodo imread para leer una imagen
#img = cv.imread('Photos/cat.jpg')
#Con la siguiente imagen surge un problema las dimensiones que son mas grandes, la imagen se va de la pantalla
img = cv.imread('Photos/cat_large.jpg')
#Este metodo muestra la imagen en una nueva ventana. pasamos el nombre de la ventana y la imagen
cv.imshow('Cat',img)
#
#Mantiene cualquier evento de ventana, tal como crear ventana o mostrar imagenes
cv.waitKey(0)