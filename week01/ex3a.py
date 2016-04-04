import numpy as np 

height          = 800.0 
intVelocity     = 0.0
g               = -9.8   ##Gravity, a constont 
time            = 0.0

print 'Entering a positive number will give a downward initial velocity.'
print 'Entering a negative number will give an upward initial velocity.'
##I switch the signs after they are input so the calculation works out correctly

intVelocity = float(input('Enter initial velocity: '))
intVelocity = -intVelocity 
time = ((-intVelocity) - np.sqrt(intVelocity**2 - 2 * g * height))/g

print time