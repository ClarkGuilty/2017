# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 12:04:45 2017

@author: Javier Acevedo
"""
import numpy as np
import matplotlib.pyplot as plt


n = 9
aprox = 0.00001
df = np.zeros( (n,n))
f = np.zeros(n)
x = np.array([0.5,0.5,0.5,0.5,0.5,0.5,1,1,1])
w1 = 10
w2 = 20
L = 8
L1 =3
L2 = 4
L3 = 4
def F(x, f):
    f[0] = L1*x[3]+ L2*x[4] + L3*x[5] - L
    f[1] = L1*x[0]+ L2*x[1] - L3*x[2]
    f[2] = x[6]*x[0] - x[7]*x[1] - w1
    f[3] = x[6]*x[3] - x[7]*x[4]
    f[4] = x[7]*x[1] + x[8]*x[2] - w2
    f[5] = x[7]*x[4] - x[8]*x[5]
    f[6] = np.power(x[0],2) +np.power(x[3],2) -1
    f[7] = np.power(x[1],2) +np.power(x[4],2) -1
    f[8] = np.power(x[2],2) +np.power(x[5],2) -1

def mod(f):
    total = 0.
    for i in range(9):
        total += np.power(f[i],2)
    return np.sqrt(total)

def dF(x, df, n):
    h = 1e-6
    for j in range(0,n):
        temp = x[j]
        x[j] = x[j] + h/2
        F(x,f)
        for i in range(0, n):
            df[i,j] = f[i]
        x[j] = temp
    for j in range(0,n):
        temp = x[j]
        x[j] = x[j] - h/2
        F(x,f)
        for i in range(0, n):
            df[i,j] = (df[i,j] - f[i] ) /h
        x[j] = temp


t1 = np.array([np.arcsin(x[0])])
t2 = np.array([np.arcsin(x[1])])
t3 = np.array([np.arcsin(x[2])])
T1 = np.array([x[6]])
T2 = np.array([x[7]])
T3 = np.array([x[8]])

B = np.zeros(n)
it = 0


F(x,f)
dF(x,df,n)

while(mod(f) > aprox):
    it +=1
    F(x,f)
    dF(x,df,n)
    
    for i in range(n):
        B[i] = -f[i]
    
    solf = np.linalg.solve(df, B)
    x = x + solf
    t1 = np.append(t1, np.arcsin(x[0])) #No es in-place. RIP memoria.
    t2 = np.append(t2, np.arcsin(x[1]))
    t3 = np.append(t3, np.arcsin(x[2]))    
    T1 = np.append(T1, x[6])
    T2 = np.append(T2, x[7])
    T3 = np.append(T3, x[8])
    

    
    
ite = np.zeros(it+1)
for i in range(it+1):
    ite[i] = i


f = plt.plot(ite,np.nan_to_num(t1), label = "Valores intermedios del primer angulo", color = "blue")
plt.plot(ite,np.nan_to_num(t2), label = "Valores intermedios del segundo angulo", color = "red")
plt.plot(ite,np.nan_to_num(t3), label = "Valores intermedios del tercer angulo", color = "green")
plt.xlabel("Iteraciones")
plt.ylabel("Valor del angulo (rad)")
plt.title("Valor de los diferentes angulos a traves de las iteraciones")
#plt.legend(loc=5)

h = plt.subplot(111).legend(loc='center left', bbox_to_anchor=(1, 0.5))
#plt.savefig("AnglesPLOT.pdf")
plt.savefig('AnglesPLOT.pdf', bbox_extra_artists=(h,), bbox_inches='tight')



plt.figure(figsize = (10,10))

f = plt.plot(ite,T1, label = "Valores intermedios de la primera tension", color = "blue")
plt.plot(ite,T2, label = "Valores intermedios de la segunda tension", color = "red")
plt.plot(ite,T3, label = "Valores intermedios de la tercera tension", color = "green")
plt.xlabel("Iteraciones")
plt.ylabel("Valor de la tension")
plt.title("Valor de las diferentes tensiones a traves de las iteraciones")
#plt.legend(loc=5)

h = plt.subplot(111).legend(loc='center left', bbox_to_anchor=(1, 0.5))
#plt.savefig("AnglesPLOT.pdf")
plt.savefig('TensionsPLOT.pdf', bbox_extra_artists=(h,), bbox_inches='tight')




print "El valor del ángulo 1 es de %f" % t1[-1]
print "El valor del ángulo 2 es de %f" % t2[-1]
print "El valor del ángulo 3 es de %f" % t3[-1]
print "El valor de la tensión 1 es de %f" % T1[-1]
print "El valor de la tensión 2 es de %f" % T2[-1]
print "El valor de la tensión 3 es de %f" % T3[-1]



    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        


    
    
    
    
    
    
    
    
    
    
    
