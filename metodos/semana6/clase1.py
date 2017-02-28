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
index = np.where( abs(freq) > 100)    
#print fft_x
#print index
print freq 
fft_x[index] = 0



plt.plot(freq,abs(fft_x))
#plt.xlim([-2000,2000])

#f = plt.scatter(img[:,0], img[:,1])
plt.savefig("heh.png")
clean_f = ifft2(fft_x).real

fig = plt.figure(1, figsize=(9.5,9))
#np.savetxt("yolo.png")

from  scipy.misc import toimage
toimage(clean_f).save('outfile.jpg')

#plt.savefig("rta.png")








































