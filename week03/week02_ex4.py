# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 19:24:39 2016
@author: jeffn_000
"""
import numpy as np


N          = 2       ##Number of bins
i          = 1
xMin       = 0.
xMax       = 1.
error      = 1.
accuracy   = 10. ** -6
newIntegral = 0.
oldIntegral = 0.

##This is the function we are integrating
def func(x):
    return (np.sin(np.sqrt(100 * x))) ** 2


##Initial Integral with 1 bin
xArray   = [xMin,xMax]
yArray   = [func(0),func(1)]
oldIntegral = np.trapz(yArray)


while error > accuracy:
    summation  = 0 
    i = 1
    dx = float((xMax - xMin)) / float(N)
    while i <= N - 1:
        summation += func(i * dx)
        i += 2
        
    newIntegral = (0.5 * oldIntegral) + (dx * summation)
    error = np.abs((newIntegral - oldIntegral) / 3.)
    oldIntegral = newIntegral
    N *= 2
    
    

    
print "The integral is: ", newIntegral
print "Number of bins at the end: ", N 