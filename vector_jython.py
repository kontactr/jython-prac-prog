from java.util import Vector as v
from java.lang import Thread 
class add(Thread):
	
	v1 = v()+

	def __init__(self,name):
		pass

	@classmethod
	def add_v(cls,num):
		cls.v1.add(num)
		print ("size\n"+str(cls.v1.size())+"size\n")
		print (cls.v1.get(cls.v1.size()-1))

	def run(self):
		for k in range(10):
			print (str(k)+" "+self.getName())
			add.add_v(k)

	

a1 = add("t1")
a2 = add("t2")
a1.start()
a2.start()