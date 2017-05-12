# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy
from matplotlib import pyplot
import sys, time

nx = 40 # num of divisions
dx = 2/ nx # x ranges from 0 to 2
dt = 0.025 # time step
c = 1 # wave speed
nt = 10 # this changes a lot

# I.C.s
u = numpy.ones(nx+1)
u[int(.5 / dx):int(1 / dx + 1)] = 2 # u = 2 between 0.5


un = numpy.ones(nx+1) #initialize a temporary array

for n in range(nt):  #loop for values of n from 0 to nt, so it will run nt times
    un = u.copy() ##copy the existing values of u into un
    for i in range(1,nx+1):
        u[i] = un[i] - c * dt / dx * (un[i] - un[i-1])
        
pyplot.plot(numpy.linspace(0, 2, nx+1),u);

