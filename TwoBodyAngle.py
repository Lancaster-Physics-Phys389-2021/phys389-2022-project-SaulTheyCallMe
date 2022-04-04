import math
import NearestPoint
import numpy as np
import scipy.constants

class TwoBodyAngle:
    """
    Class to calculate the scattering angles using Two Body scattering model.
    It will make use NearestPoint function and the 3d movement of beam and lattice particles
    using particle class to calculate the scattering angle.
    
    distances are in m.
    Angles are in degrees.
    """
    
    
    #e=1.60217662E-19 
    e=scipy.constants.elementary_charge
    #epsilon=8.854187E-12
    epsilon=scipy.constants.epsilon_0
    NearLattice = NearestPoint.NearPoint

    def __init__(self, LatticeParticles, BeamParticles, ZnumberLat=79, ZnumberBe=2, Energy = 1.6):
        self.lattice = LatticeParticles
        self.beam = BeamParticles
        self.ZL = ZnumberLat
        self.ZB = ZnumberBe
        self.Ener = Energy
    
    def AngleArrayTwoBody(self): 
        AngleArray = []
        ClosestPoint = self.NearLattice.ckdnearest(self.beam)
        D=(self.ZL*self.ZB*197.3)/(137*self.Ener)*1e-15
        Difference = []
        Force2 = []
        for x in range(0,700000):
            p = int(ClosestPoint.iloc[x].id)
            InMomentum = self.beam[x].momentum()
            self.lattice[p].position[0] = 0.2
            #B=(((self.beam[x].position[1]-self.lattice[x].position[1])**2+(self.beam[x].position[2]-self.lattice[x].position[2])**2)**(1/2))     
            for y in range(0,30):
                Difference = np.array([(self.beam[x].position[0] - self.lattice[p].position[0]),(self.beam[x].position[1] - self.lattice[p].position[1]),(self.beam[x].position[2] - self.lattice[p].position[2])],dtype=float)
                Dif = (Difference[0]**2+Difference[1]**2+Difference[2]**2)**(1/2)*D
                Force2 = np.array([(D*Difference[0]*self.Ener)/(Dif**3),D*(Difference[1])/(Dif**3),(D*Difference[2])/(Dif**3)], dtype = float)
                self.beam[x].acceleration=Force2/(self.beam[x].mass)
                self.lattice[p].acceleration = -Force2/(self.lattice[p].mass)
                self.beam[x].update(1e-8)
                self.lattice[p].update(1e-8)
            FinMomentumBeam = self.beam[x].momentum()
            FinMomentumLattice = self.lattice[p].momentum()
            MomentumCz= (self.lattice[p].mass*InMomentum[0])/(self.lattice[p].mass+self.beam[x].mass)-FinMomentumLattice[2]
            TanValue = FinMomentumBeam[0]/MomentumCz
            TV = FinMomentumBeam[0]/FinMomentumBeam[2]
            Angle =180*math.atan(TV)/math.pi
            if Angle <0:
                Angle =-1*Angle
                AngleArray.append(Angle)
            else:
                AngleArray.append(Angle)           
        return  AngleArray

