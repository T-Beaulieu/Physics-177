import numpy as np
import matplotlib.pyplot as plt
import week2_ex1 as int

data = np.loadtxt("velocities.txt")    
time = data[:,0]
vel  = data[:,1]
xArray  = []
yArray  = []
sum1    = 0
sum2    = 0

##Calculates using Trap rule, saves to file
sum1,xArray,yArray = int.TrapRule(time,vel)
f = open('Taylor_Integral_Results.txt','w+')
f.write('This is the integral with the Trapezoid Rule: ' + str(sum1) + '\n')
   
##Calculates using Simpsons rule, saves to file
sum2 = int.SimpRule(time,vel)
f.write('This is the integral with the Simpsons Rule: ' + str(sum2))
f.close()

##Plots Distance vs Time
plt.subplot(2,1,1)
plt.plot(xArray,yArray)
plt.title("Distance and Velocity vs Time")
plt.xlabel("Time")
plt.ylabel("Distance")

##Plots Velocity vs Time
plt.subplot(2,1,2)
plt.plot(time,vel)
plt.xlabel("Velocity")
plt.ylabel("Time")