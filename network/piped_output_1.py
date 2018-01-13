from java.io import PipedOutputStream as po
from java.io import PrintStream as ps

class pip_out(object):
	def __init__(self,k):
		self.pipe = ps(po(k))
		self.call()

	def call(self):
		for k in range(10):
			self.pipe.println(str(k))
		self.pipe.close()
