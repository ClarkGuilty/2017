# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 16:53:47 2017

@author: Javier
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import SubplotParams as sp



def f(x):
    return x*x*x*x

def c(n):
    if(n == 0): 
        return (np.pi**4)/5
    n = np.abs(n)
    a= 4*(np.pi**2)/(n*n)
    b = 24/(n**4)
    c = a-b
    if(n%2 == 1):
        return -1*c
    return c
    
    
def r(x):
    x = (x+np.pi) % (2*np.pi) - np.pi
    return f(x)
    
    
def g(x,N):
    g = 0
    for i in range(-N,N+1):
        g += c(i)*np.cos(i*x)
    return g
        
x = np.linspace(-2*np.pi, 2*np.pi, 200)
#q = plt.plot(x,r(x))
o = g(x,1)



#fig = plt.figure()

#ax1 = fig.add_subplot(211)

#ax1.plot(x,r(x), label = "g(x)")
#ax1.plot(x,g(x,1))
#    
#plt.legend(loc=0)

#if(True):
with plt.xkcd():
    
    he = sp(hspace = 0.5)
    fig = plt.figure(subplotpars = he)
    plt.title("Punto 1.1.b: x^4 y su serie de Fourier")
    
    ax1 = fig.add_subplot(311)

    ax1.plot(x,r(x), label = "x^4", color = 'black')
    ax1.plot(x,g(x,2), label = "Aproximacion con N = 2",color = 'b')
    
    h1 = plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    #plt.savefig("Anomalies_SOI_Plot.png",bbox_extra_artists=(h,), bbox_inches='tight')

    ax2 = fig.add_subplot(312)
    
    
    ax2.plot(x,r(x), label = "x^4",  color = 'black')
    ax2.plot(x,g(x,5), label = "Aproximacion con N = 5", color = 'b')

    h2= plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    
    ax3 = fig.add_subplot(313)
    
    ax3.plot(x,r(x), label = "x^4", color = 'black')
    ax3.plot(x,g(x,20), label = "Aproximacion con N = 20", color = 'b')

    h3= plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))


    plt.savefig("heh.png",bbox_extra_artists=(h1,h2,h3,), bbox_inches='tight')













