# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 23:30:31 2017

@author: Javier
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("datos.dat")
x = data[:,0]
y = data[:,1]
dx = data[:,2]
dy = data[:,3]

h = plt.figure()
#plt.scatter(x,y)
plt.errorbar(x,y,dx,dy, color = 'black',ecolor = 'red', label = "Datos")
plt.title("Densidad del metal contra Rata de las masas" )
plt.xlabel("Rata de las masas")
plt.ylabel("Densidad del metal (g/cm^3)")

cof = np.polyfit(x,y,1)

t = np.linspace(2,9,50)
plt.plot(t,cof[0]*t+cof[1], color = 'g', label = "Regresion")
plt.legend(loc=0)
