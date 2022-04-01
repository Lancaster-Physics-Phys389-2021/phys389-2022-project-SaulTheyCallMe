import ParticleClass
import ParticleGenerator
import ParticleWall
import Angle
import NearestPoint
import random

ParticleGen = ParticleGenerator.BeamGenerator(2, 4, 8)
Beam = ParticleGen.Generate()

def test_Beam1():
    BM = random.randint(0, len(Beam))
    assert Beam[BM] == 1.964e8
