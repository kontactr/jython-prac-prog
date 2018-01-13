from java.util import HashMap as hm
a = hm()
a.put("a1",1)
a.put("a2",2)
print (a.get("a1"))
print (a.get("a2"))
for k,j in zip(a.keySet(),a.values()):
  print (str(k)+" -> "+str(j))
a.remove("k1")
a.remove("k2")
print (a.isEmpty())
print (a.size())
print (a.clear())
del a
 
