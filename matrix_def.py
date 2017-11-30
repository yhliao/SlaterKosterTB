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
      self.H = np.zeros((H_dim,H_dim),dtype="complex")
      self.d = d

   def fill_SK(self, atom_r, atom_c, l,m,n, skparam):
      ### fill all the two-center integrals corresponding to 
      ###  the atomic interactions between atom_r and atom_c
      ## atom_r: atom in the reference cell
      ## atom_c: atom in the represented cell
      ## l,m,n: direction cosines of atom_r->atom_c vector
      for orb_r in orbitals :
         r_idx = get_index(atom_r,orb_r)
         for orb_c in orbitals :
            c_idx = get_index(atom_c,orb_c)
            H[r_idx,c_idx] = sk2e.calc_E(l,m,n,orb_r,orb_c,skparam)

   def get_block(k):
      ## k: wavevector specified for band structure calculation
      phase = np.dot(self.d,k)
      return self.H * np.exp(1j*phase)
