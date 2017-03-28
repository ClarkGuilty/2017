import numpy as np
import matplotlib.pyplot as plt

n_points = 1000
x = np.linspace(0.0,1.0,n_points)
u_initial = np.exp(-((x-0.3)*(x-0.3))/0.01)


f = plt.plot(x,u_initial)
plt.show(f)










#find the first iteration for fixed boundary conditions
delta_x = x[1]-x[0]
delta_t = 0.0005
c = 1.0
r = c * delta_t / delta_x

print r # remember, this should be less than 1.0 for this scheme to work

#fixed boundary conditions
u_initial[0] = 0.0
u_initial[n_points-1] = 0.0

u_future = np.zeros(n_points)
u_future[0] = 0.0
u_future[n_points-1] = 0.0

for i in range(1,n_points-1):
    u_future[i] = u_initial[i] + (np.power(r2/2.0) * (u_initial[i+1] - 2.0 * u_initial[i] + u_initial[i-1])

#create a new variable to hold the previous value
u_past = u_initial.copy()
#create a new variable to hold the present value
u_present = u_future.copy()

fig = plt.figure(4,10)

q= plt.plot(x, u_initial)
plt.plot(x, u_past)
plt.plot(x, u_present)
plt.xlabel('x')
plt.ylabel('u')


plt.show(q)




















