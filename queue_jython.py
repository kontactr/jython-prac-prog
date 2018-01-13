from java.util import Queue as q
from java.util import LinkedList as ll
class queue(q):
 l1 = ll() 
 def  __init__(self):
   print ("queue")
 
 def add(self,val):
  self.l1.add(val)
  
 def offer(self,val):
  self.l1.add(val)
 
 def remove(self):
  return self.l1.removeFirst()

 def poll(self):
  try:	   
	 remove()
  except Exception:
        return False
 
 def element(self):
  return self.l1.get(0)

 def peek(self):
   try: 
   	element()
   except Exception:
       return False

 def size(self):
   return self.l1.size()

 def isEmpty(self):
      try:
	 if size()>0 :
		return False
     	 else:
  		return True
      except Exception:
             return True

 def clear(self):
   self.l1.clear()
   return 0



q1 = queue()
q1.add(10)
q1.offer(20)
print (q1)
print (q1.remove())
print (q1.poll())
try:
  print (q1.element())
except Exception:
  print ("no such element")

print (q1.peek())
print (q1.size())
print (q1.isEmpty())
print (q1.clear())
del q1
