from java.net import Socket
from java.io import InputStream
from java.io import OutputStream
from java.io import PrintStream
from java.util import Scanner

class client(object):
	def __init__(self):
		self.ss = Socket("localhost",8888)

	def start(self):
			print (Scanner(self.ss.getInputStream()).nextLine())	


client().start()