# -*- coding: utf-8 -*-  
import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt("RotationCurve_F571-8.txt")
PRad = data[:,1]
VGas = data[:,2]
VDisk = data[:,3]
VBul = data[:,4]
Vel = data[:,5]


VTeo = VGas + VDisk + VBul


f = plt.plot(PRad, Vel, label = "Velocidad medida", color = "black")
plt.plot(PRad, VTeo, label = "Velocidad teorica", color = "green")

plt.ylabel('Velocidad (km/s)')
plt.xlabel('Radio (kpc)')
plt.legend(loc=0)
plt.savefig("RotationCurvePlot.pdf")






















