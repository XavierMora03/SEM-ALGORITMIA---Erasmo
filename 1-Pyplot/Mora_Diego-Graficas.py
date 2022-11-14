# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 12:01:13 2022

@author: Xavier
"""
import numpy as np
import matplotlib.pyplot as plt

def fdx(x):
    return x**4

def fdxPrima(x):
    return 4*x**3

def fdxPP(x):
    return 12*x**2

rango = np.arange(-5,5,.2)

plt.figure(figsize=(9, 7), dpi=80)

plt.title('Función 1')

plt.axis([-5,5,-75,150])
plt.text(2,-25,'F(x) = x^4',fontsize = 'large',  color = 'b')
plt.text(2,-32,'f(x) = 4x^3',fontsize = 'large',  color = 'r')
plt.text(2,-39,'f(x) = 12x^2',fontsize = 'large',  color = 'y')
# Función, derivada
plt.plot(rango,fdx(rango),'b-',rango,fdxPrima(rango),'r--')
plt.plot(rango,fdxPP(rango),'yo')

plt.tight_layout()
plt.savefig('filename.png', format='png',dpi = 120)
plt.savefig('filename.svg', format='svg')
plt.savefig('filename.eps')
