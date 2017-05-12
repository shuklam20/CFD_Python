# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 12:39:27 2017

@author: dell
"""

import numpy
from matplotlib import pyplot

def x_nodes(nx):
    dx = 2 / (nx-1) # x ranges from 0 to 2
    sigma = 0.2 # Courant Number
    nt = 20 # this makes solution interesting
    nu = 0.3 # Viscocity
    dt = sigma * dx**2 / nu # time step
    
    # I.C.s
    u = numpy.ones(nx)
    u[int(.5 / dx):int(1 / dx + 1)] = 2 # u = 2 between 0.5
    
    
    un = numpy.ones(nx) #initialize a temporary array
    
    for n in range(nt):  #loop for values of n from 0 to nt, so it will run nt times
        un = u.copy() ##copy the existing values of u into un
        for i in range(1,nx-1):
            u[i] = un[i] + nu * dt / dx**2 * (un[i+1] - 2 * un[i] + un[i-1])
    
    pyplot.plot(numpy.linspace(0, 2, nx),u);

x_nodes(81)
