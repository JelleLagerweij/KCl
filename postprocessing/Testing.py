# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 18:30:02 2023

@author: Jelle
"""

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax2 = ax1.twiny()

X = np.linspace(0, 0.5,1000)
Y = np.cos(X*20)

ax1.plot(X,Y)
ax1.set_xlabel(r"Original x-axis: $X$")

new_tick_values = np.array([100000, 1000, 1000, 500])

new_tick_locations = np.power(new_tick_values/31.436032, 1/3)

def tick_function(X):
    V = 31.436032*np.power(X, 3)
    return ["%.0f" % z for z in V]

ax2.set_xlim(ax1.get_xlim())
ax2.set_xticks(new_tick_locations)
ax2.set_xticklabels(new_tick_values)
ax2.set_xlabel(r"Modified x-axis: $1/(1+X)$")
plt.show()