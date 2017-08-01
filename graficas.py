#!/usr/bin/python
import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import os

with open("/mnt/c/Users/Emtel Sa Esp/scripts/graficos.txt") as f:
    data = f.read()

data = data.split('\n')

x = [row.split(' ')[0] for row in data]
y = [row.split(' ')[1] for row in data]
z = [row.split(' ')[2] for row in data]

fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.set_title("GRAFICA COMPORTAMIENTO NODOS...")    
ax1.set_xlabel('Hora')
ax1.set_ylabel('Porcentaje de usuarios')

ax1.plot(x,y, linestyle='--' , color='r', label='deds')
ax1.plot(x,z, linestyle='-' , color='b', label='santa')

leg = ax1.legend()
plt.savefig('/mnt/c/Users/Emtel Sa Esp/scripts/graficas/zxc.png')