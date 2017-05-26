# -*- coding: utf-8 -*-
"""
Created on Wed May 24 00:47:01 2017

@author: Javier Alejandro Acevedo Barroso
"""
import numpy as np
import matplotlib.pyplot as plt

def prob(y0, y):
	chi_squared = (1.0/2.0)*sum(((y0-y)/420.0)**2) #Al parecer diverge bastante rápido
	return np.exp(-chi_squared) #Entonces se me hizo razonable dividir por 420.

def func(ts,Q,tau):
	return Q*(1.0-np.exp(-ts*tau)) #Parece ser también que /RC es más duro computacionalmente que tau = 1/RC

data = np.loadtxt("CircuitoRC.txt")
t = data[:,0]
q = data[:,1]


#h = plt.figure()
#plt.scatter(t,q)
#plt.savefig("heh.png")

Qwalk = np.empty((0)) 
Twalk = np.empty((0))
lwalk = np.empty((0))

#Qwalk = np.append(Qwalk, np.random.random())
#Twalk = np.append(Twalk, np.random.random())


#Condiciones iniciales. Si no se colocan relativamente cerca al valor real
#No suele converger a la respuesta correcta.
Qwalk = np.append(Qwalk, 90)
Twalk = np.append(Twalk, 0.05)

yinit = func(t, Qwalk[0], Twalk[0])
lwalk = np.append(lwalk, prob(q,yinit))
print("%d %d", len(Qwalk), len(Twalk))

iter = 30000

for i in range(iter):
    Rn = np.random.normal(Qwalk[i], 0.1) 
    Cn = np.random.normal(Twalk[i], 0.1)

    yinit = func(t, Qwalk[i], Twalk[i])
    yn = func(t, Rn, Cn)
    
    linit = prob(q,yinit)
    ln = prob(q,yn)

    alpha =  ln/linit
    if(alpha>=1.0):
        Qwalk  = np.append(Qwalk,Rn)
        Twalk  = np.append(Twalk,Cn)
        lwalk = np.append(lwalk, ln)
    else:
        beta = np.random.random()
        if(beta<=alpha):
            Qwalk = np.append(Qwalk,Rn)
            Twalk = np.append(Twalk,Cn)
            lwalk = np.append(lwalk, ln)
        else:
            Qwalk = np.append(Qwalk,Qwalk[i])
            Twalk = np.append(Twalk,Twalk[i])
            lwalk = np.append(lwalk, linit)

#print "Heh"
Creal = Qwalk/10.0
Rreal = 1.0/(Qwalk*Creal)

rta = np.argmax(lwalk)

Tfun = Twalk[rta]
Qfun = Qwalk[rta]

Crta = Qwalk/10
Rrta = 1.0/(Crta*Twalk)

Rform = 1.0/(Crta[rta] * Twalk[rta])



qw = plt.figure()
fit = func(t,Qfun, Tfun)

plt.scatter(t,q, label = 'Datos')
plt.title(('Parametros: R=%.3f Ohms, C= %.3f F' %(Rrta[rta], Crta[rta])))
plt.plot(t, fit, color ='r', label = 'Modelo')
plt.legend(loc=0)
plt.savefig("reg.png")

we = plt.figure()
plt.hist(Crta, 100, normed=False)
plt.title("Histograma de C")
plt.savefig("hisC.png")


er = plt.figure()
plt.hist(Rrta, 50, normed = False)
plt.title("Histograma de R")
plt.savefig("histR.png")

rt = plt.figure()
plt.scatter(Rrta,Crta)
plt.title("Recorrido R vs Recorrido C")
plt.savefig("RC.png")

rt = plt.figure()
plt.scatter(Twalk,Qwalk)
plt.title("Recorrido variables reales (Tau vs Qmax)")
plt.savefig("QT.png")

ty = plt.figure()
hehN = np.empty((0))
hehO = np.empty((0))
for i in range(len(Rrta)):
    hehN= np.append(hehN, prob(q, func(t,Qwalk[i],Twalk[i]) ))
plt.scatter(Rrta,hehN)
plt.title("Verosimilitud vs R")
plt.savefig("verR.png")


yu = plt.figure()
plt.scatter(Crta,hehN)
plt.title("Verosimilitud vs C")
plt.savefig("verC.png")