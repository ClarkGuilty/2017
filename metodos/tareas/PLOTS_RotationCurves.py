import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt("RotationCurves/RotationCurve_F571-8.txt")
PRad = data[:,2]
VGas = data[:,3]
VDisk = data[:,4]
VBul = data[:,5]
Vel = data[:,6]


VTeo = VGas + VDisk + VBul


f = plt.plot(PRad, Vel)
plt.plot(PRad, VTeo)
plt.ylabel('Velocidad')
plt.xlabel('Radio')
plt.savefig("heh.png")






















