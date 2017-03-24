import numpy as np
import matplotlib.pyplot as plt


def c1(x):
    x = x*10
    x = np.ceil(x)
    return x/10.0
def c2(x):
    x = x*100.0
    x = np.ceil(x)
    return x/100.0
def m1(x):
    x = x/100
    x = np.ceil(x)
    return x*100

data = np.loadtxt( "datosHeh.txt", delimiter = ';' )
n = data[:,0]
t = data[:,1]
T = data[:,2]
w = data[:,4]
f = data[:,5]/10
v = data[:,6]

noise = np.random.normal(0,0.4, len(t))

v = v+noise


f = f + np.random.normal(0,1000, len(t))

t = c1(t)


def vol(tes,tau, v0):
    a = 1.0*v0
    b = 1.0*tau
    return a*np.exp(-b*tes)
def vol4(tes,tau):
    b = 1.0*tau
    return v[0]*np.exp(-b*tes)

from scipy.optimize import curve_fit





R = 10000
C = 51E-12
L = 2E-3
real = R/(L*2)

cons , cov = curve_fit(vol, t,v,(1,v[0]))
susana = curve_fit(vol4,t,v)


##print cons
tn = np.linspace(0,17.0*np.pi,100)
vn = vol(tn, cons[0], cons[1])

ncos = [70, 3000000]
vn1 = vol4(tn, 2500000)

po = plt.scatter(t,v, label = 'Datos')
plt.plot(tn,vn, label = "Regresion")
plt.title("Voltaje contra tiempo")
plt.xlabel("Voltajes medidos (V)")
plt.ylabel("Tiempo (s)")
plt.legend(loc=0)
plt.savefig('g1.png')
##plt.plot(tn,vn1, color = 'green')
##plt.show(po)

R = 10000
C = 51E-12
L = 2E-3
w0 = np.sqrt(1/(L*C))
w = np.sqrt(w0*w0-(R*R/(4*L*L)))
T = 2*np.pi/w
print "Valores teoricos"
print c1(w0),c1(w), T
print "Valores Medidos"
mf = f.mean()
wm = 2*np.pi*mf
Tm = 2*np.pi/wm
print c1(wm), Tm
print ""
print "Errores"
javier = abs(w-wm)*100/w
javier0 = abs(T-Tm)*100/T
print javier, javier0

print "Valores de la regresion"
print cons[0], cons[1]

v = c1(v)
f = m1(c2(f))
q = " & "
w = " \\\\ \hline"
for i in range(len(v)):
    print str(i+1) + q + str(f[i]) +q+str(v[i])+w



print R/(2*L), cons[0]


