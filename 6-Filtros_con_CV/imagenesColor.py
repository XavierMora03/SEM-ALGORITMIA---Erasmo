# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:12:50 2019

@author: GabrielAsus
"""
##opencv
import cv2 as cv
import numpy as np
#leer imagen en el mismo directorio que el archivo de python
imagenOriginal3=cv.imread('elmoCookie.jpg')
#leer archivo en otro directorio
imagenOriginal2=cv.imread('C:\\Users\\GabrielMtz\\Mi unidad\\clases\\algoritmia\\liz3.jpg')
#leer archivo en otro directorio el parametro cero al final es para especificar que sera en escala de grises
imagenEngris=cv.imread('C:\\Users\\GabrielMtz\\Mi unidad\\clases\\algoritmia\\liz2.jpg',0)
#cv.imshow('imagen',imagenOriginal)
cv.imshow('imagen2',imagenOriginal2)
cv.imshow('imagen3',imagenOriginal3)
cv.imshow('imagenen gris',imagenEngris)
#para esperar la presion de una tecla antes de continuar
cv.waitKey()
#la funcion shape sirve para saber las dimensiones del arreglo que contiene los datos de la imagen
print(np.shape(imagenOriginal3))
print(np.shape(imagenEngris))
#se guardan las dimensiones en las variable s filas,columnas y canales
filas,columnas,canales=np.shape(imagenOriginal3)
#se crea una matriz llena de ceros
imagenZeros=np.zeros((filas,columnas))
cv.imshow('imagenZeros',imagenZeros)
#obetner cada uno de los canales
azul=imagenOriginal3[:,:,0]
verde=imagenOriginal3[:,:,1]
rojo=imagenOriginal3[:,:,2]

cv.imshow('rojo',rojo)
cv.imshow('verde',verde)
cv.imshow('azul',azul)

