import math
import scipy.constants
import random

class AngleCalculation:
    """
    Class to calculate the scattering angles using Rutherford model.
    It will make use random function to generate the impact parameter and apply to
    calculate the scattering angle at a known energy.
    
    distances are in m.
    Angles are in degrees.
    """
    
    #e=1.60217662E-19 
    e=scipy.constants.elementary_charge
    #epsilon=8.854187E-12
    epsilon=scipy.constants.epsilon_0

    def __init__(self,LatticeParticles, ZnumberLat=79, ZnumberBe=2, Energy = 1.6):
        self.lattice = LatticeParticles
        self.ZL = ZnumberLat
        self.ZB = ZnumberBe
        self.Ener = Energy
    
    def AngleArray(self): 
        AngleArray = []
        # Calculating the maximum approach
        D=(self.ZL*self.ZB*197.3)/(137*self.Ener)*1e-15
        for x in range(0,700000):
            #Generating a random impact parameter.   
            B = random.randint(0,100000)*D*1e-5
            #Calculating scattering angle and saving it in an array.
            if B == 0:
                Angle = 180
            else:
                Angle = 360*math.atan(D/(2*B))/math.pi
                AngleArray.append(Angle)
        return  AngleArray

