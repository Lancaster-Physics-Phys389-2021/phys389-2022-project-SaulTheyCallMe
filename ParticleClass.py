import numpy as np
import math
import copy
import scipy.constants

class particle:
    """
    Class to model a massive particle in a gravitational field. 
    It will make use of numpy arrays to store the position velocity etc. 
    Working directly from past exercises... 

    mass in kg 
    position and velocity in m 
    """

    #G=6.67408E-11
    G=scipy.constants.G
    #e=1.60217662E-19 
    e=scipy.constants.elementary_charge
    #epsilon=8.854187E-12
    epsilon=scipy.constants.epsilon_0
    #amu in kg
    amu=1.66e-27

    def __init__(self, Position=np.array([0,0,0], dtype=float), Velocity=np.array([0,0,0], dtype=float), Acceleration=np.array([0,0,0], dtype=float), Name='Ball', Mass=1.0*amu, Znumber = 2.0, Energy = 1.6):
        self.Name = Name
        self.position = np.array(Position,dtype=float)
        self.velocity = np.array(Velocity,dtype=float)
        self.acceleration = np.array(Acceleration,dtype=float)
        self.mass = Mass
        self.znumber = Znumber
        self.energy = Energy

    def __repr__(self):
        return 'Particle: {0}, Mass: {1:12.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}, Atomic Number: {5}, Energy: {6}'.format(self.Name,self.mass,self.position, self.velocity,self.acceleration,self.znumber,self.energy)

    def KineticEnergy(self):
        return 0.5*self.mass*np.vdot(self.velocity,self.velocity)
  
    def momentum(self):
        return self.mass*np.array(self.velocity,dtype=float)

    def update(self, deltaT):
        self.position +=  self.velocity*deltaT
        self.velocity +=  self.acceleration*deltaT

 