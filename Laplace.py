
# Importing the libraries
from mpl_toolkits.mplot3d import Axes3D    ##New Library required for projected 3d plots

import numpy
from matplotlib import pyplot, cm

# plot function
def plotSurf(x,y,p):
    fig = pyplot.figure(figsize=(11, 7), dpi=100)
    ax = fig.gca(projection='3d')
    X, Y = numpy.meshgrid(x, y)
    surf = ax.plot_surface(X, Y, p[:], rstride=1, cstride=1, cmap=cm.viridis,
            linewidth=0, antialiased=False)
    ax.set_xlim(0, 2)
    ax.set_ylim(0, 1)
    ax.view_init(30, 225)
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')

# This function solves the Laplace Equation:
def laplace(p, dy, dx, y, targetNorm):
    l1Norm = 1 # Initialize the error = 1
    while l1Norm > targetNorm: # Iterate till the difference in norms is very less
        pn = p.copy()
        p[1:-1,1:-1] = ((dy**2 * (pn[1:-1, 2:] + pn[1:-1, :-2])
        + dx**2 * (pn[2:, 1:-1] + pn[:-2, 1:-1])) / (2 * (dx**2 + dy**2)))
        
        # Boundary Conditions
        p[:,0] = 0 # p = 0 at x = 0
        p[:,-1] = y # p = y at x = 2 
        p[0, :] = p[1, :]  # dp/dy = 0 @ y = 0
        p[-1, :] = p[-2, :]  # dp/dy = 0 @ y = 1
        
        # There are different ways to define the deciding point
#        l1Norm = ((numpy.sum(numpy.abs(pn[:])-numpy.sum(numpy.abs(p[:]))
#        / numpy.sum(numpy.abs(pn[:])) # l1 norm is sum of abs of array elements
        l1Norm = (numpy.sum(numpy.abs(p[:]) - numpy.abs(pn[:])) /
                numpy.sum(numpy.abs(pn[:])))
        
    return p

  
nx, ny = 31, 31
dx, dy = 2/(nx-1), 1/(ny-1) # , x = (0, 2) and y= (0, 1)
y = numpy.linspace(0, 1, ny)
x = numpy.linspace(0, 2, nx)

p = numpy.zeros((ny,nx))
targetNorm = 1e-4

plotSurf(x,y,p) # Initially
laplace(p, dy, dx, y, targetNorm)
plotSurf(x,y,p) # After running Laplace