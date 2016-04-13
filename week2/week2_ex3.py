import numpy as np
import week2_ex1 as int
import scipy.integrate as integrate

actualInt = 4.4
xArray    = []
yArray    = []
int1      = 0.
int1_2    = 0.
int2      = 0.
int2_2    = 0.
error1    = 0.
error2    = 0.
trash1    = []
trash2    = []

##Function we are integrating
def func(x):
    return ((x ** 4) - (2 * x) + 1)

##Converts function to array of values 
def convertToArray(xmin,xmax,N):
    dx     = float(xmax - xmin)/ (N)
    i      = 0
    var    = 0. 
    xArray = []
    yArray = []
    
        
    for i in range(N + 1): 
        var = xmin + (i * dx) 
        xArray.append(var)
        yArray.append((func(var)))
        
    return xArray,yArray    
  
  
##These use my predefined functions to get our integrals
##The trash variables are because TrapRule outputs 3 variables, only 1 needed
xArray,yArray = convertToArray(0,2,20)
int1,trash1,trash2 = int.TrapRule(xArray,yArray)
int2 = int.SimpRule(xArray,yArray)

print '\n' + "My Trapzoidal Rule gave: " + str(int1) 
print "My Simpsons Rule gave: " + str(int2) + "\n"
print "Difference between Trapazoid Rule and the real value: " + str(int1 - actualInt)
print "Difference between Simpsons Rule and real value: " + str(int2 - actualInt) + '\n'

##These are their integrals 
int1 = np.trapz(yArray,xArray,0.1)
int2 = integrate.simps(yArray,xArray)
print "Their Trapzoidal Rule gave: " + str(int1)
print "Their Simpsons Rule gave: " + str(int2) + '\n'

##This is a second calculation with bin size 10 used to estiamte error
xArray,yArray = convertToArray(0,2,10)
int1_2,trash1,trash2 = int.TrapRule(xArray,yArray)
int2_2 = int.SimpRule(xArray,yArray)
error1 = (int1_2 - int1) / 3
error2 = (int2_2 - int2) / 15
print "Trapazoidal Error is approximately: " + str(error1)
print "Simpsons Error is approximately: " + str(error2) + '\n'
print "This is the actual value: " + str(actualInt)