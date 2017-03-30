import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.fftpack import fft, fftfreq




data0 = wavfile.read("trumpet.wav")

v = data0[0]
x = data0[1]


f0 = fft(x)/len(x)
w = fftfreq(len(x), len(x)/v)
f = plt.plot(f0.real,w)
plt.savefig('satan')





































