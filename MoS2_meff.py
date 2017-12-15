from SKmatrix.MoS2TB import H, H_dim
from matplotlib import pyplot as plt
import numpy as np
from numpy.linalg import eigh
from math import sqrt
from scipy import optimize

fig = plt.figure()
axMK = fig.add_subplot(141)
axMKt= fig.add_subplot(142)
axGK = fig.add_subplot(143)
axGKt= fig.add_subplot(144)
axMK.set_ylabel("E (eV)",fontsize=14)
axMK.set_xticks([])
axMKt.set_xticks([])
axMKt.set_yticks([])
axGK.set_xticks([])
axGK.set_yticks([])
axGKt.set_xticks([])
axGKt.set_yticks([])

Ec   = 0.89855916
hbar = 1.0545718e-34
e    = 1.6e-19
a0   = 3.18e-10
m0   = 9.11e-31
k0 = 6.68614812e9*2
def EK_meff(x,B):
	return (Ec+  B * x*x )

E_MK = np.zeros([200,H_dim])
E_MKt= np.zeros([200,H_dim])
E_GK = np.zeros([200,H_dim])
E_GKt= np.zeros([200,H_dim])
idx_l = range(195,200)
idx_t = range(5)

K = np.linspace(0,2*np.pi/3,200)
for i,kx in enumerate(K):
   k_MK = [kx,2*np.pi/sqrt(3)]
   E,_  = eigh(H(k_MK))
   E_MK[i,:] = E
k_MKl = K/a0
k_MK0 = np.max(k_MKl)
B = optimize.curve_fit(EK_meff,
   k_MKl[idx_l]-k_MK0,E_MK[:,14][idx_l])[0]
m_MKl = hbar**2 / (B*2*e)
axMK.plot(k_MKl,E_MK)
axMK.plot(k_MKl,EK_meff(k_MKl-k_MK0,B),'--',c="r")
axMK.set_ylim([-2.5,2.5])
axMK.set_title("(a) M-K longitudinal")
print("m_MKl= {} m0".format(m_MKl/m0))

K = np.linspace(0,2*np.pi/3,200)
for i,ky in enumerate(K):
   k_MKt = [2*np.pi/3,2*np.pi/sqrt(3)+ky]
   E,_  = eigh(H(k_MKt))
   E_MKt[i,:] = E
k_MKt = K/a0
B = optimize.curve_fit(EK_meff,
   k_MKt[idx_t],E_MKt[:,14][idx_t])[0]
m_MKt = hbar**2 / (B*2*e)
axMKt.plot(k_MKt,E_MKt)
axMKt.plot(k_MKt,EK_meff(k_MKt,B),'--',c="r")
axMKt.set_ylim([-2.5,2.5])
axMKt.set_title("(b) M-K transverse")
print("m_MKt= {} m0".format(m_MKt/m0))

K = np.linspace(2*np.pi/3,4*np.pi/3,200)
for i,kx in enumerate(K):
   k_GK = [kx,0]
   E,_  = eigh(H(k_GK))
   E_GK[i,:] = E
k_GKl = K/a0
k_GK0 = np.max(k_GKl)
B = optimize.curve_fit(EK_meff, 
      k_GKl[idx_l]-k_GK0, E_GK[:,14][idx_l])[0]
m_GKl = hbar**2 / (B*2*e)
axGK.plot(k_GKl,E_GK)
axGK.plot(k_GKl,EK_meff(k_GKl-k_GK0,B),'--',c='r')
axGK.set_ylim([-2.5,2.5])
axGK.set_title("(c) $\Gamma$-K longitudinal")
print("m_GKl= {} m0".format(m_GKl/m0))

K = np.linspace(0,2*np.pi/3,200)
for i,ky in enumerate(K):
   k_GKt = [4*np.pi/3,ky]
   E,_  = eigh(H(k_GKt))
   E_GKt[i,:] = E
k_GKt = K/a0
B = optimize.curve_fit(EK_meff,
   k_GKt[idx_t],E_GKt[:,14][idx_t])[0]
m_GKt = hbar**2 / (B*2*e)
axGKt.plot(k_GKt,E_GKt)
axGKt.plot(k_GKt,EK_meff(k_GKt,B),'--',c="r")
axGKt.set_ylim([-2.5,2.5])
axGKt.set_title("(d) $\Gamma$-K transverse")
print("m_GKt= {} m0".format(m_MKt/m0))
plt.show()
"""
print(sqrt(2*0.0259*e/np.pi/m_y))

#plt.show()"""
