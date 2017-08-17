#!/usr/bin/python
import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import matplotlib.animation as animation
from matplotlib import style



style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
	graf = open('/mnt/c/Users/Emtel Sa Esp/scripts/test.txt', 'r').read()
	lines = graf.split('\n')
	xs = []
	ys = []
	for line in lines:
		if len(line) > 1:
			x, y = line.split(',')
			xs.append(x)
			ys.append(y)

	ax1.clear()
	ax1.plot(xs, ys)

ani = animation.FuncAnimation(fig, animate, interval=100000)