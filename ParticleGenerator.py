import ParticleClass
import numpy as np
import random

class BeamGenerator:

    #Mass multiplyer
    Amu = 1.66e-27

    def __init__(self, AtomicNumber=2, ParticleMass=4, Energy=4.5):
        self.atomicnumber = AtomicNumber
        self.particlemass = ParticleMass
        self.energy = Energy

    def __repr__(self):
        return 'Mass: {1}, Energy: {2}, AtomicNumber: {0}'.format(self.particlemass,self.energy,self.atomicnumber)


    def Generate(self):
        GeneratedParticle = []
        for x in range(1, 20000):
            Ycoord = random.uniform(-3e-13, 3e-13)
            Zcoord = random.uniform(-3e-13, 3e-13)
            ParticleBeam = ParticleClass.particle(np.array([0.0, Ycoord , Zcoord], dtype=float), np.array([0,0,0 ], dtype=float), np.array([0,0,0], dtype=float), Name='Alpha', Mass=self.particlemass*self.Amu, Znumber=self.atomicnumber, Energy=self.energy)
            Xvelocity = ((2*self.energy*1.602184e-13/(ParticleBeam.mass))**(1/2))
            ParticleBeam.velocity= np.array([Xvelocity,0.0,0.0], dtype=float)
            GeneratedParticle.append(ParticleBeam)
        return GeneratedParticle

        

