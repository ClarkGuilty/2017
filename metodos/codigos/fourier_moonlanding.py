# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 06:27:42 2017

@author: Javier
"""

import numpy as np
import matplotlib.pyplot as plt


import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt



from scipy.fftpack import fft2, fftfreq, ifft2
img = plt.imread('moonlanding.png')

n = len(img) # number of point in the whole interval
f = 200.0 #  frequency in Hz
dt = 1 / (f * 128 ) #128 samples per frequency

fft_x = fft2(img)
freq = fftfreq(n, dt) # frequencies
#f = plt.plot(freq,abs(fft_x))
#plt.savefig('satan.png')

print fft_x.shape


#index = np.where(( abs(freq) > 100)    & ( abs(fft_x[:,0]) > 5000  ) & ( abs(fft_x[:,1]) > 5000)      )

#print fft_x
#print index
#print freq
#for i in range(51,len(fft_x)):
#    fft_x[i] = 0
#fft_x[0,np.abs(freq)> 50] = 0
#temp = np.zeros((474,630))
#temp[:] = fft_x[:]

temp = np.copy(fft_x)


#y = fft_x[:,0]
#y1 = fft_x[:,0]
#y[np.abs(freq)< 50  ] = fft_x[:,0]
#index = np.where(np.abs(freq)>np.abs(freq[50]) and np.abs(freq)<   np.abs(freq[n-50]))

#y[np.abs(freq)> np.abs(freq[50])]= 0
#y[np.abs(freq)< np.abs(freq[freq.argmax(axis = 0)])]= y1[np.abs(freq)< np.abs(freq[freq.argmax(axis = 0)])]
#
#x = fft_x[:,1]
#x1 = fft_x[:,1]
#z = fft_x[2,:]

for i in range(630):
    y = fft_x[:,i]
    y1 = fft_x[:,i]
    y[np.abs(freq)> np.abs(freq[50])]= 0
    y[np.abs(freq)< np.abs(freq[freq.argmax(axis = 0)])]= y1[np.abs(freq)< np.abs(freq[freq.argmax(axis = 0)])]
    fft_x[:,i] = y


#y[50:n-50]=0
#for i in range(50,n/2-25):
#    y[i] = 0
#for i in range(-n/2-25,-50):
#    y[i] = 0








j = plt.plot(freq,fft_x, label = "Espectro de potencias modificado")
plt.plot(freq,temp, label = "Espectro de potencias original")
#plt.legend(loc=0)
#plt.plot(freq,abs(fft_x[:,0]))
#plt.xlim([-2000,2000])

#f = plt.scatter(img[:,0], img[:,1])
plt.savefig("moon_landing.png")
clean_f = ifft2(fft_x).real

fig = plt.figure(1, figsize=(9.5,9))
#np.savetxt("yolo.png")

from  scipy.misc import toimage
toimage(clean_f).save('moon-landing-Reconstruirda.jpg')

#plt.savefig("rta.png")

