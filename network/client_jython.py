from java.net import Socket
from java.io import InputStream as IS
from java.io import OutputStream as OS
from java.io import PrintStream as PS
from java.util import Scanner
from java.lang import System

class client(object):
	def __init__(self):
		self.s = Socket("localhost",777)
		self.Sc = Scanner(System.in)

	def client_run(self):
		cl_is = Scanner(self.s.getInputStream())
		cl_os = PS(self.s.getOutputStream())
		cl_os.println(self.Sc.nextLine())
		print(cl_is.nextLine())
		print(cl_is.nextLine())
		while True:
			cl_os.println(self.Sc.nextLine())
			print(cl_is.nextLine())
client().client_run()