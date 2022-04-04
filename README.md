[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=7166805&assignment_repo_type=AssignmentRepo)
ParticleClass.py
  contains a class called particle
  When calling this classs you can fill in Position array, Velocity array, Acceleration array, Name of particle, Mass in Amu, Atomic number and Energy in MeVas
  particle(Position=np.array([0,0,0], dtype=float), Velocity=np.array([0,0,0], dtype=float), Acceleration=np.array([0,0,0], dtype=float), Name='Ball', Mass=1.0*amu, Znumber = 2.0, Energy = 1.6)
  This class contains a couple functions:
    .KineticEnergy() - returns kinetic energy of the particle
    .momentum() - returns momentum of the particle
    .update(deltaT) - changes position and velocity of the particle depending on the initial position, velocity and acceleration. Will change it over a time period of DeltaT which you insert into the function.   

ParticleGenerator.py:
  Contains a class called BeamGenerator
  When calling this class you can fill in Atomic number, Particle Mass in Amu and Energy in MeV as:  BeamGenerator(AtomicNumber=2, ParticleMass=4, Energy=4.5)
  The values in the brackets are set values. Atomic number of alpha particle is 2 and the mass is 4Amu.
  You can generate a total of 700000 alpha particles in the y-z coordinate box of a size -2.5e-7m to 2.5e-7m by calling function generate(). This function also calculates velocity in the x direction according to the energy.
  The data will be saved in a PartiClass array
  
ParticleWall.py
  contains a class called LatticeGenerato
  When calling this class you can fill in  Atomic Number, Name of the atom, Mass in Amu, AtomicRadius of the atom in m, image shape y and Z length and Distance from alpha particle Beam in m as LatticeGenerato(AtomicNumber=79, Name="Gold", Mass = 196.7, AtomicRadius = 0.146e-9, image_shape=(5e-7,5e-7), DistancefromBeam = 0.2)
  It contains a function called generate_lattice: Calling this will generate a 1 atom thick lattice in the set image shape of the described atom.
  You can call the generators as ParticleWall.LatticeGenerato().generate_lattice()
  
 LatticeSave.py
  Calling this file will create and save a lattice as "Lattice.npy" to be used in other files.
  
 Angle.py
  Contains a class called AngleCalculation
  When calling this class you can fill in an array of Lattice Particles, Atomic number of target particles, Atomic number of projectile particles and the Energy in MeV as: Angle.AngleCalculation(LatticeParticles, ZnumberLat=79, ZnumberBe=2, Energy = 1.6)
  This class contains 1 function that will generate an array of scatter angles using Rutherford Model. You can call this function calling AngleArray()
  Full example Angle.AngleCalculation().AngleArray()
  Returns a array of degrees.
  
  NearestPoint.py
  Contains a class called ckdnearest
  It only needs a particle beam array to be filled in as ckdnearest(ParticleBeam)
  Calling this function NearestPoint.ckdnearest(ParticleBeam) will generate a geopandas array of closest points between the lattice and beam particles.
    
 TwoBodyAngleClass.py
   Contains a class called TwoBodyAngle
   When calling this function you can fill in Lattice Particles array, Beam Particles arrays, Target atomic number, Beam particle atomic number and Energy in MeV as:
   TwoBodyAngleClass.TwoBodyAngle(LatticeParticles, BeamParticles, ZnumberLat=79, ZnumberBe=2, Energy = 1.6)
   This class contains 1 function which would calcualte the center of mass angle in the lab scattering using two body scattering module.
   it uses the NearParticle class to calculate the closest particles between the beam and lattice.
   It can be called as TwoBodyAngleClass.TwoBodyAngle().AngleArrayTwoBody()
    
  ScatterClass.py
   Contains a Class called Scatter
   When callin this class you can fill in Atomic number of projectile, mass of the projectile in Amu and energy in MeV as: ScatterClass.Scatter(AtomNumber=2,Mass   =4,Ene=1.6)
   This class contains two functions:
    Rutherford: Contains Angle class and generates the angles described in Angles.py section above. It summons an already saved lattice array.
    TwoBody: Cotnains a TwoBodyAngle.py which would generate Center of mass angles of scattering. It also generates the beam particles when summoning this function to put into TwoBodyAngle class.
    
   Savedata.py
    Run ScatterClass class for Rutherford scattering at energy range 1.6MeV to 40MeV and saves it as "RutherfordData($Energy$MeV$.npy"
    
   Plot.py 
    Plots some of Rutherford data, need to change the files around to plot the graphs you want.
    
   test_Beam
    Runs 3 test for ParticleGenerator:
      Checks if velocity dosen't exceed speed of light.
      Checks if velocity is accurately calculated.
      Checks if the data is contained in the set range of y-z box.
      
   test_Lattice
    Runs 2 tests on ParticleWall:
      Checks if the particles are contained in wanted limits
      Checks if the closest particles are indeed 2 atmoic radii apart
    
   test_nearpoints
    Runs 1 test on NearPoints:
      checks if the closest point analysis is accurate for 2 arrays of 3 points each. 
      
     
