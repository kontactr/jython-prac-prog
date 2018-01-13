from array import array as A
from java.util import Arrays as AS

array_1 = A('i')
print (array_1)
for k in range(10):
   array_1.append(-k)
print(array_1)
AS.parallelSort(array_1)
for k in range(11,20):
   array_1.append(-k)
print (array_1)
AS.sort(array_1)
print (array_1)
