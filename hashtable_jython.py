from java.util import Hashtable as ht

h1 = ht()
h1.put("1",1)
h1.put("2",2)
h1.put("3",3)
print (h1.get("1"))
key = h1.keySet()
for k in key:
  print (h1.get(k))
val = h1.values()
print (val)
if (h1.isEmpty() == False):
	h1.clear()
else:
	pass
print (h1.size())
