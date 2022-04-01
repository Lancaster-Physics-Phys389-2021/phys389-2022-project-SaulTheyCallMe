import math
import NearestPoint
import numpy as np

class AngleCalculation:

    NearLattice = NearestPoint.NearPoint

    def __init__(self, LatticeParticles, LatticeHead, BeamParticles, BeamHead):
        self.lattice = LatticeParticles
        self.beam = BeamParticles
        self.LaH = LatticeHead
        self.BeH = BeamHead
    
    def AngleArray(self): 
        AngleArray = []
        ClosestPoint = self.NearLattice.ckdnearest(self.BeH, self.LaH)
        for x in range(0,len(self.beam)):
            p = int(ClosestPoint.iloc[x].id)
            B=(((self.beam[x].position[1]-self.lattice[p].position[1])**2+(self.beam[x].position[2]-self.lattice[p].position[2])**2)**(1/2))
            D=self.lattice[p].znumber*self.beam[x].znumber*self.beam[x].e**2/(4*self.beam[x].epsilon*math.pi*self.beam[x].energy*1.602e-13)
            TanValue = D/(2*B)
            Angle =2*180*math.atan(TanValue)/math.pi
            AngleArray.append(Angle)
        return AngleArray

