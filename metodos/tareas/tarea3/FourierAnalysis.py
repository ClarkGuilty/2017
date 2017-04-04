import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.fftpack import fft, fftfreq
from matplotlib.figure import SubplotParams as sp




data0 = wavfile.read("trumpet.wav")
data1 = wavfile.read("violin.wav")

v0 = data0[0]
x0 = data0[1]
v1 = data1[0]
x1 = data1[1]


f0 = fft(x0)/len(x0)
f1 = fft(x1)/len(x1)
w0 = fftfreq(len(x0), len(x0)/v0)
w1 = fftfreq(len(x1), len(x1)/v1)
#f = plt.plot(w0,f0.real)
#plt.plot(w1,f1.real)


he = sp(hspace = 0.5)
fig = plt.figure(subplotpars = he)

plt.title("")
    
ax1 = fig.add_subplot(211)

ax1.plot(w0,f0.real, label = "x^4", color = 'black')

    
h1 = plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    #plt.savefig("Anomalies_SOI_Plot.png",bbox_extra_artists=(h,), bbox_inches='tight')

ax2 = fig.add_subplot(212)
    
    
ax2.plot(w1,f1, label = "x^4",  color = 'black')

    
h2= plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    
plt.savefig("heh.png",bbox_extra_artists=(h1,h2,), bbox_inches='tight')





















