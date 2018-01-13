from java.io import DataInputStream as DI
from java.io import DataOutputStream as DO

a = str(10)
b = str(20)
di = DI(a)
do = DO(b)
c = di.read()
do.write(c)

print(a,b,c)
