from math import sin,log
from matplotlib import pyplot as p
a = int(input())
#print (m.log10(a))
x=[]
y=[]
for k in range(a):
	x.append(k)
	q1 = sin(k+1)
	y.append(q1)
p.plot(x,y)
p.show()
#for k in range(len(x)):
#	y[k] = log(x[k])
p.plot(x,y)
p.show()