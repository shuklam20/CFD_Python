
# Importing the libraries
from mpl_toolkits.mplot3d import Axes3D    ##New Library required for projected 3d plots

import numpy
from matplotlib import pyplot, cm


# Iterative solver for 2D Diffusion process
def Diffusion(u, nu, dx, dy, dt, nt):
    un = numpy.empty_like(u) # Define un with same structure as u

    for t in range(1,nt+1):
        un=u.copy() # remember the matrix is u(y,x) and not u(x,y)
        u[1:-1, 1:-1] = (un[1:-1,1:-1] + 
                        nu * dt / dx**2 * 
                        (un[1:-1, 2:] - 2 * un[1:-1, 1:-1] + un[1:-1, 0:-2]) +
                        nu * dt / dy**2 * 
                        (un[2:,1: -1] - 2 * un[1:-1, 1:-1] + un[0:-2, 1:-1]))
        u[0, :] = 1
        u[-1, :] = 1
        u[:, 0] = 1
        u[:, -1] = 1

    return u


# variables' declarations
length = 2
width = 2
initVel = 2
nx = 31
ny = 31
nt = 17
nu = .05
dx = 2 / (nx - 1)
dy = 2 / (ny - 1)
sigma = .25
dt = sigma * dx * dy / nu   # definition of sigma for 2D diffusion equation

# define x and y nodes
x = numpy.linspace(0,length,nx)
y = numpy.linspace(0,width,ny)

# initialize the velocities u and v and the temperory velocities un and vn
u = numpy.ones((ny,nx)) # need two brackets after ones

# Apply the Initial conditions for 0.5<=x<=1 and 0.5<=y<=1 
u[int(0.5/dy):int(1/dy+1), int(0.5/dx):int(1/dx+1)] = initVel


## Plot the initial conditions
#fig = pyplot.figure(figsize=(11, 7), dpi=100)
#ax = fig.gca(projection='3d')
#X, Y = numpy.meshgrid(x, y)
#
#ax.plot_surface(X, Y, u, cmap=cm.viridis, rstride=2, cstride=2)
#ax.set_xlabel('$x$')
#ax.set_ylabel('$y$')

fig = pyplot.figure()
ax = fig.gca(projection='3d')
X, Y = numpy.meshgrid(x, y)
surf = ax.plot_surface(X, Y, u, rstride=1, cstride=1, cmap=cm.viridis,
        linewidth=0, antialiased=False)

ax.set_xlim(0, 2)
ax.set_ylim(0, 2)
ax.set_zlim(1, 2.5)

ax.set_xlabel('$x$')
ax.set_ylabel('$y$');

u = Diffusion(u, nu, dx, dy, dt, nt)

#print(u)



#fig = pyplot.figure()
#ax = fig.gca(projection='3d')
#surf = ax.plot_surface(X, Y, u[:], rstride=1, cstride=1, cmap=cm.viridis,
#    linewidth=0, antialiased=True)
#ax.set_zlim(1, 2.5)
#ax.set_xlabel('$x$')
#ax.set_ylabel('$y$')

