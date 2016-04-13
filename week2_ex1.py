##This function does not require equal x spacing (I think) 
def TrapRule(xlist,ylist):
    numBins = len(xlist) 
    sum     = 0    
    i       = 0 
    x2      = [0]
    y2      = [0]    
    
    for i in range(1, numBins):
        sum += ((ylist[i] + ylist[i - 1]) * 0.5 * (xlist[i] - xlist[i - 1]))
        x2.append(i)
        y2.append(sum)
    return sum,x2,y2
    
    
    
##This requires equal spacing between all x values 
def SimpRule(xlist,ylist):
     numBins = (len(xlist) - 1) 
     sum     = 0
     i       = 0
     
     for i in range(0, numBins - 1, 2):
         h     = (xlist[i + 1] - xlist[i])
         sum  += ((ylist[i]) + (4 * ylist[i + 1]) + (ylist[i + 2])) *h/3
     return sum
 
