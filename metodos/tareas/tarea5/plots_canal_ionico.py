# -*- coding: utf-8 -*-
"""
Created on Tue May 23 21:18:22 2017

@author: Javier Alejandro Acevedo Barroso
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

dat1 = np.loadtxt("Canal_ionico.txt")
dat2 = np.loadtxt("Canal_ionico1.txt")
res = np.loadtxt("resultados.txt")
res0 = np.loadtxt("res1.txt")
res1 = np.loadtxt("res2.txt")
x1 = dat1[:,0]
y1 = dat1[:,1]
x2 = dat2[:,0]
y2 = dat2[:,1]

px0 = res[0][0]
py0 = res[0][1]
R0 = res[0][2]

px1 = res[1][0]
py1 = res[1][1]
R1 = res[1][2]
#y0 = 5.2
#R = 6.29

#x0 = 3.37
#y0 = 5.2
#R = 6.29


fig = plt.gcf()
ax = fig.gca()

#Primera figura.
plt.scatter([px0], [py0])
c0 = plt.Circle((px0,py0), R0, fill = False)
ax.add_artist(c0)
plt.scatter(x1,y1)
plt.savefig("g1.png")


#Segunda figura.
h = plt.figure()
fig = plt.gcf()
ax = fig.gca()

plt.scatter([px1], [py1])
c1 = plt.Circle((px1,py1), R1, fill = False)
ax.add_artist(c1)
plt.scatter(x2,y2)
plt.savefig("g2.png")


#Histogramas
noH = plt.figure()
plt.hist2d(res0[:,0], res0[:,1], bins = 100, range = [[-5,16], [-5,20]])
#plt.hist(res0[:,0], bins = 100)
plt.savefig("his1.png")

noHindeed = plt.figure()
plt.hist2d(res1[:,0], res1[:,1], bins = 100, range = [[-5,16], [-5,20]])
#plt.hist(res1[:,0], bins = 100)
plt.savefig("his2.png")







