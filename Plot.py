import numpy as np
from numpy import load
import matplotlib.pyplot as plt
import ParticleClass
import math

P = ParticleClass.particle()

A1_6 = np.load("EnergyArray(1.6MeV).npy", allow_pickle=True)
A3_2 = np.load("EnergyArray(3.2MeV).npy", allow_pickle=True)
A4_8= np.load("EnergyArray(4.8MeV).npy", allow_pickle=True)
A6_4 = np.load("EnergyArray(6.4MeV).npy", allow_pickle=True)
A8_0 = np.load("EnergyArray(8.0MeV).npy", allow_pickle=True)
A9_6 = np.load("EnergyArray(9.6MeV).npy", allow_pickle=True)
A11_2 = np.load("EnergyArray(11.2MeV).npy", allow_pickle=True)
A12_8 = np.load("EnergyArray(12.8MeV).npy", allow_pickle=True)
A14_4= np.load("EnergyArray(14.4MeV).npy", allow_pickle=True)
A16 = np.load("EnergyArray(16MeV).npy", allow_pickle=True)
A17_6 = np.load("EnergyArray(17.6MeV).npy", allow_pickle=True)
A19_2 = np.load("EnergyArray(19.2MeV).npy", allow_pickle=True)
A20_8 = np.load("EnergyArray(20.8MeV).npy", allow_pickle=True)
A22_4 = np.load("EnergyArray(22.4MeV).npy", allow_pickle=True)
A24 = np.load("EnergyArray(24MeV).npy", allow_pickle=True)
A25_6 = np.load("EnergyArray(25.6MeV).npy", allow_pickle=True)
A27_2 = np.load("EnergyArray(27.2MeV).npy", allow_pickle=True)
A28_8 = np.load("EnergyArray(28.8MeV).npy", allow_pickle=True)
A30_4 = np.load("EnergyArray(30.4MeV).npy", allow_pickle=True)
A32 = np.load("EnergyArray(32MeV).npy", allow_pickle=True)
A33_6= np.load("EnergyArray(33.6MeV).npy", allow_pickle=True)
A35_2 = np.load("EnergyArray(35.2MeV).npy", allow_pickle=True)
A36_8 = np.load("EnergyArray(36.8MeV).npy", allow_pickle=True)
A38_4 = np.load("EnergyArray(38.4MeV).npy", allow_pickle=True)
A40 = np.load("EnergyArray(40MeV).npy", allow_pickle=True)

x = []
Energy = 1.6
y = []
Value = 0
S = 0
Data =[A1_6 ,A3_2 ,A4_8 ,A6_4 ,A8_0 ,A9_6 ,A11_2 ,A12_8 ,A14_4 ,A16 ,A17_6 ,A19_2 ,A20_8 ,A22_4 ,A24, A25_6, A27_2 ,A28_8, A30_4 ,A32 ,A33_6 ,A35_2, A36_8, A38_4, A40]
#for Amount in range(0,len(Data)):
    #DAngle = Data[Amount]
    #for A in range(0,len(DAngle)):
        #EnergyArray = DAngle[A]
        #if EnergyArray < 62.5 and EnergyArray > 57.5:
            #D = math.pi*79**2*(8.9875517e9*(1.6e-19)**2/(Energy*1.6e-13))**2
            #Value = 10e28*(D)/(1+math.cos(math.pi*EnergyArray)/(1-math.cos(math.pi*EnergyArray)))
           #y.append(Value)
            #x.append(Energy)
    #Energy +=1.6
DifCross16 = []
DifCross24 = []

for A_16 in range(0, len(A40)):
    D16 = (197.3*2*79)/(137*40)
    Value16 = 10e-3*(D16**2)/(16*math.sin(math.pi*A40[A_16]/360)**4)
    DifCross16.append(Value16)
for A_24 in range(0, len(A24)):
    D24 = (197.3*2*79)/(137*24)
    Value24 = 10e-3*(D24**2)/(16*math.sin(math.pi*A24[A_24]/360)**4)
    DifCross24.append(Value24)

plt.plot(A40, DifCross16, 'o', color='black')
plt.plot(A24, DifCross24, 'o', color='green')
plt.show()