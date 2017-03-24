# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 16:27:29 2017

@author: Javier Acevedo
"""

import numpy as np
import matplotlib.pyplot as plt


dataSOI = np.loadtxt("SOI.txt", skiprows = 1, usecols = range(1,13))

SOI = dataSOI[0,:]

for i in range(104,141):
    SOI = np.concatenate((SOI,dataSOI[i,:]), axis=0)

    
dataTemp = np.loadtxt("heat_content_index.txt", skiprows = 4)
T1 = dataTemp[:,2]
T2 = dataTemp[:,3]
T3 = dataTemp[:,4]

x = np.linspace(1979,2016,len(T1))




fig = plt.figure()

ax1 = fig.add_subplot(211)
ax1.plot(x,T1, label = "130E, 80W")
ax1.plot(x,T2,label = "160E, 80W")
ax1.plot(x,T3,label ="180W, 100W")
h = plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.ylabel("Anomalias de temperatura (K)")
plt.xlim((1978,2017))

ax2 = fig.add_subplot(212)
ax2.plot(x,SOI, label = "Datos de SOI", color = "orange")
t = np.linspace(0,len(SOI),len(SOI))
plt.xlim((1978,2017))
plt.ylabel("SOI")
plt.xlabel("Meses desde enero de 1979")

h = plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("Anomalies_SOI_Plot.pdf",bbox_extra_artists=(h,), bbox_inches='tight')



av1 = np.average(T1)
av2 = np.average(T2)
av3 = np.average(T3)
avS = np.average(SOI)

T1 = T1 - np.average(T1)
T2 = T2 - np.average(T2)
T3 = T3 - np.average(T3)
SOI = SOI - np.average(SOI)

matriz = np.array([T1,T2,T3,SOI])

cMatriz = np.cov(matriz)

#eiVal = np.linalg.eigvals(cMatriz)
#print eiVal

val, vec = np.linalg.eig(cMatriz)
#print eiVec

sort = val.argsort()
#vec = vec[sort]

pV1 = vec[0]
pV2 = vec[1]

pV = np.array([pV1,pV2])

#pV = np.array([pV1,pV2,vec[2],vec[3]])

#print "Los componentes principales son:"
#print cMatriz


data = np.dot(pV,matriz)

#print data
#print "Datos originales"
#print data.shape
#print pV.shape
#print matriz.shape
#print val
#print vec
#print pV

fig = plt.figure(figsize=(4,13))
ax = plt.axes()
plt.scatter(data[0,:], data[1,:], label = "Nuevos datos")
x_line = np.linspace(-15.5,15)
plt.plot(x_line, x_line*pV[1,3]/pV[0,3], linewidth=5.0, label = "Componente mas importante")
plt.plot(x_line, -1*x_line*pV[0,3]/pV[1,3], linewidth=5.0, label = "Segundo componente")
#plt.plot(x_line, x_line*pV[1,3]/pV[0,3], linewidth=5.0)
#plt.plot(x_line, x_line*pV[1,0]/pV[0,0], linewidth=5.0)
ax.set_aspect(1.0)
h = plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("PCA_Anomalies_SOI_Plot.pdf",bbox_extra_artists=(h,), bbox_inches='tight')


#[[-0.38514492  0.80056286 -0.45903076  0.00729768]
# [ 0.82017867  0.06897864 -0.56751467  0.02181731]]



#principal = np.dot( matriz.T,pV.T).T         # change of basis
#        
#print principal.shape




#x,y = matriz[0],matriz[1]
#second, principal = np.dot( matriz.T,pV.T).T      # change of basis
#        
#fig = plt.figure(figsize=(10,4))
#ax1 = fig.add_subplot(121, projection='4d')
#        
#ax1.scatter(x, y, z,w)
#ax1.set_xlabel('$x$')
#ax1.set_ylabel('$y$')
#ax1.set_zlabel('$z$')
#
#        
#ax2 = fig.add_subplot(122, projection='3d')
#        
#ax2.scatter(principal, second, third)
#        
#min_principal = min(principal)
#max_principal = max(principal)
#ax2.set_ylim(min_principal, max_principal)      # makes x, y and z lims equal
#ax2.set_zlim(min_principal, max_principal)
#        
#ax2.set_xlabel('1st Principal Component', fontsize=10)
#ax2.set_ylabel('2nd Principal Component', fontsize=10)
#ax2.set_zlabel('3rd Principal Component', fontsize=10)






#t1,t2,t3,soi= np.dot(pV.T,data)


#fig = plt.figure()

#ax1 = fig.add_subplot(311)
#ax1.plot(x,t1+av1, label = "130E, 80W")
#ax1.plot(x,t2+av2,label = "160E, 80W")
#ax1.plot(x,t3+av3,label ="180W, 100W")
#h = plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#plt.ylabel("Anomalias de temperatura (K)")
#plt.xlim((1978,2017))

#ax2 = fig.add_subplot(312)
#t = np.linspace(0,len(SOI),len(SOI))
#ax2.plot(x,soi+avS, label = "Datos de SOI", color = "orange")
#plt.xlim((1978,2017))
#h = plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#plt.ylabel("SOI")
#plt.xlabel("Meses desde enero de 1979")
#plt.savefig("Anomalies_SOI_Plot,ot.pdf",bbox_extra_artists=(h,), bbox_inches='tight')





