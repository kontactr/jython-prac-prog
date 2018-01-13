from java.lang import Runtime
from java.lang import Thread

x = Runtime.getRuntime().availableProcessors()
global i
i = 0

class Thread_Class(Thread):
	
	def __init__(self):
		self.no = str(i)
	
	def run(self):
		global i
		if(i < x):
			i += 1
			p = Thread_Class()
			p.start()
			p.join()
			print (self.no+" "+self.getName())

#print (System.getProperties().list(System.out))
Thread_Class().start()
