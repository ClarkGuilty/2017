# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 15:00:30 2017

@author: Javier Alejandro Acevedo Barroso
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D  


x = np.linspace(0,1,100)
y = np.linspace(0,1,100)

#
#Condiciones 1, t=0, fronteras cerradas
c1t0 = np.loadtxt("c1t0.txt")
fc1t0 = plt.figure(dpi= 1000)
ax = fc1t0.gca(projection="3d")
X, Y = np.meshgrid(x,y)
pc1t0 = ax.plot_surface(X,Y,c1t0, cmap=cm.plasma)
cb = fc1t0.colorbar(pc1t0, pad =0.1 , shrink = 0.8)
ax.set_xlabel("x [m]")
ax.set_ylabel("y [m]")
ax.set_zlabel("T [C]")
ax.set_title("Condiciones iniciales")
#ax.w_zaxis.line.set_lw(0.)
#ax.set_zticks([])
plt.savefig("t0.png")

#Condiciones 1, t = 100, con fronteras cerradas
c1t100 = np.loadtxt("c1t100c.txt")
fc1t100 = plt.figure(dpi= 1000)
ax = fc1t100.gca(projection="3d")
X, Y = np.meshgrid(x,y)
pc1t100 = ax.plot_surface(X,Y,c1t100, cmap=cm.plasma)
cb = fc1t100.colorbar(pc1t100, pad =0.1 , shrink = 0.8)
ax.set_xlabel("x [m]")
ax.set_ylabel("y [m]")
ax.set_zlabel("T [C]")
#ax.w_zaxis.line.set_lw(0.)
#ax.set_zticks([])
ax.set_title("t = 100 para fronteras cerradas y caso 1")
plt.savefig("c1t100c.png")


#Condiciones 1, t = 2500, con fronteras cerradas
c1t2500 = np.loadtxt("c1t2500c.txt")
fc1t2500 = plt.figure(dpi= 1000)
ax = fc1t2500.gca(projection="3d")
X, Y = np.meshgrid(x,y)
pc1t2500 = ax.plot_surface(X,Y,c1t2500, cmap=cm.plasma)
cb = fc1t2500.colorbar(pc1t2500, pad =0.1 , shrink = 0.8)
ax.set_xlabel("x [m]")
ax.set_ylabel("y [m]")
ax.set_zlabel("T [C]")
ax.w_zaxis.line.set_lw(0.)
ax.set_zticks([])
ax.set_title("t = 2500 para fronteras cerradas y caso 1")
plt.savefig("c1t2500c.png")



#Condiciones 2, t = 100, con fronteras cerradas
c2t100 = np.loadtxt("c2t100c.txt")
fc2t100 = plt.figure(dpi= 1000)
ax = fc2t100.gca(projection="3d")
X, Y = np.meshgrid(x,y)
pc2t100 = ax.plot_surface(X,Y,c2t100, cmap=cm.plasma)
cb = fc2t100.colorbar(pc2t100, pad =0.1 , shrink = 0.8)
ax.set_xlabel("x [m]")
ax.set_ylabel("y [m]")
ax.set_zlabel("T [C]")
#ax.w_zaxis.line.set_lw(0.)
#ax.set_zticks([])
ax.set_title("t = 100 para fronteras cerradas y caso 2")
plt.savefig("c2t100c.png")

#Condiciones 2, t = 2500, con fronteras cerradas
c2t2500 = np.loadtxt("c2t2500c.txt")
fc2t2500 = plt.figure(dpi= 1000)
ax = fc2t2500.gca(projection="3d")
X, Y = np.meshgrid(x,y)
pc2t2500 = ax.plot_surface(X,Y,c2t2500, cmap=cm.plasma)
cb = fc2t2500.colorbar(pc2t2500, pad =0.1 , shrink = 0.8)
ax.set_xlabel("x [m]")
ax.set_ylabel("y [m]")
ax.set_zlabel("T [C]")
#ax.w_zaxis.line.set_lw(0.)
#ax.set_zticks([])
ax.set_title("t = 2500 para fronteras cerradas y caso 2")
plt.savefig("c2t2500c.png")



