import numpy as np

atoms = ["Mo","S_u","S_d"]
orbitals = ["s",
            "s_",
            "x" ,"y" ,"z" ,
            "x_","y_","z_",
            "xy" ,"yz" ,"xz" ,"x2y2" ,"3z2r2",
            "xy_","yz_","xz_","x2y2_","3z2r2_" ]
atom_num = len(atoms)
orbital_num = len(orbitals)
H_dim = atom_num * orbital_num

H = np.zeros((H_dim,H_dim),dtype="complex")
print H_dim, H

def get_index(atom,orbital):
   atom_idx = atoms.index(atom)
   orbital_idx = orbitals.index(orbital)
   return atom_idx * orbital_num + orbital_idx
