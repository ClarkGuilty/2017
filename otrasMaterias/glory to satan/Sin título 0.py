# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 20:47:46 2017

@author: Javier
"""

import numpy as np
import matplotlib.pyplot as plt



largo = np.loadtxt("largo.dat")
pixeles = len(largo[:,0])
largo = 1.0 #m
densidad = largo/pixeles


fig = plt.figure()

#for i in range(1,5):
#    data = np.loadtxt("g"+str(i)+".dat")
#    plt.plot(data[:,0],data[:,1])


i = 5

data = np.loadtxt("n"+str(i)+".dat")
plt.plot(data[:,0],data[:,1], label = ("n"+str(i)+".dat") )
plt.legend(loc = 3)
a = 33
b = 186
g = a-b
plt.xlim(a,b)

