import numpy as np
from SK2E import SK2E

atoms = ["Mo","S_u","S_d"]
orbitals = ["s",
            "s_",
            "x" ,"y" ,"z" ,
            "x_","y_","z_",
            "xy" ,"yz" ,"xz" ,"x2y2" ,"3z2r2",
            "xy_","yz_","xz_","x2y2_","3z2r2_" ]
sk2e = SK2E()

SO_terms =[
   ["x" ,"x_",-1j],
   ["x" ,"z_",1],
   ["x_","z_",1],
   ["y" ,"y_",-1],
   ["y" ,"z" ,1j],
   ["y_","z" ,1j],
]

atom_num    = len(atoms)
orbital_num = len(orbitals)
H_dim = atom_num * orbital_num

def get_index(atom,orbital):
   atom_idx    = atoms.index(atom)
   orbital_idx = orbitals.index(orbital)
   return atom_idx * orbital_num + orbital_idx

###################################################################
######    Class TBblock: building blocks for TB Hamiltonian 
## Each instantiation represents interactions from one unit cell 
## to another. After object initiazed, define atomic interactions by 
## calling fill_SK. Finally, call get_block to get the Bloch-
## phase-modulated building block.
###################################################################
class TBblock:
   def __init__(self,d):
      ## d: translation vector from the refernece cell to 
      ##    the represented cell
      self.H = np.matrix(np.zeros((H_dim,H_dim),dtype="complex"))
      self.d = d

   def fill_SK(self, atom_r, atom_c, lmn, skparam):
      ### fill all the two-center integrals corresponding to 
      ###  the atomic interactions between atom_r and atom_c
      ## atom_r: atom in the reference cell
      ## atom_c: atom in the represented cell
      ## l,m,n: direction cosines of atom_r->atom_c vector
      norm_lmn = np.linalg.norm(lmn)
      l = lmn[0]
      m = lmn[1]
      n = lmn[2]
      assert(np.isclose(norm_lmn,1))
      for orb_r in orbitals :
         r_idx = get_index(atom_r,orb_r)
         for orb_c in orbitals :
            c_idx = get_index(atom_c,orb_c)
            self.H[r_idx,c_idx] = sk2e.calc_E(l,m,n,orb_r,orb_c,skparam)

   ### Onsite Energy filling for  
   ### for reference cell only (d=0)
   def fill_Onsite(self,atom,osparam):
      assert(np.linalg.norm(self.d)==0)
      ## Fill out the on site diagonal
      for orb in orbitals:
         idx = get_index(atom,orb)
         ## treating spin up and down indifferently
         ## so remove "_" in orbital name
         self.H[idx,idx] = osparam[orb.replace("_","")]

      ## spin-orbit interactions
      lambda_SO = osparam["SO"] 
      for term in SO_terms:
         idx0 = get_index(atom,term[0])
         idx1 = get_index(atom,term[1])
         self.H[idx0,idx1] = lambda_SO*term[2]
         ## make sure it is hermitian
         self.H[idx1,idx0] = lambda_SO*np.conj(term[2])

   def get_block(k):
      ## k: wavevector specified for band structure calculation
      phase = np.dot(self.d,k)
      return self.H * np.exp(1j*phase)
