import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

data = np.loadtxt("TempHeight.txt")
temp = data[:,1]
h = data[:,0]

f = plt.plot(h, temp, label = "Temperatura", color = 'red')
plt.xlabel('Altura (m)')
plt.ylabel('Temperatura (C)')
plt.title('Temperatura atmosferica contra altura')
plt.legend(loc=0)
plt.savefig("TemperaturePlot.pdf")

#Segunda Parte

x = np.linspace (2500, 25000, 150)
dx = x[1]-x[0]

tck  = interpolate.splrep(h, temp)
y_spline = interpolate.splev(x,tck)


f_prime_diff = (y_spline[1:] - y_spline[0:-1])/(2*dx)



plt.figure(figsize = (10,10))


valor = -9.8/1000
ad = np.full(150,valor )


g = plt.plot(x[0:-1],f_prime_diff, label = "Gradiente de T")
plt.plot(x, ad, label = "Gradiente adiabatico")
plt.xlabel('Altura (m)')
plt.ylabel('Gradientes (C/m)')
plt.legend(loc=0)
plt.savefig("GradientsPlot.pdf")



y5 = []
x5 = []

for i in range(len(f_prime_diff)):
	if(np.absolute(f_prime_diff[i]) > 9.8/1000.0):
#		print i
		y5.append(f_prime_diff[i])
		x5.append(x[i])


#print 4 
plt.figure(figsize = (10,10))

heh = plt.scatter(x5,y5,label = "Puntos para |grad(T)| > gradiente adiabatico")


plt.xlabel('Altura (m)')
plt.ylabel('Gradientes (C/m)')

plt.legend(loc = 0)

plt.savefig("ConvectionPLOT.pdf")










#g = plt.plot(x,y_spline)














