
import cv2 as cv

# primero grabo, para evirtar la falta de frames en output
nombre_webcam_record = 'webcamrecord.mp4'
nombre_video_filtered = 'output.mp4'
cap = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'mp4v')
out = cv.VideoWriter(nombre_webcam_record, fourcc, 30.0, (640, 480))
while(True):
    ret, frame = cap.read()
    cv.imshow('frame', frame)
    out.write(frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
#fin de la grabacion
cap.release()
out.release()

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv.CascadeClassifier(cascPath)
# configuracion de video, tomando el que grabamos
video = cv.VideoCapture(nombre_webcam_record)
finalOut = cv.VideoWriter(nombre_video_filtered, fourcc, 30.0, (640, 480))
# ajustando el antifaz
ajustex = 38
antifaz = cv.imread('antifaz.png', cv.IMREAD_UNCHANGED)
if not video.isOpened():
    print('No se pudo acceder a la camara')
else:
    while video.isOpened():
        # revisar si ya puedo leer imagenes de la camara
        ret, frame = video.read()
        frame = cv.flip(frame, 1)
        imagenGrises = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            imagenGrises,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(40, 40)
        )
        #deteccion de rostro
        for (x, y, w, h) in faces:
            # resize a antifaz
            antifaz_resized = cv.resize(antifaz, (w, h))
            #intentar reajustar según el tamaño por regla de 3
            ajustex_proporcional = int((w*h)*ajustex/28000)
            for i in range(w):
                for j in range(h):
                    if(antifaz_resized[i][j][3] != 0):
                        frame[y+i-ajustex_proporcional]
                        [x + j][0] = antifaz_resized[i][j][0]
                        frame[y+i-ajustex_proporcional]
                        [x + j][1] = antifaz_resized[i][j][1]
                        frame[y+i-ajustex_proporcional]
                        [x + j][2] = antifaz_resized[i][j][2]
            # break porque solo espero una cara por cada frame
            break
        finalOut.write(frame)
    #terminando la grabacion de video
    video.release()
    cv.destroyAllWindows()
