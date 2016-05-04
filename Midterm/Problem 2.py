import numpy as np 

##Part i
fibSeq = [1, 1]
seqNumber = 12


for i in range(1,seqNumber - 1):
    fibSeq.append((fibSeq[i] + fibSeq[i - 1]))
    
print "The sequence number", seqNumber, "is:", fibSeq[seqNumber - 1]

##Part ii
fibSeq2 = [1., 1.]
seqNumber2 = 100


for i in range(1,seqNumber2 - 1):
    fibSeq2.append((fibSeq2[i] + fibSeq2[i - 1]))
    
print "Sequence number 100 / Sequence number 99 is:", fibSeq2[99] / fibSeq2[98]