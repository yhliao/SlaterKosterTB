########################################################
### S-K parameters from Varun's paper
## "    Screening in Ultrashort (5nm) Channel MoS2 
##   Transistors: A Full-Band Quantum Transport Study"
## IEEE TED, Vol.62, No. 8, Aug. 2015
########################################################

SS = {
  "ss_sigma": -0.8590,
  "sp_sigma": -0.2142,
  "pp_sigma":  0.8715,
  "pp_pi"   : -0.2449,
  "sd_sigma":  3.1818,
  "pd_sigma":  0.1138,
  "pd_pi"   : -0.4476,
  "dd_sigma":  3.7203,
  "dd_pi"   : -2.5901,
  "dd_delta": -1.1719,
  "flipsite": SS
}


MoMo = {
  "ss_sigma": -1.5166,
  "sp_sigma":  0.4991,
  "pp_sigma": -3.8198,
  "pp_pi"   :  4.5562,
  "sd_sigma":0.007971,
  "pd_sigma":  1.3306,
  "pd_pi"   : 0.95906,
  "dd_sigma": 0.95906,
  "dd_pi"   : -0.4520,
  "dd_delta":  0.5143,
  "flipsite": MoMo
}

MoS = {
  "ss_sigma": -0.1246,
  "flipsite":SMo
}

SMo = {
  "ss_sigma": -0.1246,
  "flipsite":MoS
}
