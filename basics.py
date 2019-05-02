# -*- coding: utf-8 -*-
"""
Created on Thu May  2 19:00:39 2019

@author: Dmitry
"""

import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0.1, 5, 20)
print(x, len(x))
y = np.log(x)
w = np.sin(x)

plt.figure()
plt.plot(x,y,"-r")
plt.plot(x,w,"-b")
plt.plot(x,np.zeros([len(x),1]),"o")
plt.show()