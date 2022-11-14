#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 11:46:29 2019

@author: gabriel
"""

import numpy as np
import matplotlib.pyplot as plt
import time
import random
import matplotlib.animation as manimation


#matplotlib.use('TkAgg')
random.seed(10)
np.random.seed(10)

def busquedaBinaria(lista,elemento):
    izq=0
    der=len(lista)-1
    iterations=0
    while izq<=der:
        mitad=(izq+der)//2
#        print(mitad,' ',izq,' ',der,' ',lista[mitad])
        if lista[mitad]==elemento:
            return mitad,iterations
        elif(elemento<lista[mitad]):
            der=mitad-1
        else:
            izq=mitad+1
        iterations+=1
    return -1,iterations

def busquedaLineal(lista,elemento):
    for idx,x in enumerate(lista):
        if x==elemento:
            return x,idx+1

elementNumArray=[100,200,400,800,1600,3200,6400,12800,25600,51200,102400,204800,204800*2,204800*4]

elementNumArray=[100,200,400,800,1600,3200,6400,12800]
#elementNumArray=np.arange(100,204800,100)
tiemposBi=[]
iteracionesBi=[]
tiemposLi=[]
iteracionesLi=[]

FFMpegWriter = manimation.writers['ffmpeg']

metadata = dict(title='Busqueda Lineal vs Binaria', artist='Gabriel Martinez',comment='Deja tu  like')
writer = FFMpegWriter(fps=24, metadata=metadata)

fig, (ax1, ax2) = plt.subplots(1, 2,figsize=(18,9))
ax1.title.set_text('Busqueda Lineal')
ax2.title.set_text('Busqueda Binaria')
ax1.set_ylabel("Consultas")
ax1.set_xlabel("# Elementos")
ax2.set_xlabel("# Elementos")
               
with writer.saving(fig, "BusquedaLinealVsBinaria.mp4", 100):

    plt.ion()
    for idx,elementNum in enumerate(elementNumArray):
        lista=np.sort(np.linspace(0,100000,elementNum))
        
        start=time.time()
        elemento,it=busquedaBinaria(lista,lista[-1])    
        finish=time.time() 
        iteracionesBi.append(it)
        tiemposBi.append(finish-start)
        
        start=time.time()
        elemento,it=busquedaLineal(lista,lista[-1]) 
        finish=time.time()
        iteracionesLi.append(it)
        tiemposLi.append(finish-start)
        
        ax1.plot(elementNumArray[:idx+1], iteracionesLi, 'r-',label='Lineal')
        ax2.plot(elementNumArray[:idx+1], iteracionesBi, 'b--',label='Binaria')

        fig.canvas.draw()
        fig.canvas.flush_events()
        plt.show(block=False)

        time.sleep(.1)
        for i in range(24):
         writer.grab_frame()

#fig, ax = plt.subplots()
#line1, =ax.plot(elementNumArray,tiempos)
#line1, =ax.plot(elementNumArray,iteraciones)
#plt.show()

