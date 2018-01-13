from java.io import PipedInputStream as PI
from java.io import PipedOutputStream as PO
from java.util import Scanner as S
from java.io import PrintStream as PS

class piped_interface(object):
	def __init__(self):
		s = PI()
		self.pi =  S(s)
		self.po = PS(PO(s))
		self.obj = None
			
obj =  piped_interface()
