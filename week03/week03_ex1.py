import numpy as np 
import matplotlib.pylab as plt

pi           = 3.141592
epsilon_0    = 8.854187817   
q1           = 1             
q2           = -1            
size         = 100          
seperation   = 10            
numPix       = 100
dx           = size / float(numPix)
image        = np.zeros(shape = (numPix,numPix)).astype('float')
electicField = []
i            = 0 
j            = 0

##Initial points of charge 1 and charge 2 
x1 = size / 2 - seperation / 2
y1 = size / 2 
x2 = size / 2 + seperation / 2
y2 = size / 2 


##Assuming youre measuring potential of positive charge of 1 C
def phi(r,q):
    return (q / (4  * pi * epsilon_0 * r)) 
    
for j in range(numPix):
    y = j * dx
    for i in range(numPix):
        x = i * dx
        r1 = np.sqrt((x-x1)**2 + (y-y1)**2)
        r2 = np.sqrt((x-x2)**2 + (y-y2)**2)
        phi1 = phi(r1,q1)
        phi2 = phi(r2,q2)
        image[j,i] = (phi1 + phi2) 

##Plots electric potential
plt.subplot(2,1,1)        
plt.imshow(image,origin='lower',extent=([0,size,0,size]))
plt.gray()

##Calculates the gradient, returns an x array, y array 
electricField = np.gradient(image)

##Plots the electric field
plt.subplot(2,1,2)
image2 = np.sqrt((electricField[0] ** 2) + (electricField[1] ** 2))
plt.imshow(image2,origin='lower',extent=([0,size,0,size]))
plt.gray()        
