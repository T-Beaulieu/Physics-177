import numpy as np
import matplotlib.pyplot as plt 

angle       = 30    ##degrees
intVelocity = 100   ##m/s
mass        = 1    ##kg
radius      = 0.08  ##m
rho         = 1.22 
C           = 0.47  ##Coeff of drag
g           = -9.8  ##Gravity
allconst    = np.pi * radius **2 * rho * C / (2 * mass)
xArray      = [0]
yArray      = [0]
xArray2     = [0]
yArray2     = [0]
h           = 0.2

##These 2 functions give the x and y position after time t with no drag
def NoDragYPos(velY,t):
    var = (velY * t + 0.5 * g * (t ** 2))
    if var > 0: 
        return var 
    if var >= 0:
        return 0 

def NoDragXPos(velX,t):
    return (velX * t)

##System of equations for Runge Kunta
def Func(r):
    x = r[0]
    vx = r[1]
    y = r[2]
    vy = r[3]
    vtot = np.sqrt(vx**2 + vy**2)
    x = vx 
    vx = - allconst * r[1] * vtot
    y = vy 
    vy =  g - allconst * r[3] * vtot
    return np.array([x,vx,y,vy],float)

##----------------Gets vX, vY 
angle *= np.pi / 180.       ##Converts from degrees to radians
velX = intVelocity * np.cos(angle)
velY = intVelocity * np.sin(angle)



##------------------Finds Data Points
t = 0 
tend = 15 
r = np.array([0,velX,0,velY])
r1 = r.copy()
while t < tend:
    
    k1 = h * Func(r1)
    k2 = h * Func(r1 + 0.5 * k1)
    k3 = h * Func(r1 + 0.5 * k2)
    k4 = h * Func(r1 + k3)
    r1 += 1./6. * (k1 + 2.*k2 + 2.*k3 + k4) 
    
    xArray2.append(r1[0])
    yArray2.append(r1[2])
    
    ##These calculations are only in the while loop for the creation of the 
    ##gif, if you only wanted a final graph you could move them outside for 
    ##extra efficiency 
    
    yArray.append(NoDragYPos(velY,t))  
    xArray.append(NoDragXPos(velX,t))  
    t += h 
    
    '''
    This code was used to save a picture each step, which was then 
    put into a gif maker online. It saves a lot of pictures and takes a lot 
    longer to run, so I commented it out 
    
    plt.clf()
    plt.plot(xArray,yArray)
    plt.plot(xArray2,yArray2)
    plt.xlim(0,900)
    plt.ylim(0,140)
    filename = "imAt" + str(t) + ".png"
    print filename
    plt.savefig(filename)
    '''

plt.plot(xArray,yArray)
plt.plot(xArray2,yArray2)
plt.xlim(0,900)
plt.ylim(0,140)
##figure2 = plt.figure(2)