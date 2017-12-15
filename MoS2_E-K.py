from SKmatrix.MoS2TB import H, H_dim
from matplotlib import pyplot as plt
import numpy as np
from numpy.linalg import eigh
from math import sqrt
from scipy import optimize

fig = plt.figure()
axGM = fig.add_subplot(131)
axMK = fig.add_subplot(132)
axKG = fig.add_subplot(133)

K = np.linspace(0,np.pi,200)
E_GM = np.zeros([200,H_dim])
E_MK = np.zeros([200,H_dim])
E_KG = np.zeros([200,H_dim])

for i,ky in enumerate(2*K/sqrt(3)):
   k_GM = [0,ky]
   E,_  = eigh(H(k_GM))
   E_GM[i,:] = E
axGM.plot(K,E_GM)
axGM.set_ylim([-2.5,2.5])
axGM.set_ylabel("Energy (eV)")
axGM.set_xticks([])
axGM.set_title("(a) $\Gamma$-M")
for i,kx in enumerate(2*K/3):
   k_MK = [kx,2*np.pi/sqrt(3)]
   E,_  = eigh(H(k_MK))
   E_MK[i,:] = E
axMK.plot(K,E_MK)
axMK.set_ylim([-2.5,2.5])
axMK.set_xticks([])
axMK.set_title("(b) M-K")


for i,kx in enumerate(reversed(4*K/3)):
   k_KG = [kx,0]
   E,_  = eigh(H(k_KG))
   E_KG[i,:] = E
axKG.plot(K,E_KG)
axKG.set_ylim([-2.5,2.5])
axKG.set_xticks([])
axKG.set_title("(c) K-$\Gamma$")


#plt.figure()
#plt.plot(np.vstack([E_GM,E_MK,E_KG]))
#plt.ylim([-2.5,2.5])
#plt.show()

