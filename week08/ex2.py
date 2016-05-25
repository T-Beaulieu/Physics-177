import numpy as np 
import matplotlib.pyplot as plt 
from numpy.fft import rfft,irfft

data = np.loadtxt('sunspots.txt')
length = []
c_k    = []
c_k2   = []

month = data[:,0]
spots = data[:,1]

plt.clf()
plt.figure(1)
plt.plot(month,spots)

period = 500. / 4.      ##Every 500 months, there are about 4 cycles 
print "One cycle of the sunspots is about ", period, " months."

c_k2 = rfft(spots)
length2 = len(c_k2)

c_k2 = np.abs(c_k2) ** 2

plt.figure(2)
plt.xlim([0,100])
plt.ylim([0,8.7 ** 10])
plt.plot(np.arange(length2),c_k2)

k_peak = 25         ##Got this by looking at the graph

print "The period of a sin wave with a k of 25 is ", 3142./k_peak, "months."