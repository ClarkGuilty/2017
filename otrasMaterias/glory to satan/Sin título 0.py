# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 20:47:46 2017

@author: Javier
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit



largo = np.loadtxt("largo.dat")
pixeles = len(largo[:,0])
largo = 0.01 #cm
densidad = largo/(pixeles-1)


fig = plt.figure()

#for i in range(1,5):
#    data = np.loadtxt("g"+str(i)+".dat")
#    plt.plot(data[:,0],data[:,1])

#632.8

i = 5

#data = np.loadtxt("n"+str(i)+".dat")
#plt.plot(data[:,0],data[:,1], label = ("n"+str(i)+".dat") )
#plt.legend(loc = 3)
#a = 33
#b = 186
#g = a-b
#plt.xlim(a,b)

datag = np.loadtxt("g.txt")
def lar(x, lamb):
  return lamb*1.53/0.00015


x = datag[:,0]
g = datag[:,1]*densidad


var, diff = curve_fit(lar,x,g)

print x
print var*1000000000
print np.sqrt(np.trace(diff))*1000000000



