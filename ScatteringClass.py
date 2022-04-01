from numpy import load
from numpy import save
import Angle
import geopandas as gpd
from shapely.geometry import Point
import ParticleGenerator
import TwoBodyAngle

class Scattering:

  La1 = load("Lattice.npy", allow_pickle=True)

  def __init__(self, Ene=1.6):
    self.energy = Ene

  def Rutherford(self):
    BeamPart = ParticleGenerator.BeamGenerator(AtomicNumber=2, ParticleMass=4, Energy=self.energy)
    BM1 = BeamPart.Generate()
    BeamPoints = []
    for B in range(0, len(BM1)):
      BeamPoints.append({
        'geometry' : Point(BM1[B].position[0], BM1[B].position[1], BM1[B].position[2]),
        'id': B
        })
    BH1 = gpd.GeoDataFrame(BeamPoints)

    LatticePoints = []

    for p in range(0, len(self.La1)):
       LatticePoints.append({
        'geometry' : Point(self.La1[p].position[0], self.La1[p].position[1], self.La1[p].position[2]),
        'id': p
      })
    LH1 = gpd.GeoDataFrame(LatticePoints)
 
    Angles = Angle.AngleCalculation(self.La1, LH1, BM1, BH1)
    AnglesAr = Angles.AngleArray()
    return AnglesAr

  def TwoBody(self):
    BeamPart2 = ParticleGenerator.BeamGenerator(AtomicNumber=2, ParticleMass=4, Energy=self.energy)
    BM2 = BeamPart2.Generate()
    BeamPoints2 = []
    for C in range(0, len(BM2)):
      BeamPoints2.append({
        'geometry' : Point(BM2[C].position[0], BM2[C].position[1], BM2[C].position[2]),
        'id': C
        })
    BH2 = gpd.GeoDataFrame(BeamPoints2)

    LatticePoints2 = []

    for K in range(0, len(self.La1)):
       LatticePoints2.append({
        'geometry' : Point(self.La1[K].position[0], self.La1[K].position[1], self.La1[K].position[2]),
        'id': K
      })
    LH2 = gpd.GeoDataFrame(LatticePoints2)
 
    Angles2 = TwoBodyAngle.TwoBodyCalculation(self.La1, LH2, BM2, BH2)
    AnglesAr2 = Angles2.TwoAngle()
    return AnglesAr2
