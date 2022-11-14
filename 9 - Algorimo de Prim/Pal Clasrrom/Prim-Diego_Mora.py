"""
TAREA 9 - PRIM
Ingienería informática
Diego Mora
Seminario de Algoritmia
Profesor: Erasmo Martínez
"""
import cv2
import numpy as np
from random import randint as rint  # solo para empezar aleatoriamente

# con esta funcion reviso si un punto ya esta en alguna de mis listas


def isInTheList(elemento, arreglo):
    for i in arreglo:
        if np.array_equal(i, elemento):
            return True
    return False


def calculaPeso(a1, a2):
    return ((a1[0]-a2[0]) ** 2 + (a1[1]-a2[1]) ** 2) ** .5

# retorna un arreglo que contiene presition-1 elementos (cuando es base 2)
# los cuales son parte de la línea entre p1 y p2


def puntoMedio(p1, p2, presition):
    if presition <= 1:
        return None

    x = (p1[0] + p2[0])/2
    y = (p1[1] + p2[1])/2
    medio = [x, y]
    pixeles = [medio]

    puntos_faltantes = [puntoMedio(p1, medio, presition/2),
                        puntoMedio(medio, p2, presition/2)]
    for p in puntos_faltantes:
        if p != None:
            pixeles.extend(p)

    return pixeles


def estaConectado(imagen, a1, a2, presiscion=8):
    for p in puntoMedio(a1, a2, presiscion):
        if imagen[int(p[1])][int(p[0])][0] == 0:
            return False
    return True


def removeNpArray(arreglo, elemento):
    for i in range(len(arreglo)):
        if(np.array_equal(arreglo[i], elemento)):
            return arreglo.pop(i)


'''MANIPULACION DE FILTROS'''
# para cargar el mapa
mapa = cv2.imread('mapa3.png')
gray = cv2.cvtColor(mapa, cv2.COLOR_BGR2GRAY)
cv2.imshow('mapa', gray)
ret, th1 = cv2.threshold(gray, 254, 255, cv2.THRESH_BINARY)
kernel = np.ones((11, 11), np.uint8)
# aplico un filtro de dilatacion. Este filtro hace que los puntos los puntos blancos se expandan
# probocando que algunos puntitos negros desaparecan #le pueden hacer un cv.imshow para que vean el resultado
th1 = cv2.dilate(th1, kernel, 1)
kernel = np.ones((11, 11), np.uint8)
# Despues aplico uno de erosion que hace lo opuesto al de dilatacion
th1 = cv2.erode(th1, kernel, 1)
# aplico un flitro gausiando de 5x5  para suavisar los bordes
th1 = cv2.GaussianBlur(th1, (5, 5), cv2.BORDER_DEFAULT)
# muestro como queda mi mapa
cv2.imshow('thres', th1)
# Aplico la deteccion de Esquinas de Harris. para mas informacion consulten https://docs.opencv.org/3.4/dc/d0d/tutorial_py_features_harris.html
dst = cv2.cornerHarris(th1, 2, 3, 0.05)
ret, dst = cv2.threshold(dst, 0.04*dst.max(), 255, 0)
dst = np.uint8(dst)
ret, th2 = cv2.threshold(th1, 235, 255, cv2.THRESH_BINARY)
th2 = cv2.dilate(th2, kernel, 1)
# aqui devuelvo la imagen binarizada a tres canales
th2 = cv2.cvtColor(th2, cv2.COLOR_GRAY2BGR)
# find centroids
ret, labels, stats, centroids = cv2.connectedComponentsWithStats(
    dst, 30, cv2.CV_32S)
vertices = np.int0(centroids)
'''FIN MANIPULACION FILTROS'''

aux1 = vertices
aux2 = vertices
verticesConectados = []
aristas = []
'''
verticesConectados es un arreglo de arreglos de la forma
[  [cordenadas a][cordenadas b][peso a-b]  ]
[   [[ax,ay],[bx,by], w]   ]
'''
# aqui voy a buscar cuales son las esquinas que estan conectadas
for h in range(len(aux1)):
    i = aux1[h]
    for k in range(h+1, len(aux2)):
        j = aux2[k]
        if estaConectado(th2, i, j, presiscion=32):
            lista_auxiliar = [i, j]
            aristas.append(lista_auxiliar)
            lista_auxiliar.append(calculaPeso(i, j))
            verticesConectados.append(lista_auxiliar)

# ordenanddo vertices
verticesConectados.sort(key=lambda x: x[2], reverse=False)
# elimino el peso
for vertice in verticesConectados:
    vertice.pop()

"""APLICANDO PRIM"""
# inicio en un punto aleatorio, y dibujo un circulo
start = verticesConectados[rint(0, len(verticesConectados)-1)][rint(0, 1)]
cv2.circle(th2, (start[0], start[1]), 20, (221, 160, 221), -1)

visitados = [start]
aristasArbolRM = []

pueden_faltar_vertices = True
while pueden_faltar_vertices:
    # empiezo
    pueden_faltar_vertices = False
    for i, v in enumerate(verticesConectados):
        if isInTheList(v[0], visitados) and (not isInTheList(v[1], visitados)):
            poped = verticesConectados.pop(i)
            # insertamos la arista (origen-destino)
            aristasArbolRM.append(poped)
            visitados.append(poped[1])  # solo queremos el que nos falta
            pueden_faltar_vertices = True
            break

        elif isInTheList(v[1], visitados) and (not isInTheList(v[0], visitados)):
            poped = verticesConectados.pop(i)
            # insertamos la arista (origen-destino)
            aristasArbolRM.append(poped)
            visitados.append(poped[0])  # solo queremos el que nos falta
            pueden_faltar_vertices = True
            break
"""FIN PRIM"""

# dibujar aristas
for arista in aristas:
    cv2.line(th2, tuple(arista[0]), tuple(arista[1]), (0, 255, 0), 1)
color = (180, 105, 255)
# dibujar árbol de recubrimiento mínimo
for rama in aristasArbolRM:
    cv2.line(th2, tuple(rama[0]), tuple(rama[1]), (167, 30, 60), 3)
# dibujar puntos
for point in vertices:
    cv2.circle(th2, (point[0], point[1]), 5, (255, 0, 0), -1)

# aqui muestro como quedo de chingon el grafo
cv2.imwrite('./mapa_grafo_resuldao_m1.png', th2)
cv2.imshow('points', th2)
cv2.waitKey()
cv2.destroyAllWindows()
