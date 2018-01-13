from matplotlib import pyplot as p
import math as m
a = int(input())
x,y = [],[]
for k in list(range(a,a**2)):
	print (k)
	x.append(k)
	y.append(m.log10(k))
x = p.plot(x,y)
p.show()