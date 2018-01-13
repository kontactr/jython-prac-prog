from java.util import Comparator as C
from array import array as A
from java.util import Arrays as AS

class asc(C):
  def compare(val1,val2):
       if (val1 > val2):
		return -1
       elif (val1 < val2):
		return 1
       else :
		return 0


 

array_1 = A('i')
for x in range(10):
	array_1.append(x)
print (array_1)
print (AS.sort(array_1,asc()))
