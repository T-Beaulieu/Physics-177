import numpy as np
import matplotlib.pyplot as plt 

def func(x):
    return ((-3 * (x ** 5)) - (24 * (x ** 4)) + (3 * x) + 10)

def funcPrime(x):
    return ((-15 * (x ** 4)) - (96 * (x ** 3)) + 3)

    
xArray   = np.linspace(0,1,20)
yArray   = func(xArray)
accuracy = 10 ** (-10)
guess    = 0.7
x1       = 0.                 
x2       = 0.
numSteps = 0

plt.clf()
plt.plot(xArray,yArray)

##Allows the loop to run once
x2 = guess

while abs(x2 - x1) > accuracy:
    x1 = x2
    x2 = x1 - (func(x1)/funcPrime(x1))
    numSteps += 1
    
print "The answer is:", x2
print "The number of steps was:", numSteps