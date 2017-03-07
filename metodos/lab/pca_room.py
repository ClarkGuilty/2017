import numpy as np
import matplotlib.pyplot as plt

import csv




#data = np.zeros((145,4))
#d1 = np.zeros((145,1))
#d2 = np.zeros((145,1))
#d3 = np.zeros((145,1))
#d4 = np.zeros((145,1))
#with open('room-temperature.csv', 'rb') as csvfile:
#	file = csv.reader(csvfile, delimiter=",", quotechar='|')
#	m = 0
#	for row in file:
#		print ','.join(row)
#		data[m]= row[1:].split(',')

#f =   open('room-temperature.csv','r')




data = np.loadtxt("room-temperature.csv", delimiter=',', skiprows=1, usecols=range(1,5))
T1 = data[:,0]

T2 = data[:,1]
T3 = data[:,2]
T4 = data[:,3]

x = np.linspace(0, 144,len(T1))
print x

f, axarr = plt.subplots(4, sharex=True, sharey=True)
axarr[0].plot(x, T1, label ="Front left ")
#plt.legend(loc=0)
plt.xlabel("Tiempo, cada unidad representa 30 minutos")
axarr[0].set_title('Temperature of a room, measured at the 4 corners')
axarr[1].plot(x, T2, label = "Front right")
#plt.legend(loc=0)
axarr[2].plot(x, T3, label = "Back left")
#plt.legend(loc=0)
axarr[3].plot(x, T4, label = "Back right")
#plt.legend(loc=0)
f.subplots_adjust(hspace=0)
plt.setp([a.get_xticklabels() for a in axarr[:-1]], visible=False)
f.text(0.06, 0.5, 'Temperatura en el lugar correspondiente', ha='center', va='center', rotation='vertical')
#plt.ylabel("Temperatura en el lugar correspondiente")
plt.savefig("room.pdf")




e1 = T1/np.trapz(T1)
e2 = T2/np.trapz(T2)
e3 = T3/np.trapz(T3)
e4 = T4/np.trapz(T4)
print e1
















