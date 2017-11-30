from math import sqrt

class SK2E:
   def __init__(self):
      pass

   def calc_E(self,l,m,n,orb1,orb2,SKparam):
      ### Remove spin dependencies
      orb1 = orb1.replace("_","")
      orb2 = orb2.replace("_","")
      ### Concatenate orbital names for method query
      Eorb1_orb2  = "E" + orb1 + "_" + orb2
      Emethod = getattr(self,Eorb1_orb2)
      return Emethod(l,m,n,SKparam)

   ### Es_*
   def Es_s(self,l,m,n,SKparam):
      return SKparam["ss_sigma"]

   def Es_x(self,l,m,n,SKparam):
      return l * SKparam["sp_sigma"]
   
   def Es_y(self,l,m,n,SKparam):
      return m * SKparam["sp_sigma"]
   
   def Es_z(self,l,m,n,SKparam):
      return n * SKparam["sp_sigma"]
   
   def Es_xy(self,l,m,n,SKparam):
      return sqrt(3) * l * m * SKparam["sd_sigma"]

   def Es_yz(self,l,m,n,SKparam):
      return sqrt(3) * m * n * SKparam["sd_sigma"]

   def Es_xz(self,l,m,n,SKparam):
      return sqrt(3) * l * n * SKparam["sd_sigma"]

   def Es_x2y2(self,l,m,n,SKparam):
      return 0.5*sqrt(3) * (l**2-m**2) * SKparam["sd_sigma"]

   def Es_3z2r2(self,l,m,n,SKparam):
      return (n**2 - 0.5*(l**2+m**2)) * SKparam["sd_sigma"]
   
   ### Ex_*
   def Ex_s(self,l,m,n,SKparam):
      return self.Es_x(-l,-m,-n,SKparam["flipsite"])

   def Ex_x(self,l,m,n,SKparam):
      return (     l**2  * SKparam["pp_sigma"] 
              + (1-l**2) * SKparam["pp_pi"])

   def Ex_y(self,l,m,n,SKparam):
      return (   l*m * SKparam["pp_sigma"] 
                -l*m * SKparam["pp_pi"])

   def Ex_z(self,l,m,n,SKparam):
      return (   l*n * SKparam["pp_sigma"] 
                -l*n * SKparam["pp_pi"])

   def Ex_xy(self,l,m,n,SKparam):
      pass #TODO
   def Ex_yz(self,l,m,n,SKparam):
      pass #TODO
   def Ex_xz(self,l,m,n,SKparam):
      pass #TODO
   def Ex_x2y2(self,l,m,n,SKparam):
      pass #TODO
   def Ex_3z2r2(self,l,m,n,SKparam):
      pass #TODO

   ### Ey_*
   def Ey_s(self,l,m,n,SKparam):
      return self.Es_y(-l,-m,-n,SKparam["flipsite"])
   def Ey_x(self,l,m,n,SKparam):
      return self.Ex_y(-l,-m,-n,SKparam["flipsite"])
   def Ey_y(self,l,m,n,SKparam):
      pass #TODO
   def Ey_z(self,l,m,n,SKparam):
      pass #TODO
   def Ey_xy(self,l,m,n,SKparam):
      pass #TODO
   def Ey_yz(self,l,m,n,SKparam):
      pass #TODO
   def Ey_xz(self,l,m,n,SKparam):
      pass #TODO
   def Ey_x2y2(self,l,m,n,SKparam):
      pass #TODO
   def Ey_3z2r2(self,l,m,n,SKparam):
      pass #TODO

   ### Ez_*
   def Ez_s(self,l,m,n,SKparam):
      return self.Es_z(-l,-m,-n,SKparam["flipsite"])
   def Ez_x(self,l,m,n,SKparam):
      return self.Ex_z(-l,-m,-n,SKparam["flipsite"])
   def Ez_y(self,l,m,n,SKparam):
      return self.Ey_z(-l,-m,-n,SKparam["flipsite"])
   def Ez_z(self,l,m,n,SKparam):
      pass #TODO
   def Ez_xy(self,l,m,n,SKparam):
      pass #TODO
   def Ez_yz(self,l,m,n,SKparam):
      pass #TODO
   def Ez_xz(self,l,m,n,SKparam):
      pass #TODO
   def Ez_x2y2(self,l,m,n,SKparam):
      pass #TODO
   def Ez_3z2r2(self,l,m,n,SKparam):
      pass #TODO

   ### Exy_*
   def Exy_s(self,l,m,n,SKparam):
      return self.Es_xy(-l,-m,-n,SKparam["flipsite"])
   def Exy_x(self,l,m,n,SKparam):
      return self.Ex_xy(-l,-m,-n,SKparam["flipsite"])
   def Exy_y(self,l,m,n,SKparam):
      return self.Ey_xy(-l,-m,-n,SKparam["flipsite"])
   def Exy_z(self,l,m,n,SKparam):
      return self.Ez_xy(-l,-m,-n,SKparam["flipsite"])
   def Exy_xy(self,l,m,n,SKparam):
      pass #TODO
   def Exy_yz(self,l,m,n,SKparam):
      pass #TODO
   def Exy_xz(self,l,m,n,SKparam):
      pass #TODO
   def Exy_x2y2(self,l,m,n,SKparam):
      pass #TODO
   def Exy_3z2r2(self,l,m,n,SKparam):
      pass #TODO

   ### Eyz_*
   def Eyz_s(self,l,m,n,SKparam):
      return self.Es_yz(-l,-m,-n,SKparam["flipsite"])
   def Eyz_x(self,l,m,n,SKparam):
      return self.Ex_yz(-l,-m,-n,SKparam["flipsite"])
   def Eyz_y(self,l,m,n,SKparam):
      return self.Ey_yz(-l,-m,-n,SKparam["flipsite"])
   def Eyz_z(self,l,m,n,SKparam):
      return self.Ez_yz(-l,-m,-n,SKparam["flipsite"])
   def Eyz_xy(self,l,m,n,SKparam):
      return self.Exy_yz(-l,-m,-n,SKparam["flipsite"])
   def Eyz_yz(self,l,m,n,SKparam):
      pass #TODO
   def Eyz_xz(self,l,m,n,SKparam):
      pass #TODO
   def Eyz_x2y2(self,l,m,n,SKparam):
      pass #TODO
   def Eyz_3z2r2(self,l,m,n,SKparam):
      pass #TODO

   ### Exz_*
   def Exz_s(self,l,m,n,SKparam):
      return self.Es_xz(-l,-m,-n,SKparam["flipsite"])
   def Exz_x(self,l,m,n,SKparam):
      return self.Ex_xz(-l,-m,-n,SKparam["flipsite"])
   def Exz_y(self,l,m,n,SKparam):
      return self.Ey_xz(-l,-m,-n,SKparam["flipsite"])
   def Exz_z(self,l,m,n,SKparam):
      return self.Ez_xz(-l,-m,-n,SKparam["flipsite"])
   def Exz_xy(self,l,m,n,SKparam):
      return self.Exy_xz(-l,-m,-n,SKparam["flipsite"])
   def Exz_yz(self,l,m,n,SKparam):
      return self.Eyz_xz(-l,-m,-n,SKparam["flipsite"])
   def Exz_xz(self,l,m,n,SKparam):
      pass #TODO
   def Exz_x2y2(self,l,m,n,SKparam):
      pass #TODO
   def Exz_3z2r2(self,l,m,n,SKparam):
      pass #TODO

   ### Ex2y2_*
   def Ex2y2_s(self,l,m,n,SKparam):
      return self.Es_x2y2(-l,-m,-n,SKparam["flipsite"])
   def Ex2y2_x(self,l,m,n,SKparam):
      return self.Ex_x2y2(-l,-m,-n,SKparam["flipsite"])
   def Ex2y2_y(self,l,m,n,SKparam):
      return self.Ey_x2y2(-l,-m,-n,SKparam["flipsite"])
   def Ex2y2_z(self,l,m,n,SKparam):
      return self.Ez_x2y2(-l,-m,-n,SKparam["flipsite"])
   def Ex2y2_xy(self,l,m,n,SKparam):
      return self.Exy_x2y2(-l,-m,-n,SKparam["flipsite"])
   def Ex2y2_yz(self,l,m,n,SKparam):
      return self.Eyz_x2y2(-l,-m,-n,SKparam["flipsite"])
   def Ex2y2_xz(self,l,m,n,SKparam):
      return self.Exz_x2y2(-l,-m,-n,SKparam["flipsite"])
   def Ex2y2_x2y2(self,l,m,n,SKparam):
      pass #TODO
   def Ex2y2_3z2r2(self,l,m,n,SKparam):
      pass #TODO

   ### E3z2r2_*
   def E3z2r2_s(self,l,m,n,SKparam):
      return self.Es_3z2r2(-l,-m,-n,SKparam["flipsite"])
   def E3z2r2_x(self,l,m,n,SKparam):
      return self.Ex_3z2r2(-l,-m,-n,SKparam["flipsite"])
   def E3z2r2_y(self,l,m,n,SKparam):
      return self.Ey_3z2r2(-l,-m,-n,SKparam["flipsite"])
   def E3z2r2_z(self,l,m,n,SKparam):
      return self.Ez_3z2r2(-l,-m,-n,SKparam["flipsite"])
   def E3z2r2_xy(self,l,m,n,SKparam):
      return self.Exy_3z2r2(-l,-m,-n,SKparam["flipsite"])
   def E3z2r2_yz(self,l,m,n,SKparam):
      return self.Eyz_3z2r2(-l,-m,-n,SKparam["flipsite"])
   def E3z2r2_xz(self,l,m,n,SKparam):
      return self.Exz_3z2r2(-l,-m,-n,SKparam["flipsite"])
   def E3z2r2_x2y2(self,l,m,n,SKparam):
      return self.Ex2y2_3z2r2(-l,-m,-n,SKparam["flipsite"])
   def E3z2r2_3z2r2(self,l,m,n,SKparam):
      pass #TODO



