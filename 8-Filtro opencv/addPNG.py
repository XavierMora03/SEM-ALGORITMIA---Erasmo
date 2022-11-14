# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 00:38:59 2021

@author: GabrielMtz
"""

import cv2 as cv

elMono=cv.imread("marco.png",cv.IMREAD_UNCHANGED)
elFondo=cv.cvtColor(cv.imread("sunnyDay.jpg"),cv.COLOR_BGR2BGRA)
cv.imshow("png",cv.cvtColor(elMono,cv.COLOR_BGRA2BGR))
cv.imshow("fondo",elFondo)
cv.waitKey()
print("shape del mono",elMono.shape)
print("sahep del fondo",elFondo.shape)
# elPng=cv.resize(elPng,(300,300))
filaDeseada=200
colDeseada=400
elMono=cv.resize(elMono,(300,200))
elFondo=cv.resize(elFondo,(1024,1024))
for i in range(elMono.shape[0]):
    for j in range(elMono.shape[1]):
        if(elMono[i,j][3]!=0):
           elFondo[i+filaDeseada,j+colDeseada]=elMono[i,j]
elFondo=cv.cvtColor(elFondo,cv.COLOR_BGRA2BGR)   
cv.imshow("Paste",elFondo)
cv.imwrite("combinacionPNG.png",elFondo)
cv.waitKey()
# resultado=cvz.overlayPNG(elFondo, elPng,[10,10])
# cv.imshow("resultado",resultado)