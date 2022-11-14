# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 11:06:06 2022

@author: GabrielMtz
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg

arr=[4,5,6,7,8,9,9,8,7,6,5]
'''
plt.plot(arr)
plt.ylabel('numeros')
plt.show()


plt.figure()
x1=[3,2,1,4]
x2=[1,4,9,16]
plt.plot(x1,x2)
plt.show()

plt.figure()
plt.plot(x1,x2,'ro')
plt.axis([0,20,0,10])
plt.grid()
plt.show()

plt.figure()
t=np.arange(0,5,.2)
plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'go')
plt.show()
'''
grupos=["grupo 1","grupo2","grupo3"]
valores=[1,10,100]
plt.figure()
plt.subplot(1,3,1)
plt.bar(grupos,valores)
plt.subplot(1,3,1)
plt.scatter(grupos,valores)
plt.subplot(1,3,1)
plt.plot(grupos,valores)
plt.suptitle("tipos de graficas")
plt.show()

'''
def f(x):
    y=x**3+x**2
    return y
def fPrima(x):
    return 3*x**2+2*x
t=np.arange(0,50,10)
plt.figure()
plt.plot(t,f(t),'k',t,fPrima(t),'bo')
plt.show()

img=mpimg.imread('lenna.jpg')
height,width,channels=img.shape
imgGray=np.zeros((height,width))
for i in range(height):
    for j in range(width):
        imgGray[i,j]=(int(img[i,j,0])\
            +int(img[i,j,1])+int(img[i,j,2]))//3
plt.figure()
plt.imshow(img)
plt.figure()
plt.imshow(imgGray,cmap=plt.cm.inferno)




'''
