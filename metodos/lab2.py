import matplotlib.pyplot  as plt
import numpy as np
from scipy.stats import expon
from scipy.stats import norm

n=[]
for i in range(10000):
	n.append(np.random.exponential(500))



f, figura1 = plt.subplots(1,1)
figura1.hist(n, bins = 2000, normed = True)
f.savefig('histograma.png')

