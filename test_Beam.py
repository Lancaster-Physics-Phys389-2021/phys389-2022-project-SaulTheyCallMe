import ParticleGenerator
import random
import pytest

ParticleGen1 = ParticleGenerator.BeamGenerator(2, 4, 24)
Beam24 = ParticleGen1.Generate()
ParticleGen2 = ParticleGenerator.BeamGenerator(2, 4, 1.6)
Beam1_6 = ParticleGen2.Generate()
ParticleGen3 = ParticleGenerator.BeamGenerator(2, 4, 40)
Beam40 = ParticleGen3.Generate()


def test_Beam1():
    BM = random.randint(0, len(Beam24))
    assert Beam24[BM].velocity[0] == pytest.approx(3.400e7, 2e5)

def test_Beam2():
    for X in range(0, len(Beam40)):
        assert Beam40[X].velocity[0] < 3e8
        assert Beam1_6[X].velocity[0] < 3e8

def test_Beam3():
    for Y in range(0, len(Beam24)):
        assert -3e-7 < Beam24[Y].position[1] < 3e-7
        assert -3e-7 < Beam24[Y].position[2] < 3e-7