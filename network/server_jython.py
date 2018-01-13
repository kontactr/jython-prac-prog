from java.lang import Thread
from java.net import ServerSocket
from java.net import Socket
from java.io import InputStream as IS
from java.io import OutputStream as OS
from java.util import Scanner
from java.io import PrintStream

class server(object):
	def __init__(self):
		self.ss = ServerSocket(777)
		self.s = None
		print ("accpted",self.s)

	def server_run(self):
		while True:		
			self.s = self.ss.accept()
			multi_client(self.s).start()

class multi_client(Thread):
	def __init__(self,s):
		self.s = s
		self.cs_IS = None
		self.cs_OS = None

	def run(self):
		self.cs_IS = Scanner(self.s.getInputStream())
		self.cs_OS = PrintStream(self.s.getOutputStream())
		self.cs_OS.println("breaches are open...")
		x = self.cs_IS.nextLine()
		self.cs_OS.println(x+" server received")
		while True:
			x = self.cs_IS.nextLine()
			self.cs_OS.println(x+" server received")

server().server_run()