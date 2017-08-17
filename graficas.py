#!/usr/bin/python
import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import os

path = os.getcwd()

with open(path + "/test2.txt") as f:
    data = f.read()
 
data = data.split('\n')

x = [row.split(' ')[0] for row in data]
y = [row.split(' ')[1] for row in data]
z = [row.split(' ')[2] for row in data]
a = [row.split(' ')[3] for row in data]
b = [row.split(' ')[4] for row in data]
c = [row.split(' ')[5] for row in data]
d = [row.split(' ')[6] for row in data]

fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.set_title("GRAFICA COMPORTAMIENTO NODOS...")    
ax1.set_xlabel('Hora')
ax1.set_ylabel('Porcentaje de usuarios')

ax1.plot(x,y, linestyle='--' , color='r', label='deds')
ax1.plot(x,z, linestyle='-' , color='b', label='santa')
ax1.plot(x,a, linestyle='-' , color='y', label='santasad')
ax1.plot(x,b, linestyle='-' , color='g', label='santsda')
ax1.plot(x,c, linestyle='-' , color='b', label='sandfta')

print "genial"

leg = ax1.legend()
plt.savefig(path + '/graficas/proof.png')