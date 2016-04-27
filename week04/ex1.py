def f1(x,y): 
	return y * (1. + x ** 2.)

def f2(x,y):
    return 2. / (1. + x ** 2.)

x = 1.
y = 1.

for i in range(3):
    y = f2(x,y)
    x = f1(x,y)
    print x,y

