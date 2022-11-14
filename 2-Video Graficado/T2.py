# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 16:39:43 2022

@author: Xavier
"""

import matplotlib.pyplot as plt
import matplotlib.animation as manimation
import numpy as np
import os
import random
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
    

'''
        
random.seed()

mylist =[]
for i in range( 10):
    mylist.append(random.randint(0,1000))
    
   
mylist2 = mylist.copy()

contt = 0
l4,contt = quickSort(mylist2,0,len(mylist)-1)
print(mylist2)
print(l4)


print(contt)


'''


elementNumArray=[100,200,400,800,1600,3200,6400,12800]

tiemposQuick =[]
iteracionesQuick = []
tiemposBubble = []
iteracionesBubble = []

FFMpegWriter = manimation.writers['ffmpeg']

metadata = dict(title='BubbleSort Mejorado vs QuickSort', artist='Diego Mora',
                comment='Deja tu  like')
writer = FFMpegWriter(fps=24, metadata=metadata)

fig, (ax1, ax2) = plt.subplots(1, 2,figsize=(18,9))
ax1.title.set_text('Busqueda Lineal')
ax2.title.set_text('Busqueda Binaria')
ax1.set_ylabel("Consultas")
ax1.set_xlabel("# Elementos")
ax2.set_xlabel("# Elementos")

lista = []
for i in range(13000):
    lista.append(random.randint(0,100000))
    
    

with writer.saving(fig, "BubbleSort Mejorado vs QuickSort", 100):

    plt.ion()
    for idx,elementNum in enumerate(elementNumArray):
        #lista=np.linspace(0,100000,elementNum)
        
        it = 0 
        start=time.time()
        l1,it = burbujaMejorada(lista[:elementNum-1])    
        finish=time.time() 
        iteracionesBubble.append(it)
        tiemposBubble.append(finish-start)
        
        it =0
        start=time.time()
        l2, it=quickSort(lista[:elementNum-1], 0, elementNum-1)#OJO esta bien
        finish=time.time()
        iteracionesQuick.append(it)
        tiemposQuick.append(finish-start)
        
        ax1.plot(elementNumArray[:idx+1], iteracionesBubble, 'r-',label='Lineal')
        ax2.plot(elementNumArray[:idx+1], iteracionesQuick, 'b--',label='Binaria')

        fig.canvas.draw()
        fig.canvas.flush_events()
        plt.show(block=False)

        time.sleep(.1)
        for i in range(24):
         writer.grab_frame()

print(tiemposBubble,'\n\n',tiemposQuick)
