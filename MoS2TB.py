from param_OnSite import Mo, S
from param_SK import MoMo, SS, MoS, SMo
from matrix_def import TBblock 
from math import sqrt

d00 = [0,0]
d01 = [sqrt(3)/2,1./2]
d02 = [0,1]
d03 = [-sqrt(3)/2,1./2]

H00 = TBblock(d00)
H01 = TBblock(d01)
H02 = TBblock(d02)
H03 = TBblock(d03)

### H00 onsite
H00.fill_Onsite("Mo" ,Mo)
H00.fill_Onsite("S_u",S)
H00.fill_Onsite("S_d",S)
### TODO: 2 Mo-S bonds

### H01
H01.fill_SK("Mo" ,"Mo" ,[-1./2,sqrt(3)/2,0],MoMo)
H01.fill_SK("S_u","S_u",[-1./2,sqrt(3)/2,0],SS)
H01.fill_SK("S_d","S_d",[-1./2,sqrt(3)/2,0],SS)
### TODO: 2 S-Mo bonds

### H02
H02.fill_SK("Mo" ,"Mo" ,[-1,0,0],MoMo)
H02.fill_SK("S_u","S_u",[-1,0,0],SS)
H02.fill_SK("S_d","S_d",[-1,0,0],SS)

### H03
H03.fill_SK("Mo" ,"Mo" ,[-1./2,-sqrt(3)/2,0],MoMo)
H03.fill_SK("S_u","S_u",[-1./2,-sqrt(3)/2,0],SS)
H03.fill_SK("S_d","S_d",[-1./2,-sqrt(3)/2,0],SS)
### TODO: 2 Mo-S bonds


### H04
H04.fill_SK("Mo" ,"Mo" ,[1./2,-sqrt(3)/2,0],MoMo)
H04.fill_SK("S_u","S_u",[1./2,-sqrt(3)/2,0],SS)
H04.fill_SK("S_d","S_d",[1./2,-sqrt(3)/2,0],SS)
H04.fill_SK("S_d","S_d",[0.4483428791,-0.7765526458,0.4426676528],MoS)
H04.fill_SK("S_d","S_d",[0.4483428791,-0.7765526458,-0.4426676528],MoS)


### H05
H05.fill_SK("Mo" ,"Mo" ,[1,0,0],MoMo)
H05.fill_SK("S_u","S_u",[1,0,0],SS)
H05.fill_SK("S_d","S_d",[1,0,0],SS)

### H06
H06.fill_SK("Mo" ,"Mo" ,[1./2,sqrt(3)/2,0],MoMo)
H06.fill_SK("S_u","S_u",[1./2,sqrt(3)/2,0],SS)
H06.fill_SK("S_d","S_d",[1./2,sqrt(3)/2,0],SS)
H06.fill_SK("S_d","S_d",[0.4483428791,0.7765526458,0.4426676528],SMo)
H06.fill_SK("S_d","S_d",[0.4483428791,0.7765526458,-0.4426676528],SMo)
