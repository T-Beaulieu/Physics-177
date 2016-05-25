import numpy as np 
import matplotlib.pyplot as plt

N = 1000
xArray = np.linspace(0,1,1000)
yArray = []
length = []


def ModWave(xArray):
    for i in range(len(xArray)):
        var = np.sin(np.pi * i / float(N)) * np.sin(20. * np.pi * i / float(N))
        yArray.append(var)
    return yArray


def FourierTrans(yArray):
    N = 1000
    c = np.zeros(N//2 + 1,complex)
    for k in range(N//2 + 1):
        for n in range(N):
            c[k] += yArray[n] * np.exp(-2j*np.pi*k*n/N)
        length.append(k)
        c[k] = np.abs(c[k])
    return c,length


yArray = ModWave(xArray)

c_k,length = FourierTrans(yArray)

plt.clf()
plt.subplot(2,1,1)
plt.xlim([0,100])
plt.plot(length,c_k)

plt.subplot(2,1,2)
plt.plot(xArray,yArray)