#Condiciones 1, t = 100s, fronteras periodicas
qwe = np.loadtxt("c1t100p.txt")
fc3t0 = plt.figure()
ax = fc3t0.gca(projection="3d")
X, Y = np.meshgrid(x,y)
pc3t0 = ax.plot_surface(X,Y,qwe, cstride = 10, rstride = 10, cmap = cm.plasma)
cb = fc3t0.colorbar(pc3t0, pad =0.1 , shrink = 0.8)
ax.set_xlabel("x [m]")
ax.set_ylabel("y [m]")
ax.set_zlabel("T [C]")
#ax.w_zaxis.line.set_lw(0.)
#ax.set_zticks([])
ax.set_title("t = 100 para fronteras periodicas y caso 1")

plt.savefig("c1t100p.png")


#Condiciones 1, t = 2500s, fronteras periodicas
asd = np.loadtxt("c1t2500p.txt")
fc3t0 = plt.figure()
ax = fc3t0.gca(projection="3d")
X, Y = np.meshgrid(x,y)
pc3t0 = ax.plot_surface(X,Y,asd, cstride = 10, rstride = 10, cmap = cm.plasma)
cb = fc3t0.colorbar(pc3t0, pad =0.1 , shrink = 0.8)
ax.set_xlabel("x [m]")
ax.set_ylabel("y [m]")
ax.set_zlabel("T [C]")
#ax.w_zaxis.line.set_lw(0.)
#ax.set_zticks([])
ax.set_title("t = 2500 para fronteras periodicas y caso 1")
plt.savefig("c1t2500p.png")



#Condiciones 2, t = 100s, fronteras periodicas
zxc = np.loadtxt("c2t100p.txt")
fc3t0 = plt.figure()
ax = fc3t0.gca(projection="3d")
X, Y = np.meshgrid(x,y)
pc3t0 = ax.plot_surface(X,Y,zxc, cstride = 10, rstride = 10, cmap = cm.plasma)
cb = fc3t0.colorbar(pc3t0, pad =0.1 , shrink = 0.8)
ax.set_xlabel("x [m]")
ax.set_ylabel("y [m]")
ax.set_zlabel("T [C]")
#ax.w_zaxis.line.set_lw(0.)
#ax.set_zticks([])
ax.set_title("t = 100 para fronteras periodicas y caso 2")
plt.savefig("c2t100p.png")


#Condiciones 2, t = 2500s, fronteras periodicas
sdf = np.loadtxt("c2t2500p.txt")
fc3t0 = plt.figure()
ax = fc3t0.gca(projection="3d")
X, Y = np.meshgrid(x,y)
pc3t0 = ax.plot_surface(X,Y,sdf, cstride = 10, rstride = 10, cmap = cm.plasma)
cb = fc3t0.colorbar(pc3t0, pad =0.1 , shrink = 0.8)
ax.set_xlabel("x [m]")
ax.set_ylabel("y [m]")
ax.set_zlabel("T [C]")
#ax.w_zaxis.line.set_lw(0.)
#ax.set_zticks([])
ax.set_title("t = 2500 para fronteras periodicas y caso 2")
plt.savefig("c2t2500p.png")




temperaturas = np.loadtxt("Tmean.txt")

T1c = temperaturas[:,0]
T1p = temperaturas[:,1]
T2c = temperaturas[:,2]
T2p = temperaturas[:,3]

t = np.linspace(0,2500,10000)

h = plt.figure()
plt.plot(t,T1c)
plt.xlabel("Tiempo transcurrido [s]")
plt.ylabel("Temperatura media [C]")
plt.title("T media vs tiempo para caso 1, condiciones de frontera cerradas")
plt.savefig("TmeanC1c")

h = plt.figure()
plt.plot(t,T1p)
plt.xlabel("Tiempo transcurrido [s]")
plt.ylabel("Temperatura media [C]")
plt.title("T media vs tiempo para caso 1, condiciones de frontera periodicas")
plt.savefig("TmeanC1p")

h = plt.figure()
plt.plot(t,T2c)
plt.xlabel("Tiempo transcurrido [s]")
plt.ylabel("Temperatura media [C]")
plt.title("T media vs tiempo para caso 2, condiciones de frontera cerradas")
plt.savefig("TmeanC2c")

h = plt.figure()
plt.plot(t,T2p)
plt.xlabel("Tiempo transcurrido [s]")
plt.ylabel("Temperatura media [C]")
plt.title("T media vs tiempo para caso 2, condiciones de frontera periodicas")
plt.savefig("TmeanC2p")






