import cv2 as cv
import numpy as np

imagen1 = 'img1.jpg'
imagen2= 'img2.jpg'
imagenOriginal=cv.imread(imagen1)
imagenPlaya=cv.imread(imagen2)

#resize
imagenOriginal = cv.resize(imagenOriginal,(1080,720))
imagenPlaya = cv.resize(imagenPlaya,(1080,720))

minBGR = np.array([0,110,0])
maxBGR = np.array([120, 255,120])
 
maskBGR = cv.inRange(imagenOriginal,minBGR,maxBGR)
mask_inv = cv.bitwise_not(maskBGR)
cv.imshow('mascara esto da un resutado',maskBGR)
cv.imshow('mascara_inv',mask_inv)

resultBGR = cv.bitwise_and(imagenOriginal, imagenOriginal, mask = mask_inv)
result_inv = cv.bitwise_and(imagenPlaya, imagenPlaya, mask = maskBGR)


cv.imshow('resultado',resultBGR)
cv.imshow('resultado_inv',result_inv)

total=cv.add(resultBGR,result_inv)
cv.imshow('resultado total',total)

cv.imwrite('resultado.jpg',total)
cv.waitKey()
cv.destroyAllWindows()
