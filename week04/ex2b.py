import numpy as np 
import matplotlib.pyplot as plt


def p(x): 
    return 924*(x ** 6) -  2772*(x ** 5) + 3150*(x ** 4) - 1680*(x ** 3) + 420*(x ** 2) - 42 * x + 1 

def pPrime(x):
    return 5544*(x ** 5) - 13860*(x ** 4) + 12600*(x ** 3) - 5040*(x ** 2) + 840*(x) - 42
    
##Initial Guess, Root 1
initialGuess = [0.0,0.18,0.32,0.58,0.8,1.0]
root = [0,0,0,0,0,0]
i = 0

for i in range(6):
    oldX = initialGuess[i]
    newX = 0.
    error = 1
    while error > 10 ** -10:
        newX = oldX - (p(oldX) / pPrime(oldX))
        error = abs(newX - oldX)
        oldX = newX
        
    root[i] = oldX
   

print "The roots are: ", root[0], ",", root[1], ",", root[2], ",", root[3], ",",
print root[4], ",", root[5]
