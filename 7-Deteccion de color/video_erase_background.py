import cv2 as cv
import numpy as np
import moviepy.editor as mp

#Capturar archivo de video y crear uno de salida
video = cv.VideoCapture('video.mp4')
fourcc = cv.VideoWriter_fourcc('m', 'p', '4', 'v')
out = cv.VideoWriter('output.mp4',fourcc,60,(1920,1080))

#estableciendo fondo
imagen2= 'img2.jpg'
imagenFondo=cv.imread(imagen2)

#rango
minBGR = np.array([110,110,0])
maxBGR = np.array([255, 255,140])

while  video.isOpened():
    is_ok, frame = video.read()
    if not is_ok:
        break
    frame = cv.resize(frame,(1920,1080))
    imagenFondo = cv.resize(imagenFondo,(1920,1080))
    maskBGR = cv.inRange(frame,minBGR,maxBGR)
    mask_inv = cv.bitwise_not(maskBGR)
    resultBGR = cv.bitwise_and(frame, frame, mask = mask_inv)
    result_inv = cv.bitwise_and(imagenFondo, imagenFondo, mask = maskBGR)
    total=cv.add(resultBGR,result_inv)

    out.write(total)
    
out.release()

#para agregar audio 
audio = mp.AudioFileClip("audio.mp3")
video1 = mp.VideoFileClip("output.mp4")
final = video1.set_audio(audio)
final.write_videofile("output_finalFULLHD.mp4")