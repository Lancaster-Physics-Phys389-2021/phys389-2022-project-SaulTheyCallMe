from numpy import load
import Angle
import ParticleGenerator
import TwoBodyAngle

class Scattering:
  """
  Class to store different analyzis methods: Rutherford and TwoBody scattering
  It will make use of the classes created previously and the np.load feature.
  The results are an array of angles.

  mass in Amu 
  distances in m
  Energy in MeV
  """
  La1 = load("Lattice.npy",allow_pickle=True)
  La2 = load("LatticeTwoBody.npy", allow_pickle=True)

  def __init__(self,AtomNumber=2,Mass =4,Ene=1.6):
    self.energy = Ene
    self.mass = Mass
    self.Anum = AtomNumber
    
  def Rutherford(self):
    #Generating an array of beam particles at a set energy
    BeamPart = ParticleGenerator.BeamGenerator(AtomicNumber=self.Anum, ParticleMass=self.mass, Energy=self.energy)
    BM1 = BeamPart.Generate()
    #Generate the scattering angles using Rutherford model. 
    Angles = Angle.AngleCalculation(self.La1, self.La1[0].znumber, BeamPart.atomicnumber, self.energy)
    AnglesAr = Angles.AngleArray()
    return AnglesAr

  def TwoBody(self):
    #Generating an array of beam particles at a set energy
    BeamPart2 = ParticleGenerator.BeamGenerator(AtomicNumber=2, ParticleMass=self.mass, Energy=self.energy)
    BM2 = BeamPart2.Generate()
    #Generating 
    Angles2 = TwoBodyAngle.TwoBodyAngle(self.La2, BM2,79, 2, 1.6)
    AnglesAr2 = Angles2.AngleArrayTwoBody()
    return AnglesAr2
