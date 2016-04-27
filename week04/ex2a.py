import numpy as np 
import matplotlib.pyplot as plt


def p(x): 
    return 924*(x ** 6) -  2772*(x ** 5) + 3150*(x ** 4) - 1680*(x ** 3) + 420*(x ** 2) - 42 * x + 1 

xArray = np.linspace(0,1,150)
yArray = p(xArray)

plot = plt.plot(xArray,yArray)
plt.show()

plt.savefig("roots.png")