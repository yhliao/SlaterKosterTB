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


plt.figure()
plt.plot(np.vstack([E_GM,E_MK,E_KG]))
plt.ylim([-2.5,2.5])
#plt.show()


#################################################################
################calculating effective mass#######################
#################################################################


X_m_x=np.array([K[4],K[3],K[2],K[1],K[0],K[1],K[2],K[3],K[4]])
Y_m_x=np.array([E_KG[4,14],E_KG[3,14],E_KG[2,14],E_KG[1,14],E_KG[0,14],E_KG[1,14],E_KG[2,14],E_KG[3,14],E_KG[4,14]])
X_m_x=X_m_x*4/3/(3.18E-10)
def extract_meff_x(x,B_x):
	return (0.89855916+  B_x * x*x )

B_x  = optimize.curve_fit(extract_meff_x, X_m_x, Y_m_x)[0]

m_x=(1.0545718E-34)**2 / (B_x*2*1.6E-19)


x_test_x = np.arange(0, 0.4E10, 1E7)
y_test_x=0.89855916+  B_x * x_test_x*x_test_x 
plt.figure()
plt.plot(K*4/3/(3.18E-10),E_KG,"-o")
plt.plot(x_test_x,y_test_x,"red")
plt.ylim([-2.5,2.5])
plt.xlim([0,0.4E10])
print(m_x/9.11E-31)
#plt.show()

##

X_m_y=np.array([K[4],K[3],K[2],K[1],K[0],K[1],K[2],K[3],K[4]])
Y_m_y=np.array([E_MK[195,14],E_MK[196,14],E_MK[197,14],E_MK[198,14],E_MK[199,14],E_MK[198,14],E_MK[197,14],E_MK[196,14],E_MK[195,14]])
X_m_y=X_m_y*2/3/(3.18E-10)
def extract_meff_y(x,B_y):
	return (0.89855916437+  B_y * x*x )

B_y  = optimize.curve_fit(extract_meff_y, X_m_y, Y_m_y)[0]

m_y=(1.0545718E-34)**2 / (B_y*2*1.6E-19)


x_test_y = np.arange(-0.4E10, 0, 1E7)
y_test_y=0.89855916437+  B_y * x_test_y*x_test_y 
plt.figure()
plt.plot(K*2/3/(3.18E-10),E_MK,"-o")
plt.plot(x_test_y+6.58614812E09,y_test_y,"red")
plt.ylim([-2.5,2.5])
plt.xlim([4E9,6.58614812E09])
print(m_y/9.11E-31)


plt.show()

#print(K*2/3/(3.18E-10))

#print(E_MK[199,14])
