from __future__ import division
from param_OnSite import Mo, S
from param_SK import MoMo, SS, MoS, SMo
from matrix_def import TBblock, H_dim
from math import sqrt
from numpy.linalg import norm, eigh
import numpy as np
from matplotlib import pyplot as plt
### Direction Cosines
def lmn(r):
   assert(len(r)==3)
   l = r[0]/norm(r)
   m = r[1]/norm(r)
   n = r[2]/norm(r)
   return [l,m,n]

def H(K):
   H = H00.get_block(K)
   H += H01.get_block(K)
   H += H02.get_block(K)
   H += H03.get_block(K)
   H += H04.get_block(K)
   H += H05.get_block(K)
   H += H06.get_block(K)
   assert np.isclose(np.sum(H-H.H),0)
   return H

a=3.18
c=3.12

d00 = [0, 0]
H00 = TBblock(d00)
### H00 onsite
H00.fill_Onsite("Mo" ,Mo)
H00.fill_Onsite("S_u",S)
H00.fill_Onsite("S_d",S)
H00.fill_SK("Mo","S_u", lmn([0,a/sqrt(3),c/2]),MoS)
H00.fill_SK("Mo","S_d", lmn([0,a/sqrt(3),-c/2]),MoS)
H00.fill_SK("S_u","Mo", lmn([0,-a/sqrt(3),-c/2]),SMo)
H00.fill_SK("S_d","Mo", lmn([0,-a/sqrt(3),c/2]),SMo)
H00.fill_SK("S_u","S_d", lmn([0,0,-1]),SS)
H00.fill_SK("S_d","S_u", lmn([0,0,1]),SS)

d01 = [-1./2, sqrt(3)/2]
H01 = TBblock(d01)
### H01
H01.fill_SK("Mo" ,"Mo" ,[-1./2,sqrt(3)/2,0],MoMo)
H01.fill_SK("S_u","S_u",[-1./2,sqrt(3)/2,0],SS)
H01.fill_SK("S_d","S_d",[-1./2,sqrt(3)/2,0],SS)
H01.fill_SK("S_u","Mo",lmn([-a/2,a/(2*sqrt(3)),-c/2]),SMo)
H01.fill_SK("S_d","Mo",lmn([-a/2,a/(2*sqrt(3)), c/2]),SMo)

d04 = [ 1./2,-sqrt(3)/2]
H04 = TBblock(d04)
H04.fill_SK("Mo" ,"Mo" ,[1./2,-sqrt(3)/2,0],MoMo)
H04.fill_SK("S_u","S_u",[1./2,-sqrt(3)/2,0],SS)
H04.fill_SK("S_d","S_d",[1./2,-sqrt(3)/2,0],SS)
H04.fill_SK("Mo","S_u",lmn([a/2,-a/(2*sqrt(3)),c/2]),MoS)
H04.fill_SK("Mo","S_d",lmn([a/2,-a/(2*sqrt(3)),-c/2]),MoS)


d02 = [-1,0]
H02 = TBblock(d02)
### H02
H02.fill_SK("Mo" ,"Mo" ,[-1,0,0],MoMo)
H02.fill_SK("S_u","S_u",[-1,0,0],SS)
H02.fill_SK("S_d","S_d",[-1,0,0],SS)

d05 = [ 1   , 0        ]
H05 = TBblock(d05)
### H05
H05.fill_SK("Mo" ,"Mo" ,[1,0,0],MoMo)
H05.fill_SK("S_u","S_u",[1,0,0],SS)
H05.fill_SK("S_d","S_d",[1,0,0],SS)

d03 = [-1./2,-sqrt(3)/2]
H03 = TBblock(d03)
### H03
H03.fill_SK("Mo" ,"Mo" ,[-1./2,-sqrt(3)/2,0],MoMo)
H03.fill_SK("S_u","S_u",[-1./2,-sqrt(3)/2,0],SS)
H03.fill_SK("S_d","S_d",[-1./2,-sqrt(3)/2,0],SS)
H03.fill_SK("Mo","S_u",lmn([-a/2,-a/(2*sqrt(3)), c/2]),MoS)
H03.fill_SK("Mo","S_d",lmn([-a/2,-a/(2*sqrt(3)),-c/2]),MoS)

d06 = [ 1./2, sqrt(3)/2]
H06 = TBblock(d06)
## H06
H06.fill_SK("Mo" ,"Mo" ,[1./2,sqrt(3)/2,0],MoMo)
H06.fill_SK("S_u","S_u",[1./2,sqrt(3)/2,0],SS)
H06.fill_SK("S_d","S_d",[1./2,sqrt(3)/2,0],SS)
H06.fill_SK("S_u","Mo",lmn([a/2,a/(2*sqrt(3)),-c/2]),SMo)
H06.fill_SK("S_d","Mo",lmn([a/2,a/(2*sqrt(3)), c/2]),SMo)



print lmn([a/2,a/(2*sqrt(3)),-c/2])
E_GM = np.zeros([1000,H_dim])
K_GM = np.linspace(-2*np.pi,2*np.pi,1000)
for i,kx in enumerate(K_GM):
   k   = [kx,0]
   E,_ = eigh(H(k))
   E_GM[i,:] = E

plt.plot(K_GM,E_GM[:,:])
plt.ylim([-5,5])
plt.grid()
plt.show()

