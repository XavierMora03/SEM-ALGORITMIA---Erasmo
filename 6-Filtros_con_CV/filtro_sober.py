import cv2 as cv
import numpy as np
import random
# Image values
img_dir = 'happy_doggo.jpg'
img_name = 'Doggo'
#defining filter
gauss_filter = [[.1, .5 ,.1],
                [.5, 1 ,.5],
                [.1 ,.5 ,.1]]
gauss_denominador = 9
gauss_filter_alternative = [[1,2,1],
                [2,4,2],
                [1,2,1]]
gauss_denominador_alternative = 16
sobel_filter = [[-1 ,0, 1],
                [-2 ,0,2],
                [-1,0,1]]
sobel_denominador = 9

filter_matrix = sobel_filter
filter_denominador = sobel_denominador
filter_dimension = len(filter_matrix)

#leyendo imagen y almacenando medidas
imagenOriginal=cv.imread(img_dir)
filas,columnas,canales = np.shape(imagenOriginal)
imagen_con_filtro = np.zeros((filas,columnas,3),dtype='uint8')

#aplicando filtro
for numero_de_fila in range(filas-2):
    for numero_de_columna  in range(columnas-2):
        for numero_de_canal in range(3):  
            #multiplicando matrices
            matrix_sum = 0
            for f in range(3):
                for c in range(3):
                    matrix_sum += imagenOriginal[numero_de_fila+f][
                        numero_de_columna+c][numero_de_canal
                                             ]*filter_matrix[f][c]
            pixel_value = min(255,matrix_sum/filter_denominador)
            pixel_value = max(0,pixel_value)
            imagen_con_filtro[numero_de_fila+1,numero_de_columna+1
                              ][numero_de_canal] = pixel_value
            
cv.imshow(img_name+'Original',imagenOriginal)
cv.imshow(img_name+'Filter',imagen_con_filtro)

#Saliendo...
pressed_key = cv.waitKey(0)
if True or pressed_key == ord('s'):
    cv.imwrite(img_name+'sobel.png',imagen_con_filtro)
cv.destroyAllWindows()