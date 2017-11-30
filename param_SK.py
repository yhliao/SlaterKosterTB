########################################################
### S-K parameters from Varun's paper
## "    Screening in Ultrashort (5nm) Channel MoS2 
##   Transistors: A Full-Band Quantum Transport Study"
## IEEE TED, Vol.62, No. 8, Aug. 2015
########################################################

global SS, MoMo, MoS, SMo

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
}

MoS = {
  "ss_sigma": -0.1246,
  "sp_sigma":  1.1862,
  "pp_sigma":  1.2385,
  "pp_pi"   : -0.2589,
  "sd_sigma": 10.4024,
  "pd_sigma": 16.3744,
  "pd_pi"   :-16.6761,
  "dd_sigma":  4.8937,
  "dd_pi"   : -9.3391,
  "dd_delta":  1.2478,
}

SMo = {
  "ss_sigma": -0.1246,
  "sp_sigma":  3.9553,
  "pp_sigma":  1.2385,
  "pp_pi"   : -0.2589,
  "sd_sigma":  1.6798,
  "pd_sigma": -2.8710,
  "pd_pi"   :  0.8901,
  "dd_sigma":  4.8937,
  "dd_pi"   : -9.3391,
  "dd_delta":  1.2478,
}

SS  ["flipsite"] = SS
MoMo["flipsite"] = MoMo
MoS ["flipsite"] = SMo
SMo ["flipsite"] = MoS
