import numpy as np 
import matplotlib.pyplot as plt
import scipy

def f(x):
    return x ** 2 - 4 * x * np.sin(x) + (2 * np.sin(x))  ** 2
    
xArray = np.linspace(0,3,150)
yArray = f(xArray)
plot = plt.plot(xArray,yArray)
plt.show()

plt.savefig("roots2.png")

initialGuessX1 = [0.1,2.5]
initialGuessX2 = [0.2,2]
root = [0,0]
i = 0


for i in range(2):
    x1 = initialGuessX1[i]
    x2 = initialGuessX2[i]
    error = 1
    while error > 10 ** -8:
        x3 = x2 - (f(x2)/(f(x2) - f(x1))) * (x2 - x1)
        x1 = x2 
        x2 = x3 
        error = np.abs(x1 - x2)
        
    root[i] = x2
    
    
theirRoot1 = scipy.optimize.fsolve(f,0.5)
theirRoot2 = scipy.optimize.fsolve(f,3)
print "These are the roots my function found: ", root[0], "and", root[1]
print "These are the roots scipy found: ", theirRoot1[0], "and", theirRoot2[0]

