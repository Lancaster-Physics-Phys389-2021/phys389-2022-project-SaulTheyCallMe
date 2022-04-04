import ParticleClass
import numpy as np
import random

class BeamGenerator:
    """
    Class to model a big group of particles spread out over a certain distance travelling
    towards the lattice for scattering with a set energy value.
    It will make use of the random library to randomly generate particles in a box and store
    that data in the numpy arrays. 
    The final positions are stored in the ParticleClass array.

    mass in Amu 
    distances in m
    Energy in MeV
    """

    #Mass multiplyer
    Amu = 1.66e-27
    Lattice = np.load("Lattice.npy", allow_pickle=True)

    def __init__(self, AtomicNumber=2, ParticleMass=4, Energy=4.5):
        self.atomicnumber = AtomicNumber
        self.particlemass = ParticleMass
        self.energy = Energy

    def Generate(self):
        # Create and array to store data
        GeneratedParticle = []
        # Generating particles in the range equal to the number of lattice atoms
        # This is the maximum number of possible atoms as nearest point analysis will
        # be used and it can't be bigger 
        for x in range(0, 700000):
        # Range chosen to fill in the lattice 
            Ycoord = random.uniform(-2.5e-7, 2.5e-7)
            Zcoord = random.uniform(-2.5e-7, 2.5e-7)
        # Calculating the velocty in the X direction from energy.
            Xvelocity = ((2*self.energy*1.602184e-13/(self.particlemass*self.Amu))**(1/2))
        # Filling up the ParticleClass to store data.
            ParticleBeam = ParticleClass.particle(Position=np.array([0.0, Ycoord , Zcoord], dtype=float), Velocity=np.array([Xvelocity,0,0 ], dtype=float), Acceleration=np.array([0,0,0], dtype=float), Name='Alpha', Mass=self.particlemass*self.Amu, Znumber=self.atomicnumber, Energy=self.energy)
            GeneratedParticle.append(ParticleBeam)
        return GeneratedParticle

        

