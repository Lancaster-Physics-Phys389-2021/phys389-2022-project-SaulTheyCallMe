import pytest
import numpy as np
import ParticleWall

Lattice = ParticleWall.LatticeGenerato(AtomicNumber=79, Name="Gold", Mass = 196.7, AtomicRadius = 0.146e-9, image_shape=(5e-7,5e-7), DistancefromBeam = 0.2).generate_lattice()
np.save("Lattice.npy", Lattice)
def test_lattice1():
    for Y in range(0, len(Lattice)):
        assert -2.5e-7 < Lattice[Y].position[1] < 2.5e-7
        assert -2.5e-7 < Lattice[Y].position[2] < 2.5e-7
def test_lattice2():
    X= ((Lattice[0].position[1]-Lattice[2].position[1])**2+(Lattice[3].position[2]-Lattice[3].position[2])**2)**(1/2)
    print(X)
    assert X == pytest.approx(2*0.146e-9)
    
    