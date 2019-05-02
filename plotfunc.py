# -*- coding: utf-8 -*-
"""
Created on Thu May  2 11:18:55 2019

@author: MY-PC
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3])
y = x**2 + 1

print(x)
print(y)

plt.figure()

plt.plot(x, y, "-ro")

plt.show()