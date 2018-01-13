from java.net import ServerSocket as ss
from java.net import Socket as s
from java.io import InputStream as Is
from java.io import OutputStream as os
from java.io import FileReader as fr
from java.io import BufferedReader as br
from java.io import InputStreamReader as isr
from java.io import PrintStream as ps
from java.lang import Thread

ss1 = ss(766)

class server(object):
	def __init__(self):
		while True:
			
			self.s = ss1.accept()
			obj(self.s).start()

class obj(Thread):
	def __init__(self,x):
		self.s = x 

	def run(self):
		is1 = br(isr(self.s.getInputStream()))
		os1 = ps(self.s.getOutputStream())
		st = is1.readLine()
		global file 
		try:
			file = fr(st)
		except:
			"Exception"
		while True:
			try:
		  		x = chr(file.read())
		  		print (x)
		  		os1.print(x)
			except:
		 		break
		file.close()
		os1.print("")
		os1.close()
		is1.close()
		self.s.close()
		#file = open(st,"r")
		#for  k in file:
		#	print(k)
		#	os1.println(k)
server()