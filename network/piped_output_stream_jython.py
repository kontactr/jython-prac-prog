from java.io import PipedOutputStream as po
from java.io import PipedInputStream as pi
from java.lang import Thread

class obj_input(Thread):
	def __init__(self,pout):
		self.pout = pout
	def run(self):
		print ("Writing.....")
		for k in range(10):
			self.pout.write(str(k))


class obj_output(Thread):
	def __init__(self,pin,thread_x):
		self.pin = pin
		self.thread_x = thread_x

	def run(self):
		self.thread_x.join()
		print ("Reading.....")
		while self.pin.available() > 0:
			try:
				print (chr(self.pin.read()))
			except:
				break

#object of pipedinputstream
pi_1 = pi()

#object of pipedoutputstream pass pipedinputstream bcz of reading content from 
po_1 = po(pi_1)

#create obj_input means write data 
oi = obj_input(po_1)

#create obj_output means read data
oo = obj_output(pi_1,oi)uh

#obj_input thread start
oi.start()

#obj_output thread start
oo.start()

#wait for obj_input thread (this will always be exc in instant time because 
#							 we write  this statement also in read class)
#							it is ambiguous but for saftey

oi.join()

#wait for obj_output thread
oo.join()

#for check if any deadlock occures or not means
#sucessfully run the program
print ("end")
