import numpy as np
from MoS2TB import H, H_dim
from numpy.linalg import eigh
from math import sqrt
from matplotlib import pyplot as plt

step = 800
Kx = np.linspace(0,2*np.pi,step)
Ky = np.linspace(-2*np.pi/sqrt(3),2*np.pi/sqrt(3),step)
Kgrid = np.meshgrid(Kx,Ky)

E = np.zeros([H_dim,step,step])
for i,kx in enumerate(Kx):
   for j,ky in enumerate(Ky):
      E[:,i,j],_ = eigh(H([kx,ky]))

np.save("MoS2fullband",E)

plt.subplot(121)
plt.imshow(E[14,:,:])
plt.colorbar()
plt.subplot(122)
plt.imshow(E[13,:,:])
plt.colorbar()
plt.show()
