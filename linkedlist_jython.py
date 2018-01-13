from java.util  import LinkedList as ll
l1 = ll()
print (l1.add(100))
print (l1.add(1,200))
print (l1.addFirst(300))
l1.addLast(300)
print(l1.get(2))
print (l1.size())
print (l1)
k = l1.iterator()
print (type(k))
while (k.hasNext()):
	print (k.next())