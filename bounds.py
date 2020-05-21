#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 23:19:54 2020

@author: horitamasayoshi
"""

import matplotlib.pyplot as plt

ts = 0.01
g = 9.8
e = 0.6
v = []
p = []
t = []
v.append(0)
p.append(10)
t.append(0)

for i in range (1, 1000):
    t.append(i/100)
    v.append(v[i-1] - g*ts)
    p.append(p[i-1] + v[i-1]*ts)
    if p[i] < 0:
        p[i] = -p[i]
        v[i] = -e*v[i]
        
plt.plot(t,p)
plt.show()