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


#################################################################
################calculating effective mass#######################
#################################################################
Ec   = 0.89855916
hbar = 1.0545718e-34
e    = 1.6e-19
a0   = 3.18e-10
m0   = 9.11e-31
k0 = 6.68614812e9*2
def extract_meff(x,B):
	return (Ec+  B * x*x )

idx_x = [4,3,2,1,0,1,2,3,4]
X_m_x = K[idx_x]
Y_m_x = E_KG[:,14][idx_x]
X_m_x = X_m_x*4/3/a0

B_x = optimize.curve_fit(extract_meff, X_m_x, Y_m_x)[0]
m_x = hbar**2 / (B_x*2*e)
print(m_x/m0)

x_test_x = np.arange(-.4E10, 0.4E10, 1E7)
y_test_x = Ec + B_x * x_test_x**2

fig2 = plt.figure()
ax21 = fig2.add_subplot(121)
ax22 = fig2.add_subplot(122)
ax21.plot(
   k0+np.concatenate((-np.flip(K,0)*4/3/a0,K*4/3/a0)),
   np.vstack((np.flip(E_KG,0),E_KG)))
ax21.plot(x_test_x+k0,y_test_x,'--',c="red")
ax21.set_xlim([-6e9+k0,6e9+k0])
ax21.set_ylim([-2.5,2.5])
ax21.set_xlabel("$k_x$ $(m^{-1})$")
ax21.set_title("(a) $k_y$=0")
##
idx_y = range(195,199)+range(199,194,-1)
X_m_y = K[idx_x]
Y_m_y = E_MK[:,14][idx_y]
X_m_y = X_m_y*2/3/a0

B_y = optimize.curve_fit(extract_meff, X_m_y, Y_m_y)[0]
m_y = hbar**2 / (B_y*2*e)

x_test_y = np.arange(-0.4E10, 0.4e10, 1E7)
y_test_y = Ec +  B_y * x_test_y**2
print(m_y/m0)

ax22.plot(
   np.concatenate((-np.flip(K*2/3/a0,0),K*2/3/a0)),
   np.vstack((E_MK,np.flip(E_MK,0))))
ax22.plot(x_test_y,y_test_y,'--',c="red")
ax22.set_ylim([-2.5,2.5])
ax22.set_xlim([-6e9,6e9])
ax22.set_xlabel("$k_y$ $(m^{-1})$")
ax22.set_title("(b) $k_x$=$4\pi/3a_0$")

plt.show()
