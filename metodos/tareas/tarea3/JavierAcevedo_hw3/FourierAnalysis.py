import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.fftpack import fft, fftfreq, ifft
from matplotlib.figure import SubplotParams as sp




data1 = wavfile.read("trumpet.wav")
data0 = wavfile.read("violin.wav")

v0 = data0[0]
x0 = data0[1]
v1 = data1[0]
x1 = data1[1]

t = np.linspace(0,100, len(x0))

f0 = fft(x0)/len(x0)
f1 = fft(x1)/len(x1)
w0 = fftfreq(len(x0), 1.0/v0)
w1 = fftfreq(len(x1), 1.0/v1)


#f = plt.plot(w0,f0.real)
#plt.plot(w1,f1.real)

#
#he = sp(hspace = 0.5)
#fig = plt.figure(subplotpars = he)
#plt.title("")
#    
#ax1 = fig.add_subplot(211)
#ax1.plot(w0,f0.real, label = "Transformada de la trompeta", color = 'black')    
#h1 = plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#
#ax2 = fig.add_subplot(212)    
#ax2.plot(w1,f1, label = "Transformada del violin",  color = 'black')
##ax2.set_xlim([0, 5])
##ax2.set_xlabel("Frecuencias")
##ax2.set_ylabel("Coeficientes")
#h2= plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#
#fig.tight_layout()
#fig.text(0.5, 0.04, 'common X', ha='center')
#    
#plt.savefig("heh.png",bbox_extra_artists=(h1,h2,), bbox_inches='tight')



index0 = np.where(w0>0)
index1 = np.where(w1>0)

f, axarr = plt.subplots(2)
axarr[0].plot(w0[index0], f0[index0].real, label = "Violin")
box4 = axarr[0].get_position()
axarr[0].set_position([box4.x0, box4.y0, box4.width*0.8, box4.height])
leg = axarr[0].legend( loc = 'center left', bbox_to_anchor = (1.0, 0.5))
axarr[0].set_title('Transformadas')
axarr[1].plot(w1[index1], f1[index1].real, label = "Trompeta")
box = axarr[1].get_position()
axarr[1].set_position([box.x0, box.y0, box.width*0.8, box.height])
leg = axarr[1].legend( loc = 'center left', bbox_to_anchor = (1.0, 0.5))
plt.xlabel("Frecuencias [Hz]")

f.text(0, 0.5, 'Coeficientes', va='center', rotation='vertical')
#f.savefig("ViolinTrompeta.pdf")
f.savefig('ViolinTrompeta.pdf', bbox_inches='tight')

def filtroFF(arr):
    m = np.argmax(arr)
    heh = arr.copy()
    heh[m-5:5+m] = 0
    heh[-m-5:-m+5] = 0
    return heh
    
def filtroPA(arr,freq):
    index = np.where(abs(freq) < 2000)
    heh = arr.copy()
    heh[index] = 0
    return heh
    
def filtroPB(arr,freq):
    index = np.where(abs(freq) > 2000)
    heh = arr.copy()
    heh[index] = 0
    return heh



def filtroNF(arr):
    m = np.argmax(arr)
    heh = np.zeros(len(arr), complex)
    heh[m-5:5+m] = arr[m-5:5+m]
    heh[-m-5:-m+5] = arr[-m-5:-m+5]
    return heh

    
    

figu = plt.figure(figsize = (20,20))

f, axarr = plt.subplots(5, sharex = True)
axarr[0].plot(w0[index0], filtroFF(f0)[index0], label = "Filtro frecuencia fundamental")
axarr[0].legend(loc="upper right")
axarr[0].set_title('Filtros')
axarr[1].plot(w0[index0], filtroPA(f0,w0)[index0], label = "Filtro pasa altas")
axarr[2].plot(w0[index0], filtroPB(f0,w0)[index0], label = "Filtro pasa bajas")
axarr[3].plot(w0[index0], filtroNF(f0)[index0], label = "Filtro pasa banda")
axarr[4].plot(w0[index0], f0[index0], label = "Datos originales")
axarr[4].set_xlim(0,7000)
box0 = axarr[0].get_position()
axarr[0].set_position([box0.x0, box0.y0, box0.width*0.8, box0.height])
leg = axarr[0].legend( loc = 'center left', bbox_to_anchor = (1.0, 0.5))

box1 = axarr[1].get_position()
axarr[1].set_position([box1.x0, box1.y0, box1.width*0.8, box1.height])
leg = axarr[1].legend( loc = 'center left', bbox_to_anchor = (1.0, 0.5))

box2 = axarr[2].get_position()
axarr[2].set_position([box2.x0, box2.y0, box2.width*0.8, box2.height])
leg = axarr[2].legend( loc = 'center left', bbox_to_anchor = (1.0, 0.5))
#plt.ylabel("Coeficientes")

box3 = axarr[3].get_position()
axarr[3].set_position([box3.x0, box3.y0, box3.width*0.8, box3.height])
leg = axarr[3].legend( loc = 'center left', bbox_to_anchor = (1.0, 0.5))
#pyplot.show()

box4 = axarr[4].get_position()
axarr[4].set_position([box4.x0, box4.y0, box4.width*0.8, box4.height])
leg = axarr[4].legend( loc = 'center left', bbox_to_anchor = (1.0, 0.5))
plt.tight_layout()
plt.xlabel("Frecuencias")
#plt.ylabel("Coeficientes")



f.text(0, 0.5, 'Coeficientes', va='center', rotation='vertical')

plt.savefig('ViolinFiltros.pdf', bbox_inches='tight')
#figu.text(0.5, 0.04, 'common xlabel', ha='center', va='center')
#figu.text(0.06, 0.5, 'common ylabel', ha='center', va='center', rotation='vertical')

o0 = ifft(filtroFF(f0))
o1 = ifft(f0)*len(f0)

wavfile.write("violin_pico.wav", data = o0.real, rate = v0)





o1 = ifft(filtroPA(f0,w0))
#o2 = ifft(abs(f0))

wavfile.write("violin_pasaaltos.wav", data = o1.real, rate = v0)

o2 = ifft(filtroPB(f0,w0))
#o2 = ifft(abs(f0))

wavfile.write("violin_pasabajos.wav", data = o2.real, rate = v0)

o3 = ifft(filtroNF(f0))
#o2 = ifft(abs(f0))

wavfile.write("violin_pasabanda.wav", data = o3.real, rate = v0)



