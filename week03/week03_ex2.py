import numpy.linalg as lin
import numpy as np

##PART A
'''
System of equations:
4V1 - V2 - V3 - V4 = 5V
V1 - 4V2 - V3 - V4 = 0
V1 - V2 - 4V3 - V4 = 5V
V1 - V2 - V3 - 4V4 = 0
'''

##PART B
##Array definitions
array = np.array([[4., -1., -1., -1.],
                  [-1., 4., -1., -1.],
                  [-1., -1., 4., -1.],
                  [-1., -1., -1., 4.]])
                  
knownVoltage = np.array([5., 0., 5., 0.])

##Variables
N   = len(knownVoltage)
i   = 0
j   = 0
v   = np.zeros(N)
v2  = np.zeros(N)

##Makes the diagonal value into 1
for j in range(N):
    var = array[j,j]
    array[j,:] = array[j,:] / var
    knownVoltage[j] = knownVoltage[j] / var
    
##Subtracts rows using linear row operations
    for i in range((j + 1), N):
        var = array[i,j]
        array[i,:] -= var * array[j,:]
        knownVoltage[i]   -= var * knownVoltage[j]

##Uses back substitution to solve for varialbes 
for j in range((N - 1),-1,-1):
    v[j] = knownVoltage[j]
    for i in range((j + 1),N):
        v[j] -= array[j,i] * v[i]
        
print "This is the solution Gaussian Elimination gave: ", (v)

##Part C
v2 = lin.solve(array,knownVoltage)
print "This is the solution that lin.solve gave: ", (v2)