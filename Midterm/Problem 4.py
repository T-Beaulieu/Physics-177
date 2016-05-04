import numpy as np 
import matplotlib.pyplot as plt

q       = -1
k       = 9 * (10 ** 9) 
xLength = 100
yLength = 100 
xInt    = xLength / 2
yInt    = yLength / 2
x2      = 0.
y2      = 0. 
dx      = 1.
i       = 0
j       = 0
r       = 0.
image   = np.zeros((100,100))


def func(r):
    return k * q / r
    
for i in range(xLength):
    x2 = i * dx
    for j in range(yLength):
        y2 = j * dx
        r = np.sqrt(((xInt - x2) ** 2) + ((yInt - y2)) ** 2)
        image[j,i] = func(r) + (1.0 ** -10)
     

plt.clf()
plt.imshow(image)
plt.savefig("problem4.png")
       