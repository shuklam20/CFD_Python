# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 12:03:33 2017

@author: dell
"""

import numpy
from matplotlib import pyplot

def x_nodes(nx):
    dx = 2 / nx # x ranges from 0 to 2
    sigma = 0.5 # Courant Number
    dt = sigma * dx # time step
    nt = 20 # this makes solution interesting

    # I.C.s
    u = numpy.ones(nx+1)
    u[int(.5 / dx):int(1 / dx + 1)] = 2 # u = 2 between 0.5


    un = numpy.ones(nx+1) #initialize a temporary array

    for n in range(nt):  #loop for values of n from 0 to nt, so it will run nt times
        un = u.copy() ##copy the existing values of u into un
        for i in range(1,nx+1):
            u[i] = un[i] - un[i] * dt / dx * (un[i] - un[i-1])

    pyplot.plot(numpy.linspace(0, 2, nx+1),u);

x_nodes(85)

