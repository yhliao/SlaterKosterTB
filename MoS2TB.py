from param_OnSite import Mo, S
from param_SK import MoMo, SS, MoS, SMo
from matrix_def import TBblock 
from math import sqrt
from numpy.linalg import norm

### Direction Cosines
def lmn(r):
   assert(len(r)==3)
   l = r[0]/norm(r)
   m = r[1]/norm(r)
   n = r[2]/norm(r)
   return [l,m,n]

d00 = [0,0]
d01 = [sqrt(3)/2,1./2]
d02 = [0,1]
d03 = [-sqrt(3)/2,1./2]

H00 = TBblock(d00)
H01 = TBblock(d01)
H02 = TBblock(d02)
H03 = TBblock(d03)

a=3.16
c=3.12
### H00 onsite
H00.fill_Onsite("Mo" ,Mo)
H00.fill_Onsite("S_u",S)
H00.fill_Onsite("S_d",S)
H00.fill_SK("Mo","S_u", lmn([0,a/sqrt(3),c/2]),MoS)
H00.fill_SK("Mo","S_d", lmn([0,a/sqrt(3),-c/2]),MoS)
H00.fill_SK("S_u","Mo", lmn([0,-a/sqrt(3),-c/2]),SMo)
H00.fill_SK("S_d","Mo", lmn([0,-a/sqrt(3),c/2]),SMo)

### H01
H01.fill_SK("Mo" ,"Mo" ,[-1./2,sqrt(3)/2,0],MoMo)
H01.fill_SK("S_u","S_u",[-1./2,sqrt(3)/2,0],SS)
H01.fill_SK("S_d","S_d",[-1./2,sqrt(3)/2,0],SS)
H01.fill_SK("S_u","Mo",[-a/2,a/(2*sqrt(3)),-c/2],SMo)
H01.fill_SK("S_d","Mo",[-a/2,a/(2*sqrt(3)), c/2],SMo)

### H02
H02.fill_SK("Mo" ,"Mo" ,[-1,0,0],MoMo)
H02.fill_SK("S_u","S_u",[-1,0,0],SS)
H02.fill_SK("S_d","S_d",[-1,0,0],SS)

### H03
H03.fill_SK("Mo" ,"Mo" ,[-1./2,-sqrt(3)/2,0],MoMo)
H03.fill_SK("S_u","S_u",[-1./2,-sqrt(3)/2,0],SS)
H03.fill_SK("S_d","S_d",[-1./2,-sqrt(3)/2,0],SS)
H03.fill_SK("Mo","S_u",[-a/2,-a/(2*sqrt(3)),c/2],SS)
H03.fill_SK("Mo","S_d",[-a/2,-a/(2*sqrt(3)),-c/2],SS)

