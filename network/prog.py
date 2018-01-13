from matplotlib import pyplot as p
import sys
import math as m
print ("hello world")

#val = sys.stdin.readline("Enter: ")
print ("hello world",str(50))

x,y = [],[]
for i in range(int(50)):
	x.append(i)
	y.append(m.log10(i))
x = p.plot(x,y)
p.show()
print ("hello world")