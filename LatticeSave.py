import numpy as np
import ParticleWall

Lattice = ParticleWall.LatticeGenerato().generate_lattice()
np.save("Lattice.npy", Lattice)