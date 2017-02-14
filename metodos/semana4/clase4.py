import numpy as np
import matplotlib.pyplot as plt
import math as m
from numpy.linalg import inv 

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


#f = plt.plot(x,y)
#plt.plot(xp,yp,'ro')


#plt.savefig("heh.png")

#Punto 3

data = np.loadtxt("movimiento.dat")

f = plt.plot(data[:,0], data[:,1], 'ro')

def par(x,a,b,c):
	return a*x**2 + b*x+c

x2 = data[:,0]
y2 = data[:,1]

n = len(x2)
J = np.zeros((n,3))
k = np.zeros(n)

for i in range(n):
	J[i] = x2[i]**2,  x2[i], 1
	k[i] = y2[i]

#J1 = inv(J)
Jt = np.transpose(J)

kim = np.dot(Jt, J)
kim1 =inv(kim)

heh = np.dot(kim1, Jt)
rta = np.dot(heh, k)


x = np.linspace(0, 11, 2000)
print rta

y_fit = par(x, rta[2], rta[1], rta[0])
plt.plot(x,y)

plt.savefig("par.png")

#print k[1] 

















          








