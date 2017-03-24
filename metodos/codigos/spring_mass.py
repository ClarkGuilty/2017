# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 07:39:04 2017

@author: Javier
"""
import numpy as np
import matplotlib.pyplot as plt

h=0.01
min_x = 0
max_x = 6.0
n_points = int((max_x-min_x)/h)
x = np.zeros(n_points)
y_1 = np.zeros(n_points)
y_2 = np.zeros(n_points)

k = 42
g = 9.8
m = 0.25
u = 0.15

def func_prime_1(x, y_1, y_2):
    return y_2

def func_prime_2(x, y_1, y_2):
    a = -k*y_1
    b = -u*m*g
    
    if(y_2>0):
        b = -b
    return a+b
    
    
#we use our initial conditions
x[0] = min_x
y_1[0] = 0.2
y_2[0] = 0.0

for i in range(1,n_points):
    #get the first derivatives
    y_prime_1 = func_prime_1(x[i-1], y_1[i-1], y_2[i-1])
    y_prime_2 = func_prime_2(x[i-1], y_1[i-1], y_2[i-1])
    

    x[i] = x[i-1] + h
    y_1[i] = y_1[i-1] + h * func_prime_1(x[i-1], y_1[i-1], y_2[i-1])
    y_2[i] = y_2[i-1] + h * func_prime_2(x[i-1], y_1[i-1], y_2[i-1])
    

f = plt.plot(x,y_1, label = "Posicion del resorte")
plt.plot(x,y_2, label = "Velocidad del resorte")
plt.xlabel("Tiempo transcurrido (s)")
plt.ylabel("Posicion de la particula (m)")
plt.legend(loc=0)

plt.savefig("spring_mass.png")

    
