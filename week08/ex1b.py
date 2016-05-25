import numpy as np 
import matplotlib.pyplot as plt

N = 1000
xArray = []
yArray = []
length = []

def SawWave():
    xArray = np.linspace(-1,1,N)
    for i in range(len(xArray)):
        if xArray[i] < 0:
            yArray.append(xArray[i] + 0.5)
        elif xArray[i] >= 0 & i < 1:
            yArray.append((xArray[i] - 0.5))    
    return xArray,yArray

def FourierTrans(yArray):
    N = 1000
    c = np.zeros(N//2 + 1,complex)
    for k in range(N//2 + 1):
        for n in range(N):
            c[k] += yArray[n] * np.exp(-2j*np.pi*k*n/N)
        length.append(k)
        c[k] = np.abs(c[k])
    return c,length


xArray,yArray = SawWave()

c_k,length = FourierTrans(yArray)

plt.clf()
plt.subplot(2,1,1)
plt.xlim([0,100])
plt.plot(length,c_k)

plt.subplot(2,1,2)
plt.plot(xArray,yArray)

