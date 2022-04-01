import ParticleClass
import numpy as np
import math

class LatticeGenerator:
    
    #Mass multiplyer
    Amu = 1.66e-27

    def __init__(self, AtomicNumber=79, Name="Gold", Mass = 196.7, image_shape=(5e-12,5e-12)):
        self.atomicnumber = AtomicNumber
        self.Atom = Name
        self.mass = Mass
        self.shape = image_shape

    def generate_lattice(self):
        A=self.atomicnumber
        R0 = 1.25e-15
        R = R0*A**(1/3)
        X=2*R/math.sin(45*math.pi/180)
        lattice_vectors = [
            np.array([-2*X, 0]),
            np.array([ X, -X])]
        center_pix = np.array(self.shape) // 2
        # Get the lower limit on the cell size.
        dx_cell = max(abs(lattice_vectors[0][0]), abs(lattice_vectors[1][0]))
        dy_cell = max(abs(lattice_vectors[0][1]), abs(lattice_vectors[1][1]))
        # Get an over estimate of how many cells across and up.
        nx = self.shape[0]//dx_cell
        ny = self.shape[1]//dy_cell
        # Generate a square lattice, with too many points.
        # Here I generate a factor of 4 more points than I need, which ensures 
        # coverage for highly sheared lattices.  If your lattice is not highly
        # sheared, than you can generate fewer points.
        x_sq = np.arange(-nx, nx, dtype=float)
        y_sq = np.arange(-ny, nx, dtype=float)
        x_sq.shape = x_sq.shape + (1,)
        y_sq.shape = (1,) + y_sq.shape
        # Now shear the whole thing using the lattice vectors
        x_lattice = lattice_vectors[0][0]*x_sq + lattice_vectors[1][0]*y_sq
        y_lattice = lattice_vectors[0][1]*x_sq + lattice_vectors[1][1]*y_sq
        # Trim to fit in box.
        mask = ((x_lattice < self.shape[0]/2.0)
            & (x_lattice > -self.shape[0]/2.0))
        mask = mask & ((y_lattice < self.shape[1]/2.0)
                    & (y_lattice > -self.shape[1]/2.0))
        x_lattice = x_lattice[mask]
        y_lattice = y_lattice[mask]
        # Translate to the centre pix.
        x_lattice += center_pix[0]
        y_lattice += center_pix[1]
        # Make output compatible with original version.
        out = np.empty((len(x_lattice), 2), dtype=float)
        out[:, 0] = y_lattice
        out[:, 1] = x_lattice
        LatticePar = []
        for p in out:
            LatticeParticle = ParticleClass.particle(Position=np.array([0.2,p[1],p[0]], dtype=float), Velocity=np.array([0,0,0], dtype=float), Acceleration=np.array([0,0,0], dtype=float), Name=self.Atom, Mass=self.mass*self.Amu, Znumber = self.atomicnumber, Energy = 1.6)
            LatticePar.append(LatticeParticle)
        return LatticePar
       