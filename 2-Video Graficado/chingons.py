# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 20:08:41 2022

@author: Xavier
"""

import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

def burbujaMejorada(P):
    cont = 0
    L = P.copy()
    long = len(L)
    
    isSorted = False
    for k in range(1,long):
        
        if isSorted:
            break
        
        isSorted = True
        
        for i in range(1,long):
            if L[i]<L[i-1]:
                aux = L[i]
                L[i] = L[i-1]
                L[i-1] = aux
                isSorted = False
                cont += 1
    return L,cont
                
def partition(array, low, high):
    pivot = array[high]
    cont = 0
    
    
    i = low - 1
    for j in range(low, high):
      if array[j] <= pivot:
        i = i + 1
        (array[i], array[j]) = (array[j], array[i])
        cont += 1

    # swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # return the position from where partition is done
    return i + 1,cont

 

def quickSort1(array, low, high):
    if low < high:
        
        pi,cont = partition(array, low, high)
        cont += quickSort1(array, low, pi - 1)
        cont += quickSort1(array, pi + 1, high)

        return cont
    return 0


def quickSort(array1, low, high):
    array = array1.copy()
    
    cont = quickSort1(array, low, high)
    
    return array,cont


# Settings
video_file = "elquick.mp4"
clear_frames = True     # Should it clear the figure between each frame?
fps = 60

# Output video writer
FFMpegWriter = animation.writers['ffmpeg']
metadata = dict(title='BUBBLE SORT MEJORADO vs QUICK SORT', artist='Diego Mora',
                comment='Movie support!')
writer = FFMpegWriter(fps=fps, metadata=metadata)


#fig
fig = plt.figure()
fig, (ax1, ax2) = plt.subplots(1, 2,figsize=(18,9))
ax1.title.set_text('BUBBLE SORT MEJORADO')
ax2.title.set_text('QUICK SORT')
ax1.set_ylabel("Consultas")
ax1.set_xlabel("# Elementos")
ax2.set_xlabel("# Elementos")





#mis variables
lista = []
for i in range(204800*2):
    lista.append(random.randint(0,1000000))
    
elementNumArray=[20,40,80,160,320,640,1280,2560,5102,10240,1024*20]

tiemposQuick =[]
iteracionesQuick = []
tiemposBubble = []
iteracionesBubble = []

with writer.saving(fig, video_file, 100):
    for idx,elementNum in enumerate(elementNumArray):
        
        
        it = 0 
        start=time.time()
        l1,it = burbujaMejorada(lista[:elementNum-1])    
        finish=time.time() 
        iteracionesBubble.append(it)
        tiemposBubble.append(finish-start)
        
        it =0
        start=time.time()
        l2, it=quickSort(lista[:elementNum-1], 0, elementNum-2)#OJO esta bien
        finish=time.time()
        iteracionesQuick.append(it)
        tiemposQuick.append(finish-start)
        
       
        #if clear_frames:
       #     fig.clear()
        ax1.plot(elementNumArray[:idx+1], iteracionesBubble, 'r-',label='Lineal')
        ax2.plot(elementNumArray[:idx+1], iteracionesQuick, 'b--',label='Binaria')
        for i in range(60):
            writer.grab_frame()

