import ParticleClass
import numpy as np

class LatticeGenerato:
    """
    Class to model a 2D lattice of a set atomic radius a set distance away in the X direction.
    This lattice is 1 atom thick. 
    It will make use of numpy arrays to store positons of each individual atom and when
    transfer that data to the ParticleClass.

    mass in Amu 
    distances in m
    """
    
    #Mass multiplyer
    Amu = 1.66e-27

    def __init__(self, AtomicNumber=79, Name="Gold", Mass = 196.7, AtomicRadius = 0.146e-9, image_shape=(5e-7,5e-7), DistancefromBeam = 0.2):
        self.atomicnumber = AtomicNumber
        self.Atom = Name
        self.mass = Mass
        self.shape = image_shape
        self.radius = AtomicRadius
        self.distance = DistancefromBeam

    def generate_lattice(self):
        # Getting the diagonal distance between two atoms
        X=self.radius/(2**(1/2))
        #Formatting the position of the lattices, the first array shows movement in the z axis, while the second in the y axis.
        lattice_vect = [
            np.array([-2*X, 0]),
            np.array([ X, -X])]
        center_pix = np.array(self.shape) // 2
        # Get the lower limit on the cell size.
        dxcell = max(abs(lattice_vect[0][0]), abs(lattice_vect[1][0]))
        dycell = max(abs(lattice_vect[0][1]), abs(lattice_vect[1][1]))
        # An estimate on the number of cells
        Nx = self.shape[0]//dxcell
        Ny = self.shape[1]//dycell
        # Generate a square lattice.
        x_sq = np.arange(-Nx, Nx, dtype=float)
        y_sq = np.arange(-Ny, Nx, dtype=float)
        x_sq.shape = x_sq.shape + (1,)
        y_sq.shape = (1,) + y_sq.shape
        #Shearing down the lattice to fit in the assigned limits
        x_lat = lattice_vect[0][0]*x_sq + lattice_vect[1][0]*y_sq
        y_lat = lattice_vect[0][1]*x_sq + lattice_vect[1][1]*y_sq
        # Fill in the lattice inside a box
        mask = ((x_lat < self.shape[0]/2.0)
            & (x_lat > -self.shape[0]/2.0))
        mask = mask & ((y_lat < self.shape[1]/2.0)
                    & (y_lat > -self.shape[1]/2.0))
        x_lat = x_lat[mask]
        y_lat = y_lat[mask]
        # Translate to the nucleus of the atom
        x_lat += center_pix[0]
        y_lat += center_pix[1]
        # Make output compatible with original version.
        Positions = np.empty((len(x_lat), 2), dtype=float)
        Positions[:, 0] = y_lat
        Positions[:, 1] = x_lat
        LatticePar = []
        # Fill in the ParticleCalls array and return it for further use.
        for p in Positions:
            LatticeParticle = ParticleClass.particle(Position=np.array([self.distance,p[1],p[0]], dtype=float), Velocity=np.array([0,0,0], dtype=float), Acceleration=np.array([0,0,0], dtype=float), Name=self.Atom, Mass=self.mass*self.Amu, Znumber = self.atomicnumber, Energy = 1.6)
            LatticePar.append(LatticeParticle)
        return LatticePar
       