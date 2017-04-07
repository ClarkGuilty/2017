import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import SubplotParams as sp

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
        ax = 0
        ay = 0
        for i in range(2):
            r2 = np.power(self.x[j+1]-self.sis[i].x[j+1],2) + np.power(self.y[j+1]-self.sis[i].y[j+1],2)
            
            ax += self.sis[i].masa*(-self.x[j+1]+self.sis[i].x[j+1])/np.power(r2,1.5)
            ay += self.sis[i].masa*(-self.y[j+1]+self.sis[i].y[j+1])/np.power(r2,1.5)
        self.fx[j+1] = ax
        self.fy[j+1] = ay
      
      
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
        
    def run(self, lista):
        for l in lista:
            l.i1()
        for l in lista:
            l.fuerza(0)

        for i in range(1,n-1):
#            print i
            for heh in lista:
                heh.vel(i)
            for heh in lista:
                heh.pos(i)    
            for heh in lista:
                heh.fuerza(i)
#

    
    #Aca acaba la clase

dt = 0.01
tmin = 0
tmax = 800
n = int(tmax/dt)
t = np.linspace(tmin,tmax*1.0,n)
v = np.sqrt(1050/100)

estrella = Planetas(1047,t,dt,0,0,0,0,n)
planeta = Planetas(1,t,dt,100,0,0,-v,n)

troyano = Planetas(0.005,t,dt,100.0*1/2,100.0*np.sqrt(3)/2, np.sqrt(3)*v/2, -v/2, n)

estrella.cargar(planeta,troyano )
planeta.cargar(estrella,troyano )
troyano.cargar( estrella,planeta)

cosas = (estrella,planeta,troyano)


estrella.run(cosas)


#for l in cosas:
##  print l.masa, "objeto"
#  l.i1()
#for l in cosas:
#  l.fuerza(0)
#
#  
#
##  
#totalus = n-1
#
#for i in range(1,n-1):
#    print i
#    for heh in cosas:
#    
##      print heh.masa, i
#        heh.vel(i)
#    for heh in cosas:
#        heh.pos(i)    
#    for heh in cosas:
#        heh.fuerza(i)
#


##
#f = plt.plot(estrella.x, estrella.y, label = "Estrella")
#plt.scatter(planeta.x[0],planeta.y[0])
#plt.scatter(troyano.x[0],troyano.y[0])
#plt.plot(planeta.x,planeta.y,label = "Planeta")
#plt.plot(troyano.x,troyano.y,label = "Troyano")
#plt.legend(loc=0)
#plt.savefig("superpuestas.png")
#

he = sp(hspace = 0.5)
fig = plt.figure(subplotpars = he)
plt.title("Trayectorias")    
ax1 = fig.add_subplot(311)
ax1.plot(estrella.x,estrella.y, label = "Estrella")    
h1 = plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax2 = fig.add_subplot(312)   
ax2.plot(planeta.x,planeta.y, label = "Planeta")
h2= plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax3 = fig.add_subplot(313)
ax3.plot(troyano.x,troyano.y, label = "Troyano")
h3= plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))   
plt.xlabel("x")

fig.text(0.01, 0.5, 'y', va='center', rotation='vertical') 
plt.savefig("OrbitsPLOT.pdf",bbox_extra_artists=(h1,h2,h3), bbox_inches='tight')






plt.figure(figsize = (10,10))
difx = troyano.x - planeta.x
dify = troyano.y - planeta.y

q = plt.plot(difx, dify, label = "Posicion del troyano respecto al planeta.")
plt.scatter(difx[0],dify[0], label="Posicion inicial")
plt.legend(loc=3)
plt.title("Posicion del troyano")
plt.xlabel("x")
plt.ylabel('y')
plt.savefig("Troyano.pdf")



dt = 0.01
tmin = 0
tmax = 2000
n = int(tmax/dt)
t = np.linspace(tmin,tmax*1.0,n)
v = np.sqrt(1050/100)

estrellas = (Planetas(1047,t,dt,0,0,0,0,n),Planetas(1047,t,dt,0,0,0,0,n),Planetas(1047,t,dt,0,0,0,0,n),Planetas(1047,t,dt,0,0,0,0,n))
planetas = (Planetas(10,t,dt,100,0,0,-v,n), Planetas(20,t,dt,100,0,0,-v,n),Planetas(30,t,dt,100,0,0,-v,n),Planetas(40,t,dt,100,0,0,-v,n))

troyanos = (Planetas(0.005,t,dt,100.0*1/2,100.0*np.sqrt(3)/2, np.sqrt(3)*v/2, -v/2, n),Planetas(0.005,t,dt,100.0*1/2,100.0*np.sqrt(3)/2, np.sqrt(3)*v/2, -v/2, n),Planetas(0.005,t,dt,100.0*1/2,100.0*np.sqrt(3)/2, np.sqrt(3)*v/2, -v/2, n),Planetas(0.005,t,dt,100.0*1/2,100.0*np.sqrt(3)/2, np.sqrt(3)*v/2, -v/2, n))

for i in range(len(estrellas)):  
    estrellas[i].cargar(planetas[i],troyanos[i] )
for i in range(len(planetas)): 
    planetas[i].cargar(estrellas[i],troyanos[i] )
for i in range(len(troyanos)):
    troyanos[i].cargar( estrellas[i],planetas[i])

for i in range(4):
    estrellas[0].run((estrellas[i], planetas[i], troyanos[i]))







he = sp(hspace = 0.5, wspace = 1.6)
fig = plt.figure(subplotpars = he)


ax1 = fig.add_subplot(221)

ax1.title.set_text("Trayectorias para m2 = 10")
#ax1.plot(estrellas[0].x,estrellas[0].y, label = "Estrella")    
#ax1.plot(planetas[0].x,planetas[0].y, label = "Planeta") 
ax1.plot(troyanos[0].x,troyanos[0].y, label = "Troyano") 

#h1 = plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

ax2 = fig.add_subplot(222)
ax2.title.set_text("Trayectorias para m2 = 20")
#ax2.plot(estrellas[1].x,estrellas[1].y, label = "Estrella")    
#ax2.plot(planetas[1].x,planetas[1].y, label = "Planeta") 
ax2.plot(troyanos[1].x,troyanos[1].y, label = "Troyano")
h2= plt.legend(loc='upper left', bbox_to_anchor=(1, 0.5))
#h2= plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

ax3 = fig.add_subplot(223)
ax3.title.set_text("Trayectorias para m2 = 30")
#ax3.plot(estrellas[2].x,estrellas[2].y, label = "Estrella")    
#ax3.plot(planetas[2].x,planetas[2].y, label = "Planeta") 
ax3.plot(troyanos[2].x,troyanos[2].y, label = "Troyano")
#h3= plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))    

ax4 = fig.add_subplot(224)
ax4.title.set_text("Trayectorias para m2 = 40")
#ax4.plot(estrellas[3].x,estrellas[3].y, label = "Estrella")    
#ax4.plot(planetas[3].x,planetas[3].y, label = "Planeta") 
ax4.plot(troyanos[3].x,troyanos[3].y, label = "Troyano")

plt.xlabel("x")

fig.text(0, 0.5, 'y', va='center', rotation='vertical')
plt.tight_layout()

plt.savefig("MassPLOT.pdf",bbox_extra_artists=(h1,h2,h3), bbox_inches='tight')





