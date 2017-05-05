import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("datos.txt")
V1 = data[:,0]
t = data[:,1]*60
V2 = data[:,2]
Q = V1/t
D = 6.5 #cm
z1 = 74#cm
d = 0.3 #cm
z2 = 21#cm

A1 = 6.5*6.5/4
A2 = 0.3*0.3/4
dV1 = 5
dt = 0.05


v = Q/A2
dq = np.sqrt(dV1*dV1/(t*t) + dt*dt*V1*V1/(t*t*t*t))
dA = (0.05*d/t)
dv = np.sqrt(dq*dq/(A2*A2) + dA*dA*Q*Q/(A2*A2*A2*A2))

print "\hline"
print "$V_1 (mL)$ & t(s) & $V_2$ (mL) & Q (mL/s) & $v_2$ (m/s) \\\\ \hline"
for i in range (0,10):
  print("$%.2f \pm 5$ &$ %.2f \pm 0.05$ & $%.2f \pm 5$  & $%.4f \pm %.4f $& $%.2f \pm %.2f$ \\\\ \hline" % (V1[i], t[i], V2[i], Q[i],dq[i], v[i], dv[i]))