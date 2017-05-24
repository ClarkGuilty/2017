# -*- coding: utf-8 -*-
"""
Created on Wed May 24 00:47:01 2017

@author: Javier Alejandro Acevedo Barroso
"""
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("CircuitoRC (copy).txt")
t = data[:,0]
q = data[:,1]


h = plt.figure()
plt.scatter(t,q)
plt.savefig("heh.png")



def prob(y0, y):
	chi_squared = (1.0/2.0)*sum((y0-y)**2)
	return exp(-chi_squared)

def func(t,R,C):
	return 10*C*(1.0-np.exp(-t/(R*C)))
