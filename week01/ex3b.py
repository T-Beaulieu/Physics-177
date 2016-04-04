import numpy as np 
import matplotlib.pyplot as plt
 
height          = 800.0 
g               = -9.8  ##Gravity, a constont 
minVelocity     = 0.0   
maxVelocity     = 0.0
time            = 0.0
dy              = 0.0
i               = 0
var             = 0.0   ##Dummy varible 
listOfTimes     = []
intVelocity     = []

print 'Entering a positive number will give a downward initial velocity.'
print 'Entering a negative number will give an upward initial velocity.'
print 'Minumum velocity must be smaller than maximum velocity.' 
##Entering a positive number as a downward velocity is the wrong sign for the 
##calculation, but it is more intuitive and easier to deal with. I switch the 
##signs back after they are input so that the calculation comes out correct.

##Gets values for vmin and vmax
while minVelocity >= maxVelocity:
    minVelocity = float(input('Enter minimum velocity: '))
    maxVelocity = float(input('Enter maximum velocity: '))
    if minVelocity >= maxVelocity:
        print 'Please make sure minimum velocity is less than maximum velocity.'
minVelocity = -minVelocity      ##These sign changes are important so the 
maxVelocity = -maxVelocity      ##calcuation works out correctly           
 
##Caculates the time over 10 bins between vmin and vmax
dy = (maxVelocity - minVelocity) / 9
for i in range(10):
        var = minVelocity + (i * dy)
        time = ((-var) - np.sqrt(var**2 - 2 * g * height))/g
        listOfTimes.append(time)
        intVelocity.append(-var)
        

##Plots the data
plt.plot(intVelocity, listOfTimes)        
plt.title("Time to Ground vs Initial Velocity")
plt.xlabel("Initial Velocity (m/s)")
plt.ylabel("Time to Ground (s)")

##Saves the data
plt.savefig('ex3b.png',format = 'png')
np.array(listOfTimes)
np.savetxt('ex3b.txt',listOfTimes)
