import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt("data.txt")
x = data[:,0]
y = data[:,1]

f = plt.plot(x,y, label = "Promedio de muestreos")
plt.xlabel("Tiempo")
plt.ylabel("Numero de particulas")
plt.legend(loc=0)

plt.savefig("grafica.png")
plt.show(f)
