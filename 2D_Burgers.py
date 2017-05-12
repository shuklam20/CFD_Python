# Importing the libraries
from mpl_toolkits.mplot3d import Axes3D    ##New Library required for projected 3d plots

import numpy
from matplotlib import pyplot, cm

# variables' declarations
length = 2
width = 2
initTemp = 2
nx = 41
ny = 41
c = 1
nt = 120
dx = 2 / (nx - 1)
dy = 2 / (ny - 1)
sigma = .0009
nu = 0.01
dt = sigma * dx * dy / nu

# define x and y nodes
x = numpy.linspace(0,length,nx)
y = numpy.linspace(0,width,ny)

# initialize the velocities u and v and the temperory velocities un and vn
u = numpy.ones((ny,nx)) # need two brackets after ones
v = numpy.ones((ny,nx))
un = numpy.ones((ny,nx))
vn = numpy.ones((ny,nx))

# Initial Conditions set up
u[int(0.5/dy):int(1/dy+1),int(0.5/dx):int(1/dx+1)] = initTemp
v[int(0.5/dy):int(1/dy+1),int(0.5/dx):int(1/dx+1)] = initTemp

# Graph with I.C.
fig = pyplot.figure(figsize=(11, 7), dpi=100)
ax = fig.gca(projection='3d')
X, Y = numpy.meshgrid(x, y)
ax.plot_surface(X, Y, u[:], cmap=cm.viridis, rstride=1, cstride=1)
ax.plot_surface(X, Y, v[:], cmap=cm.viridis, rstride=1, cstride=1)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$');

# Time iterations
for t in range(1,nt+1):
    un = u.copy()
    vn = v.copy()
    
    # Interesting discovery: the expression on the RHS yields correct result only if put inside brackets
    u[1:-1, 1:-1] = (un[1:-1, 1:-1] - (dt/dx) * un[1:-1, 1:-1] *(un[1:-1, 1:-1]-un[1:-1, 0:-2])
    - (dt/dy) * vn[1:-1, 1:-1] *(un[1:-1, 1:-1]-un[0:-2, 1:-1])
    + (nu*dt/dx**2) * (un[1:-1, 2:] - 2 * un[1:-1, 1:-1] + un[1:-1, 0:-2])
    + (nu*dt/dy**2) * (un[2:, 1:-1] - 2 * un[1:-1, 1:-1] + un[0:-2, 1:-1]))

   
    v[1:-1, 1:-1] = (vn[1:-1, 1:-1] - (dt/dx) * un[1:-1, 1:-1] * (vn[1:-1, 1:-1] - vn[1:-1, 0:-2])
    - (dt/dy) * vn[1:-1, 1:-1] * (vn[1:-1, 1:-1] - vn[0:-2, 1:-1])
    + (nu*dt/dx**2) * (vn[1:-1, 2:] - 2 * vn[1:-1, 1:-1] + vn[1:-1, 0:-2])
    + (nu*dt/dy**2) * (vn[2:, 1:-1] - 2 * vn[1:-1, 1:-1] + vn[0:-2, 1:-1]))
    
    # Boundary Conditions
    u[0, :] = 1
    u[-1, :] = 1
    u[:, 0] = 1
    u[:, -1] = 1
    
    v[0, :] = 1
    v[-1, :] = 1
    v[:, 0] = 1
    v[:, -1] = 1   


# Graph
fig = pyplot.figure(figsize=(11, 7), dpi=100)
ax = fig.gca(projection='3d')
X, Y = numpy.meshgrid(x, y)
ax.plot_surface(X, Y, u, cmap=cm.viridis, rstride=1, cstride=1)
ax.plot_surface(X, Y, v, cmap=cm.viridis, rstride=1, cstride=1)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$');