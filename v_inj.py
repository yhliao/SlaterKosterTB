import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm
from math import sqrt

h_bar = 1.0545718e-34
e  = 1.60217662e-19
a0 = 3.18e-10
b = a0/2
a = a0*sqrt(3)/2

E = np.load("MoS2fullBand.npy")
kstepx = E.shape[1]
kstepy = E.shape[2]
dkx =   (np.pi/b)/(kstepx-1)
dky = (2*np.pi/a)/(kstepy-1)

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
#fig2 = plt.figure()
#ax2 = fig2.add_subplot(121)
#ax3 = fig2.add_subplot(122)

#ca = ax1.imshow(E[14,:,:],cmap=cm.coolwarm)
#fig1.colorbar(ca,orientation="vertical")

kBT = 0.0259 ## eV
def fE(mu,E):
   return 1./(1+np.exp((E-mu)/kBT))

def v_inj(mus,maxband=16):
   assert maxband >= 15
   sum_fv_x = 0
   sum_f_x  = 0
   sum_fv_y = 0
   sum_f_y  = 0

   for i in range(14,maxband):
      ### the i-th band for conduction band
      Ei =  E[i,:,:]
      ### group velocity Del_k(E)/h_bar
      vx = e*np.diff(Ei,axis=0)/dkx/h_bar
      vy = e*np.diff(Ei,axis=1)/dky/h_bar
      ### the interpolated energy for Fermi-Dirac statistics
      E_vx = (Ei[1:,:] + Ei[:-1,:] )/2
      E_vy = (Ei[:,1:] + Ei[:,:-1] )/2
      assert vx.shape==E_vx.shape
      assert vy.shape==E_vy.shape
      idx = vx > 0 
      idy = vy > 0

      f_x = fE(mus,E_vx[idx])
      f_y = fE(mus,E_vy[idy])
      sum_f_x  += np.sum(f_x)
      sum_f_y  += np.sum(f_y)
      sum_fv_x += np.sum(f_x*vx[idx])
      sum_fv_y += np.sum(f_y*vy[idy])
   v_injx = sum_fv_x / sum_f_x
   v_injy = sum_fv_y / sum_f_y
   return v_injx, v_injy

Ecmin = np.min(E[14,:,:])
Evmax = np.max(E[13,:,:])
print ("Conduction Band Edge: {}eV".format(Ecmin))
print ("Valence Band Edge: {}eV".format(Evmax))
print ("Bandgap: {}eV".format(Ecmin-Evmax))

MUS = np.linspace(0,0.9,20)
etas = MUS-Ecmin
pattern = ['-^','-o']
label = ['lowest CB only','Whole band']
for imax,pat,lab in zip([15,16],pattern,label): 
   VX = []
   VY = []

   print imax
   for mus in MUS:
      vx, vy = v_inj(mus,imax)
      print vx,vy
      VX.append(vx*100/1e7)
      VY.append(vy*100/1e7)

   ax1.plot(etas,VX,pat,c='r',label="$v_{inj,x}$ "+lab)
   ax1.plot(etas,VY,pat,c='g',label="$v_{inj,y}$ "+lab)

ax1.set_xlabel('$\mu_s-E_c\ (eV)$',fontsize=14)
ax1.set_ylabel('$v_{inj}\ (10^7cm/s)$',fontsize=14)
ax1.axhline(0.8385,linestyle='--',label="approximation from $m_{eff}$ (non-degenerate)")
ax1.grid()
ax1.legend(fontsize=12)
plt.show()
