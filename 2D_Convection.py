# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 16:02:15 2017

@author: dell
"""

from mpl_toolkits.mplot3d import Axes3D    ##New Library required for projected 3d plots

import numpy
from matplotlib import pyplot, cm


###variable declarations
nx = 81
ny = 81
nt = 100
c = 1
dx = 2 / (nx - 1)
dy = 2 / (ny - 1)
sigma = .2
dt = sigma * dx


# node numbers
x = numpy.linspace(0, 2, nx)
y = numpy.linspace(0, 2, ny)

# initialize u
u = numpy.ones((ny, nx))
un = numpy.ones((ny, nx)) 

# initial condition for u(.5<=x<=1 && .5<=y<=1 ) is 2
u[int(.5 / dy):int(1 / dy + 1),int(.5 / dx):int(1 / dx + 1)] = 2 

###Plot Initial Condition
##the figsize parameter can be used to produce different sized images
fig = pyplot.figure(figsize=(5, 5), dpi=100)
ax = fig.gca(projection='3d')                      
X, Y = numpy.meshgrid(x, y)                            
surf = ax.plot_surface(X, Y, u[:], cmap=cm.viridis)

# Numerical Solution

for n in range(nt): ##loop across number of time steps
    un = u.copy()
    row, col = u.shape
    u[1:, 1:] = (un[1:, 1:] - (c * dt / dx * (un[1:, 1:] - un[1:, :- 1])) -
                          (c * dt / dy * (un[1:, 1:] - un[:- 1, 1:])))
    u[0, :] = 1
    u[-1, :] = 1
    u[:, 0] = 1
    u[:, -1] = 1


fig = pyplot.figure(figsize=(11, 7), dpi=100)
ax = fig.gca(projection='3d')
surf2 = ax.plot_surface(X, Y, u[:], cmap=cm.viridis)

