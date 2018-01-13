from java.util import ArrayList as al
a1 = al()
print (a1.add(200))
print (a1.add(300))
print (a1.get(0))
a2 = a1.toArray()
print (a2,a1)
for k in a2:
	print (k)
a1.clear()
del a1