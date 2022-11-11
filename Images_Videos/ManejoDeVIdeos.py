import cv2 as cv
#Lectura de Videos
#EL metodo VIdeoCapture puede tomar argumentos como enteros
#Pasar un entero puede representar para webcams o camaras conectadas
#o un camino a un video
#capture = cv.VideoCapture('Videos/dog.mp4')
capture = cv.VideoCapture(0)
#Para leer un video se necesita un loop para capturar cada Frame
while True:
    #EL metodo lee Frame por Frame, retorna el frame y el booleano
    #Para saber si la lectura fue exitosa
    isTrue,frame = capture.read()
    cv.imshow('Video',frame)
    #Para parar
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
        #Liberamos
capture.release
#Destuimos ventanas
cv.destroyAllWindows()