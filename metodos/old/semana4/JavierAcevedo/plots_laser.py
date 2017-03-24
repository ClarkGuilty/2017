#import matplotlib as plt
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit 
#from math import exp

data = np.loadtxt("red3_filtrado.txt")
x = data[:,0]
y = data[:,1]

f = plt.plot(x,y)
plt.savefig("red3.png")

def gaus(x,a,b,c):
	return 1.0*a*np.exp(-(x-b)**2/c) 

p_opt, p_cov = curve_fit( gaus, x, y)

	
