# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 07:16:17 2017

@author: Javier
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("random_walks.txt")


plt.hist(data, bins= "auto",normed=1)
plt.xlabel("Posicion final")
plt.ylabel("Probabilidad normalizada")
plt.savefig("rand.png")
