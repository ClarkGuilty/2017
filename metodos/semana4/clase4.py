import numpy as np
import matplotlib.pyplot as plt
import math as m

#Hacer la matriz.
xp = np.array([0, 0.25, 0.5, 0.75])
yp = np.array([3,1,-3,1])
A = np.zeros((4,4))
b = np.zeros(4)
for i in range(4):
	A[i] = m.cos(m.pi*xp[i]), m.cos(2*m.pi*xp[i]), m.cos(3*m.pi*xp[i]), m.cos(4*m.pi*xp[i])
	b[i] = yp[i]

sol = np.linalg.solve(A,b)


def serie(x, a, b, c, d):
	return a*np.cos(np.pi*x) + b*np.cos(2*np.pi*x) + c*np.cos(3*np.pi*x)+ d*np.cos(4*np.pi*x)



x = np.linspace(-3,3,2000)
y = serie(x, sol[0], sol[1], sol[2],sol[3])


f = plt.plot(x,y)
plt.plot(xp,yp,'ro')


plt.savefig("heh.png")










