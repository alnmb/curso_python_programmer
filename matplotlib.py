# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 18:03:08 2021

@author: aln_m
@title: matplotlib 1st session
"""

import matplotlib.pyplot as plt
from random import choice

plt.rc('figure', figsize=(12,6))

values = list(range(0,55,5))
"""simple graph"""
# plt.plot(values)
# plt.show() 


x_axis=[0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
""" changing title, xlabel and ylim and x and y limits"""
# plt.plot(x_axis, values)
# plt.xlim(0,1.0)
# plt.ylim(0,50)
# plt.title("Mi primera grafica")
# plt.xlabel("Valores de X")
# plt.ylabel("Valores de Y")
# plt.show()
"""displaying in a different shape"""
# plt.plot(x_axis, values, 'ko--')
# plt.xlim(0,1.0)
# plt.ylim(0,50)
# plt.title("Mi primera grafica")
# plt.xlabel("Valores de X")
# plt.ylabel("Valores de Y")
# plt.show()