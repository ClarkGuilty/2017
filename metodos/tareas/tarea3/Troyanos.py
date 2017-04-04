import numpy as np
import matplotlib.pyplot as plt

class Planetas:

    masa = -1
    sis = []
    otros = (-1,-2)
    x = np.zeros((1))
    y = np.zeros((1))
    vx = np.zeros((1))
    vy = np.zeros((1))
    fx = np.array((1))
    fy = np.zeros((1))
    t = -1
    dt = -10
    n = -1
    
    
    def __init__(self,masa,t,dt,x0,y0,vx0,vy0,n):
        self.masa = masa
        self.x  = np.zeros(n)
        self.y  = np.zeros(n)
        self.fx = np.zeros(n)
        self.fy = np.zeros(n)
        self.vx  = np.zeros(n)
        self.vy  = np.zeros(n)
        self.dt = dt
        self.x[0] = x0
        self.y[0] = y0
        self.vx[0] = vx0
        self.vy[0] = vy0
        self.n = n
        self.sis = []
        
        
    def cargar(self,p1,p2):
        self.sis.append(p1)
        self.sis.append(p2)
            
            
    def fuerza(self,j):
                #    for j in range(self.n):
        fx = 0
        fy = 0
        for i in range(2):
            r2 = np.power(self.x[j+1]-self.sis[i].x[j+1],2) + np.power(self.y[j+1]-self.sis[i].y[j+1],2)*15
            
            fx += self.sis[i].masa*(-self.x[j+1]+self.sis[i].x[j+1])/r2
            fy += self.sis[i].masa*(-self.y[j+1]+self.sis[i].y[j+1])/r2
        self.fx[j+1] = fx
        self.fy[j+1] = fy
      
      
    def vel(self,j):
        if(True):
            for i in range(2):
                self.vx[j+1] = self.vx[j-1]+2*dt*self.fx[j]
                self.vy[j+1] = self.vy[j-1]+2*dt*self.fy[j]
    	
    	
    def pos(self,j):
        if(True):
            for i in range(2):
                self.x[j+1] = self.x[j-1]+2*dt*self.vx[j]
                self.y[j+1] = self.y[j-1]+2*dt*self.vy[j]
    
    def i1(self):
        self.fuerza(-1)
        self.vx[1]=self.vx[0] + dt*self.fx[0]
        self.vy[1]=self.vy[0] + dt*self.fy[0]
        self.x[1]=self.x[0] + dt*self.vx[0]
        self.y[1]=self.y[0] + dt*self.vy[0] 
    
    def rad(self,p1,p2,j):
        x = (p1.x[j]-p2.x[j])**2
        y = (p1.y[j]-p2.y[j])**2
        return x+y
    
    #Aca acaba la clase

dt = 0.001
tmin = 0
tmax = 80
n = int(tmax/dt)
t = np.linspace(tmin,tmax*1.0,n)
v = np.sqrt(1047/100)

estrella = Planetas(1047,t,dt,0,0,0,0,n)
planeta = Planetas(1,t,dt,100,0,0,-v,n)

troyano = Planetas(0.005,t,dt,100.0*1/2,100.0*np.sqrt(3)/2, -np.sqrt(3)*v/2, v/2, n)

estrella.cargar(planeta,troyano )
planeta.cargar(estrella,troyano )
troyano.cargar( estrella,planeta)

cosas = (estrella,planeta,troyano)





for l in cosas:
#  print l.masa, "objeto"
  l.i1()
for l in cosas:
  l.fuerza(0)

  
#def heh():
#    for l in cosas:
#        l.i1()
#    for l in cosas:
#            l.fuerza(0)
#  
print n
for i in range(1,n-1):
    for heh in cosas:
    
#      print heh.masa, i
        heh.vel(i)
    for heh in cosas:
        heh.pos(i)    
    for heh in cosas:
        heh.fuerza(i)
#


#
f = plt.plot(estrella.x, estrella.y)
plt.plot(planeta.x,planeta.y)
plt.plot(troyano.x,troyano.y)
#plt.savefig("heh.png")


















    