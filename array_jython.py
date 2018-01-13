from java.util import Arrays as A

l = [x for x in range(10)]
print (l)
l.sort()
print (A.binarySearch(l,3))
k = [1,2,3,4,5,6,7,8,9,0]
print (A.equals(l,k))
print (A.copyOf(l,len(l)))

