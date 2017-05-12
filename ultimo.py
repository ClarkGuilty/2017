import numpy as np
import matplotlib.pyplot as plt

def k(r,R):
  a = (1.0)*r/R
  return 1 - 2.10443*a + 2.08877*a*a*a - 0.94813*a*a*a*a*a

R = 6.1/200
r1 = 2.971/2000
r2 = 5.896/2000

dJab = 978 #kg/L
v1 = 4.0*np.pi*r1*r1*r1/3
v2 = 4.0*np.pi*r2*r2*r2/3
d1 = 0.1/(v1*1000)
d2 = 0.9/(v2*1000)

t1 = np.loadtxt("heh.txt")
t2 = np.loadtxt("noHeh.txt")

t01 = t1.mean()
t02 = t2.mean()

print t01, t02

v1 = 0.22/t01
v2 = 0.22/t02

def mu(dM, rM, K, v):
  return 2*(dM-dJab)*rM*rM*(9.80)*K/(9*np.pi*v)

k(r1,R)
m1 = mu(d1,r1,k(r1,R), v1)
m2 = mu(d2,r2,k(r2,R), v2)
m3 = m1/2 + m2/2
m4 = m3*0.43

print "t_1 (s) & t_2 (s)"
for i in range (0,20):
  print("%.2f & %.2f \\\\ \hline" % (t1[i], t2[i]))