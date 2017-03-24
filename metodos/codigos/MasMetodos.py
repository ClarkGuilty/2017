# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 20:49:23 2017

@author: Javier
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import SubplotParams as sp



A = 1.0
def f(x):
    return x*x*A

def c(n):
    if(n == 0): 
        return (A/3)
    n = np.abs(n)
    a= 2*A
    b = n*n*np.pi*np.pi
    c = a/b
    if(n%2 == 1):
        return -1*c
    return c
    
    
def r(x):
    x = (x+1) % (2) - 1
    return f(x)
    
    
def g(x,N):
    l = 0
    for i in range(-N,N+1):
        l += c(i)*np.cos(i*x*np.pi)
    return l
        
x = np.linspace(-3, 3, 200)
#q = plt.plot(x,r(x))
o = g(x,10)
k = r(x)

aprox = o.mean()
areal = k.mean()


#fig = plt.figure()

#ax1 = fig.add_subplot(211)

#ax1.plot(x,r(x), label = "g(x)")
#ax1.plot(x,g(x,1))
#    
#plt.legend(loc=0)

#with plt.xkcd():
if(True):
    
    he = sp(hspace = 0.5)
    fig = plt.figure(subplotpars = he)
    plt.title("Punto 1.1.b: g(x) y su serie de Fourier")
    
    ax1 = fig.add_subplot(311)

    ax1.plot(x,r(x), label = "g(x)")
    ax1.plot(x,g(x,2), label = "Aproximacion con N = 2")
    
    h1 = plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    #plt.savefig("Anomalies_SOI_Plot.png",bbox_extra_artists=(h,), bbox_inches='tight')

    ax2 = fig.add_subplot(312)
    
    
    ax2.plot(x,r(x), label = "g(x)")
    ax2.plot(x,g(x,5), label = "Aproximacion con N = 5", color = 'red')

    h2= plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    
    ax3 = fig.add_subplot(313)
    
    ax3.plot(x,r(x), label = "g(x)")
    ax3.plot(x,g(x,20), label = "Aproximacion con N = 20", color = 'red')

    h3= plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))


    plt.savefig("noHeh.png",bbox_extra_artists=(h1,h2,h3,), bbox_inches='tight')
