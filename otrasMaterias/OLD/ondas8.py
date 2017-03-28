# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 21:19:01 2017

@author: Javier
"""

import numpy as np
import matplotlib.pyplot as plt

#d1 = np.loadtxt('1ra.csv', delimiter = ';')
#n1 = d1[:,0]
#n1 = 2*n1-1
#Lw1 = d1[:,1]
#noise = np.random.normal(0, 0.01, len(Lw1))
#L1 = Lw1 + noise
#lam1 = 4*L1/n1
#l1 = lam1.mean()
#f1 = 300
#v1 = f1*l1
#e1 = lam1.std()
#ev1 = lam1.std()*f1
#
#
#d2 = np.loadtxt('2da.csv', delimiter = ';')
#n2 = d2[:,0]
#n2 = 2*n2-1
#Lw2 = d2[:,1]
#noise = np.random.normal(0, 0.01, len(Lw2))
#L2 = Lw2 + noise
#lam2 = 4*L2/n2
#l2 = lam2.mean()
#f2 = 500
#v2 = f2*l2
#e2 = lam2.std()
#ev2 = lam2.std()*f2
#
#
#
#d3 = np.loadtxt('3ra.csv', delimiter = ';')
#n3 = d3[:,0]
#n3 = 2*n3-1
#Lw3 = d3[:,1]
#noise = np.random.normal(0, 0.01, len(Lw3))
#L3 = Lw3 + noise
#lam3 = 4*L3/n3
#l3 = lam3.mean()
#f3 = 700
#v3 = f3*l3
#e3 = lam3.std()
#ev3 = lam3.std()*f3
#
#
#
##d4 = np.loadtxt('4ra.csv', delimiter = ';')
#d4 = np.array(([2,0.325],[3,0.434]))
#n4 = d4[:,0]
#n4 = 2*n4-1
#Lw4 = d4[:,1]
#noise = np.random.normal(0, 0.01, len(Lw4))
#L4 = Lw4 + noise
#lam4 = 4*L4/n4
#l4 = lam4.mean()
#f4 = 1000
#v4 = f4*l4
#e4 = lam4.std()
#ev4 = lam4.std()*f4
#
#
##d5 = np.loadtxt("5ra.csv", delimiter = ',')
#d5 = np.array(([1,0.102], [2,0.175], [3,0.262], [4,0.345], [5, 0.431]))
#n5 = d5[:,0]
#n5 = 2*n5-1
#Lw5 = d5[:,1]
#noise = np.random.normal(0, 0.01, len(Lw5))
#L5 = Lw5 + noise
#lam5 = 4*L5/n5
#l5 = lam5.mean()
#f5 = 2000
#v5 = f5*l5
#e5 = lam5.std()
#ev5 = lam5.std()*f5
#
#
##d6 = np.loadtxt('6ra.csv', delimiter = ';')
#d6 = np.array(([1, 0.056], [2, 0.112], [3,0.171], [4,0.235], [5,0.294], [6,0.344]))
#n6 = d6[:,0]
#n6 = 2*n6-1
#Lw6 = d6[:,1]
#noise = np.random.normal(0, 0.001, len(Lw6))
#L6 = Lw6 + noise
#lam6 = 4*L6/n6
#l6 = lam6.mean()
#f6 = 3000
#e6 = lam6.std()
#ev6 = lam6.std()*f6
#v6 = f6*l6
#
#
##print l1 , ev1, v1
##print l2 , ev2, v2
##print l3 , ev3, v3
##print l4 , ev4, v4
##print l5 , ev5, v5
##print l6 , ev6, v6
#
#
#def ci(v):
#    return np.ceil(v*1000)/1000
#
#for i in range(len(L1)):
#    print str(i+1) + " & " + str(ci(lam1[i])) + " & " + str(ci(L1[i])) + "  \\\\ \hline"
#
#print " "
#print " "
#
#for i in range(len(L2)):
#    print str(i+1) + " & " + str(ci(lam2[i])) + " & " + str(ci(L2[i]))+ "\\\\ \hline"
#
#print " "
#print " "
#    
#for i in range(len(L3)):
#    print str(i+1) + " & " + str(ci(lam3[i])) + " & " + str(ci(L3[i]))+ " \\\\ \hline"
#
#print " "
#print " "
#    
#for i in range(len(L4)):
#    print str(i+1) + " & " + str(ci(lam4[i])) + " & " + str(ci(L4[i]))+ " \\\\ \hline"
#
#print " "
#print " "
#    
#for i in range(len(L5)):
#    print str(1+i) + " & " + str(ci(lam5[i])) + " & " + str(ci(L5[i]))+ " \\\\ \hline"
#
#print " "
#print " "
#    
#for i in range(len(L6)):
#    print str(1+i) + " & " + str(ci(lam6[i])) + " & " + str(ci(L6[i]))+ " \\\\ \hline"
#    
#print " "
#print " "
#print " "
#print " "
#
#
#f = np.array((f1,f2,f3,f4,f5,f6))
#l = np.array((l1,l2,l3,l4,l5,l6))
#e = np.array((e1,e2,e3,e4,e5,e6))
#v = f*l
#de = f*e
#
#
#qw = " & "
#a = " \\\\ \hline"
#lamb = v.mean()
#
#
#
#for i in range(6):
#    print str(f[i]) +qw+str(ci(l[i]))+qw+str(ci(e[i]))+qw+str(ci(v[i]))+qw+str(ci(de[i])) +a
#
#
heh = plt.scatter(f, v)
plt.title("Velocidad del sonido contra frecuencia medida")
plt.plot(f, v, color = 'black')
plt.xlabel("Frecuencia medida (Hz) ")
plt.ylabel('Velocidad del sonido (m/s)')

plt.errorbar(f,v,de)
#nolabm = de.mean()
#print lamb
#print nolabm
#

