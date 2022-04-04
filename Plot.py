import numpy as np
import matplotlib.pyplot as plt
import math

A1_6 = np.load("RutherfordData(1_6MeV).npy", allow_pickle=True)
A3_2 = np.load("RutherfordData(3_2MeV).npy", allow_pickle=True)
A4_8 = np.load("RutherfordData(4_8MeV).npy", allow_pickle=True)
A6_4 = np.load("RutherfordData(6_4MeV).npy", allow_pickle=True)
A8_0 = np.load("RutherfordData(8_0MeV).npy", allow_pickle=True)
A9_6 = np.load("RutherfordData(9_6MeV).npy", allow_pickle=True)
A11_2 = np.load("RutherfordData(11_2MeV).npy", allow_pickle=True)
A12_8 = np.load("RutherfordData(12_8MeV).npy", allow_pickle=True)
A14_4 = np.load("RutherfordData(14_4MeV).npy", allow_pickle=True)
A16_0 = np.load("RutherfordData(16_0MeV).npy", allow_pickle=True)
A17_6 = np.load("RutherfordData(17_6MeV).npy", allow_pickle=True)
A19_2 = np.load("RutherfordData(19_2MeV).npy", allow_pickle=True)
A20_8 = np.load("RutherfordData(20_8MeV).npy", allow_pickle=True)
A22_4 = np.load("RutherfordData(22_4MeV).npy", allow_pickle=True)
A24_0 = np.load("RutherfordData(24_0MeV).npy", allow_pickle=True)
A25_6 = np.load("RutherfordData(25_6MeV).npy", allow_pickle=True)
A27_2 = np.load("RutherfordData(27_2MeV).npy", allow_pickle=True)
A28_8 = np.load("RutherfordData(28_8MeV).npy", allow_pickle=True)
A30_4 = np.load("RutherfordData(30_4MeV).npy", allow_pickle=True)
A32_0 = np.load("RutherfordData(32_0MeV).npy", allow_pickle=True)
A33_6 = np.load("RutherfordData(33_6MeV).npy", allow_pickle=True)
A35_2 = np.load("RutherfordData(35_2MeV).npy", allow_pickle=True)
A36_8 = np.load("RutherfordData(36_8MeV).npy", allow_pickle=True)
A38_4 = np.load("RutherfordData(38_4MeV).npy", allow_pickle=True)
A40_0 = np.load("RutherfordData(40_0MeV).npy", allow_pickle=True)

x = []
Energy = 1.6
y = []
Value = 0
S = 0
Data =[A1_6 ,A3_2 ,A4_8 ,A6_4 ,A8_0 ,A9_6 ,A11_2 ,A12_8 ,A14_4 ,A16_0 ,A17_6 ,A19_2 ,A20_8 ,A22_4 ,A24_0, A25_6, A27_2 ,A28_8, A30_4 ,A32_0 ,A33_6 ,A35_2, A36_8, A38_4, A40_0]
for Amount in range(0,len(Data)):
    DAngle = Data[Amount]
    for A in range(0,len(DAngle)):
        EnergyArray = DAngle[A]
        if EnergyArray < 62.5 and EnergyArray > 57.5:
            D = math.pi*79**2*(8.9875517e9*(1.6e-19)**2/(Energy*1.6e-13))**2
            Value = 10e28*(D)/(1+math.cos(math.pi*EnergyArray)/(1-math.cos(math.pi*EnergyArray)))
            y.append(Value)
            x.append(Energy)
    Energy +=1.6
plt.plot(x, y, 'o', color='black')
DifCross19_2 = []
DifCross24 = []
print(A40_0)
for B in range(0, len(A19_2)):
    D19_2 = (197.3*2*79)/(137*19.2)
    Value40 = 10e-3*(D19_2**2)/(16*math.sin(math.pi*A19_2[B]/360)**4)
    DifCross19_2.append(Value40)
for C in range(0, len(A24_0)):
    D24 = (197.3*2*79)/(137*24)
    Value24 = 10e-3*(D24**2)/(16*math.sin(math.pi*A24_0[C]/360)**4)
    DifCross24.append(Value24)

plt.plot(A19_2, DifCross19_2, 'o', color='black')
plt.title('Number of alpha particles scattering around 60 degrees over energy')
plt.xlabel('Energy in MeV')
plt.ylabel('Number of alpha particles around 60 degrees')
plt.show()