from java.io import PipedInputStream
from java.util import Scanner
from java.lang import Thread
import piped_interface as pii


class server(Thread):
	def __init__(self):
		self.pi = None
		self.po = None
		print ("Server start")
		print (pii.obj)

	def setup(self):
		while True:
				x = pii.obj		
				try:
					print ("yes")
					if x.pi.hasNext():

						print (x.pi.next())
					else:
						print ("no")
				except:
					pass

server().setup()