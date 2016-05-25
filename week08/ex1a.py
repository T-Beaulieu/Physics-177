import numpy as np 
import matplotlib.pyplot as plt
from scipy import signal

##Interval from -1, 1 
N = 1000
xArray = []
yArray = []
length = []

def SquareWave():
    xArray = np.linspace(0,2 * np.pi,1000)
    yArray = signal.square(xArray)
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

xArray,yArray = SquareWave()
c_k,length = FourierTrans(yArray)

plt.clf()
plt.subplot(2,1,1)
plt.xlim([0,100])
plt.plot(length,c_k)

plt.subplot(2,1,2)
plt.plot(xArray,yArray)
plt.plot(0,-1.5)
plt.plot(0,1.5)